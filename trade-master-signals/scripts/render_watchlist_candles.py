#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
from html import escape
import json
import math
from pathlib import Path
import re
import sys
from textwrap import wrap
from typing import Iterable

import pandas as pd
import requests


YAHOO_HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
}
SVG_SIZE_RE = re.compile(r'<svg[^>]*\bwidth="(?P<width>[0-9.]+)"[^>]*\bheight="(?P<height>[0-9.]+)"', re.IGNORECASE)
SECTOR_ETF_MAP = {
    "Technology": "XLK",
    "Financial Services": "XLF",
    "Financial": "XLF",
    "Financials": "XLF",
    "Industrials": "XLI",
    "Healthcare": "XLV",
    "Energy": "XLE",
    "Consumer Cyclical": "XLY",
    "Consumer Defensive": "XLP",
    "Consumer Staples": "XLP",
    "Basic Materials": "XLB",
    "Utilities": "XLU",
    "Communication Services": "XLC",
    "Real Estate": "XLRE",
}


@dataclass
class WatchlistEntry:
    ticker: str
    setup_label: str
    summary: str
    master_note: str
    trigger_price: float | None = None
    trigger_label: str | None = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render daily candle charts for a trade-master watchlist.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--watchlist-file", help="JSON watchlist file with structured setup notes.")
    group.add_argument("--ticker-file", help="Plain text file with one ticker per line.")
    group.add_argument("--tickers", nargs="+", help="Ticker symbols to render.")
    parser.add_argument("--output-dir", required=True, help="Directory for charts and summary artifacts.")
    parser.add_argument("--benchmark", default="SPY", help="Benchmark ticker for RS display.")
    parser.add_argument("--period", default="18mo", help="Yahoo chart range such as 1y, 18mo, 2y.")
    parser.add_argument("--lookback", type=int, default=120, help="Number of daily bars to render.")
    parser.add_argument("--split-pages", type=int, default=0, help="If > 0, emit montage pages with this many charts per page.")
    parser.add_argument("--montage-columns", type=int, default=2, help="Number of columns for split montage pages.")
    parser.add_argument("--card-width", type=int, default=700, help="Scaled width of each chart in montage pages.")
    return parser.parse_args()


def fetch_history(ticker: str, period: str) -> pd.DataFrame:
    response = requests.get(
        f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}",
        params={
            "interval": "1d",
            "range": period,
            "includeAdjustedClose": "true",
        },
        headers=YAHOO_HEADERS,
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    result = payload.get("chart", {}).get("result", [])
    if not result:
        error = payload.get("chart", {}).get("error")
        raise ValueError(f"No Yahoo chart result returned for {ticker}: {error}")

    chart = result[0]
    timestamps = chart.get("timestamp", [])
    quote_list = chart.get("indicators", {}).get("quote", [])
    if not timestamps or not quote_list:
        raise ValueError(f"Incomplete Yahoo chart payload for {ticker}")

    quote = quote_list[0]
    history = pd.DataFrame(
        {
            "Open": quote.get("open", []),
            "High": quote.get("high", []),
            "Low": quote.get("low", []),
            "Close": quote.get("close", []),
            "Volume": quote.get("volume", []),
        },
        index=pd.to_datetime(timestamps, unit="s", utc=True),
    )
    exchange_timezone = chart.get("meta", {}).get("exchangeTimezoneName")
    if exchange_timezone:
        history.index = history.index.tz_convert(exchange_timezone).normalize().tz_localize(None)
    else:
        history.index = history.index.tz_localize(None)
    history = history.dropna(subset=["Open", "High", "Low", "Close", "Volume"]).copy()
    if history.empty:
        raise ValueError(f"No usable price history returned for {ticker}")
    return history[["Open", "High", "Low", "Close", "Volume"]]


def fetch_company_profile(ticker: str) -> dict[str, str]:
    try:
        response = requests.get(
            f"https://query1.finance.yahoo.com/v10/finance/quoteSummary/{ticker}",
            params={"modules": "assetProfile,summaryProfile"},
            headers=YAHOO_HEADERS,
            timeout=30,
        )
        response.raise_for_status()
        payload = response.json()
    except Exception:
        return {"sector": "Unknown", "industry": "Unknown"}
    result = payload.get("quoteSummary", {}).get("result", [])
    if not result:
        return {"sector": "Unknown", "industry": "Unknown"}
    asset_profile = result[0].get("assetProfile", {})
    summary_profile = result[0].get("summaryProfile", {})
    sector = asset_profile.get("sector") or summary_profile.get("sector") or "Unknown"
    industry = asset_profile.get("industry") or summary_profile.get("industry") or "Unknown"
    return {"sector": sector, "industry": industry}


def add_price_indicators(frame: pd.DataFrame) -> pd.DataFrame:
    data = frame.copy()
    data["ema8"] = data["Close"].ewm(span=8, adjust=False).mean()
    data["ema21"] = data["Close"].ewm(span=21, adjust=False).mean()
    data["sma50"] = data["Close"].rolling(50).mean()
    data["sma200"] = data["Close"].rolling(200).mean()
    data["avg_volume20"] = data["Volume"].rolling(20).mean()
    data["relative_volume20"] = data["Volume"] / data["avg_volume20"]
    data["adr_percent"] = ((data["High"] - data["Low"]) / data["Close"].shift(1) * 100).rolling(20).mean()
    return data


def compute_rs_line(stock: pd.Series, benchmark: pd.Series) -> pd.Series:
    aligned = pd.concat([stock, benchmark], axis=1, join="inner").dropna()
    aligned.columns = ["stock", "benchmark"]
    return aligned["stock"] / aligned["benchmark"]


def _polyline_points(
    values: pd.Series,
    x_values: list[float],
    min_value: float,
    max_value: float,
    top: int,
    plot_height: int,
) -> str:
    points: list[str] = []
    value_range = max(max_value - min_value, 1e-6)
    for x, value in zip(x_values, values):
        if pd.isna(value):
            continue
        y = top + plot_height - ((float(value) - min_value) / value_range * plot_height)
        points.append(f"{x:.1f},{y:.1f}")
    return " ".join(points)


def _text_block(svg: list[str], text: str, x: int, y: int, color: str, font_size: int, width: int = 38) -> int:
    lines = wrap(text, width=width) or [text]
    for index, line in enumerate(lines):
        svg.append(
            f'<text x="{x}" y="{y + index * (font_size + 6)}" fill="{color}" '
            f'font-size="{font_size}" font-family="Menlo, Consolas, monospace">{escape(line)}</text>'
        )
    return len(lines)


def _price_y(value: float, y_min: float, y_max: float, top: int, plot_height: int) -> float:
    price_range = max(y_max - y_min, 1e-6)
    return top + plot_height - ((value - y_min) / price_range * plot_height)


def build_entry_plan(
    entry: WatchlistEntry,
    latest_close: float,
    trigger_price: float,
    ema8: float,
    ema21: float,
    above_trigger: bool,
) -> tuple[list[str], float, str]:
    trigger_gap = (latest_close / trigger_price - 1) * 100 if trigger_price else 0.0
    note_lower = f"{entry.summary} {entry.master_note}".lower()
    if above_trigger:
        lines = [
            f"Entry plan: pullback hold {trigger_price:.2f}",
            f"Add only if trigger keeps acting as support",
            f"EMA8 ref: {ema8:.2f} | Extension: {trigger_gap:.2f}%",
        ]
        return lines, trigger_price, "#22c55e"

    if "8ema" in note_lower or "8 ema" in note_lower:
        lines = [
            f"Entry plan: break > {trigger_price:.2f}",
            f"Alt entry: support hold near EMA8 {ema8:.2f}",
            f"EMA21 ref: {ema21:.2f}",
        ]
    else:
        lines = [
            f"Entry plan: break > {trigger_price:.2f}",
            f"Prefer close strength instead of early anticipation",
            f"EMA8 ref: {ema8:.2f} | EMA21 ref: {ema21:.2f}",
        ]
    return lines, trigger_price, "#f97316"


def build_stop_plan(
    entry: WatchlistEntry,
    trigger_price: float,
    ema8: float,
    ema21: float,
    recent_support: float,
    above_trigger: bool,
) -> tuple[list[str], float, str]:
    note_lower = f"{entry.summary} {entry.master_note}".lower()
    if above_trigger:
        stop_price = min(trigger_price, ema21) * 0.985
        lines = [
            f"Stop guide: below trigger / EMA21",
            f"Stop ref: {stop_price:.2f}",
            f"Support refs: trigger {trigger_price:.2f}, EMA21 {ema21:.2f}",
        ]
        return lines, stop_price, "#ef4444"

    if "8ema" in note_lower or "8 ema" in note_lower:
        stop_price = min(ema21, recent_support) * 0.99
        lines = [
            "Stop guide: below EMA21 / recent retest low",
            f"Stop ref: {stop_price:.2f}",
            f"Support refs: EMA8 {ema8:.2f}, EMA21 {ema21:.2f}",
        ]
    else:
        stop_price = min(ema21, recent_support) * 0.985
        lines = [
            "Stop guide: below recent support cluster",
            f"Stop ref: {stop_price:.2f}",
            f"Support refs: support {recent_support:.2f}, EMA21 {ema21:.2f}",
        ]
    return lines, stop_price, "#ef4444"


def build_rr_comment(latest_close: float, entry_price: float, stop_price: float, above_trigger: bool) -> str:
    risk_pct = abs((entry_price / stop_price - 1) * 100) if stop_price else 0.0
    extension_pct = abs((latest_close / entry_price - 1) * 100) if entry_price else 0.0
    if above_trigger:
        if extension_pct > 3.0:
            return f"R/R: extended {extension_pct:.1f}% above entry ref, prefer retest"
        if risk_pct <= 6.0:
            return f"R/R: tight risk around {risk_pct:.1f}%, trigger hold matters"
        return f"R/R: workable only if support holds, risk about {risk_pct:.1f}%"
    if risk_pct <= 6.0:
        return f"R/R: clean break can work, initial risk about {risk_pct:.1f}%"
    return f"R/R: wide risk around {risk_pct:.1f}%, wait for tighter entry"


def build_sector_snapshot(
    profile: dict[str, str] | None,
    period: str,
    sector_history_cache: dict[str, pd.DataFrame],
) -> dict[str, str]:
    profile = profile or {"sector": "Unknown", "industry": "Unknown"}
    sector = profile.get("sector", "Unknown")
    industry = profile.get("industry", "Unknown")
    etf = SECTOR_ETF_MAP.get(sector)
    if not etf:
        return {
            "sector": sector,
            "industry": industry,
            "etf": "n/a",
            "ret5": "n/a",
            "ret20": "n/a",
            "trend": "n/a",
        }

    if etf not in sector_history_cache:
        sector_history_cache[etf] = add_price_indicators(fetch_history(etf, period))

    history = sector_history_cache[etf]
    latest = history.iloc[-1]
    close = float(latest["Close"])
    prior5 = float(history["Close"].iloc[-6]) if len(history) > 5 else float(history["Close"].iloc[0])
    prior20 = float(history["Close"].iloc[-21]) if len(history) > 20 else float(history["Close"].iloc[0])
    ret5 = (close / prior5 - 1) * 100 if prior5 else 0.0
    ret20 = (close / prior20 - 1) * 100 if prior20 else 0.0
    if close > float(latest["ema21"]) and close > float(latest["sma50"]) and ret20 > 0:
        trend = "strong"
    elif close > float(latest["sma50"]) or ret5 > 0:
        trend = "neutral"
    else:
        trend = "weak"
    return {
        "sector": sector,
        "industry": industry,
        "etf": etf,
        "ret5": f"{ret5:+.2f}%",
        "ret20": f"{ret20:+.2f}%",
        "trend": trend,
    }


def render_watchlist_chart(
    entry: WatchlistEntry,
    history: pd.DataFrame,
    benchmark_history: pd.DataFrame,
    output_path: str | Path,
    lookback: int = 120,
    profile: dict[str, str] | None = None,
    sector_snapshot: dict[str, str] | None = None,
) -> Path:
    chart = add_price_indicators(history).tail(lookback).copy()
    benchmark = benchmark_history.reindex(chart.index).dropna()
    chart = chart.loc[benchmark.index]
    rs_line = compute_rs_line(chart["Close"], benchmark["Close"]).reindex(chart.index)
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    width = 1640
    height = 1100
    left = 90
    plot_width = 980
    price_top = 80
    price_height = 560
    volume_top = 680
    volume_height = 130
    rs_top = 860
    rs_height = 140
    right_panel_x = 1120

    lows = chart["Low"]
    highs = chart["High"]
    y_min = float(lows.min()) * 0.97
    y_max = float(highs.max()) * 1.03
    volume_max = max(float(chart["Volume"].max()), 1.0)
    rs_min = float(rs_line.min()) * 0.98
    rs_max = float(rs_line.max()) * 1.02
    rs_range = max(rs_max - rs_min, 1e-6)
    x_step = plot_width / max(len(chart), 1)
    x_values = [left + (index + 0.5) * x_step for index in range(len(chart))]

    latest = chart.iloc[-1]
    prior_20_high = float(chart["High"].iloc[:-1].tail(20).max()) if len(chart) > 20 else float(chart["High"].max())
    prior_50_high = float(chart["High"].iloc[:-1].tail(50).max()) if len(chart) > 50 else float(chart["High"].max())
    trigger_price = entry.trigger_price if entry.trigger_price is not None else prior_20_high
    trigger_label = entry.trigger_label if entry.trigger_label else "Watch level"
    avg_volume20 = float(latest["avg_volume20"]) if pd.notna(latest["avg_volume20"]) else 0.0
    relative_volume20 = float(latest["relative_volume20"]) if pd.notna(latest["relative_volume20"]) else 0.0
    adr_percent = float(latest["adr_percent"]) if pd.notna(latest["adr_percent"]) else 0.0
    above_trigger = float(latest["Close"]) > trigger_price
    latest_close = float(latest["Close"])
    ema8_value = float(latest["ema8"]) if pd.notna(latest["ema8"]) else latest_close
    ema21_value = float(latest["ema21"]) if pd.notna(latest["ema21"]) else latest_close
    recent_support = float(chart["Low"].tail(10).min()) if len(chart) >= 10 else float(chart["Low"].min())
    entry_lines, entry_price, entry_color = build_entry_plan(
        entry=entry,
        latest_close=latest_close,
        trigger_price=trigger_price,
        ema8=ema8_value,
        ema21=ema21_value,
        above_trigger=above_trigger,
    )
    stop_lines, stop_price, stop_color = build_stop_plan(
        entry=entry,
        trigger_price=trigger_price,
        ema8=ema8_value,
        ema21=ema21_value,
        recent_support=recent_support,
        above_trigger=above_trigger,
    )
    rr_comment = build_rr_comment(
        latest_close=latest_close,
        entry_price=entry_price,
        stop_price=stop_price,
        above_trigger=above_trigger,
    )
    sector_snapshot = sector_snapshot or {
        "sector": (profile or {}).get("sector", "Unknown"),
        "industry": (profile or {}).get("industry", "Unknown"),
        "etf": "n/a",
        "ret5": "n/a",
        "ret20": "n/a",
        "trend": "n/a",
    }

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#07101e" />',
        f'<text x="{left}" y="34" fill="#f8fafc" font-size="26" font-family="Menlo, Consolas, monospace">{entry.ticker} Daily Setup Chart</text>',
        f'<text x="{left}" y="58" fill="#94a3b8" font-size="15" font-family="Menlo, Consolas, monospace">Setup: {escape(entry.setup_label)} | Lookback: {lookback} sessions</text>',
    ]

    for step in range(6):
        y = price_top + step * (price_height / 5)
        price = y_max - step * ((y_max - y_min) / 5)
        svg.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left + plot_width}" y2="{y:.1f}" stroke="#1e293b" stroke-width="1" />')
        svg.append(
            f'<text x="{left - 12}" y="{y + 4:.1f}" fill="#94a3b8" font-size="12" text-anchor="end" '
            f'font-family="Menlo, Consolas, monospace">{price:.2f}</text>'
        )

    for index, (_, row) in enumerate(chart.iterrows()):
        x = x_values[index]
        open_price = float(row["Open"])
        close_price = float(row["Close"])
        high_price = float(row["High"])
        low_price = float(row["Low"])
        color = "#22c55e" if close_price >= open_price else "#ef4444"
        wick_top = _price_y(high_price, y_min, y_max, price_top, price_height)
        wick_bottom = _price_y(low_price, y_min, y_max, price_top, price_height)
        body_top = _price_y(max(open_price, close_price), y_min, y_max, price_top, price_height)
        body_bottom = _price_y(min(open_price, close_price), y_min, y_max, price_top, price_height)
        body_height = max(body_bottom - body_top, 1.5)
        body_width = max(x_step * 0.58, 2.0)
        svg.append(f'<line x1="{x:.1f}" y1="{wick_top:.1f}" x2="{x:.1f}" y2="{wick_bottom:.1f}" stroke="{color}" stroke-width="1.3" />')
        svg.append(
            f'<rect x="{x - body_width / 2:.1f}" y="{body_top:.1f}" width="{body_width:.1f}" height="{body_height:.1f}" fill="{color}" opacity="0.9" />'
        )
        volume_height_px = float(row["Volume"]) / volume_max * volume_height
        svg.append(
            f'<rect x="{x - body_width / 2:.1f}" y="{volume_top + volume_height - volume_height_px:.1f}" '
            f'width="{body_width:.1f}" height="{volume_height_px:.1f}" fill="{color}" opacity="0.48" />'
        )

    indicator_specs = [
        ("ema8", "#38bdf8", "EMA 8"),
        ("ema21", "#f59e0b", "EMA 21"),
        ("sma50", "#a78bfa", "SMA 50"),
        ("sma200", "#f97316", "SMA 200"),
    ]
    for legend_index, (column, color, label) in enumerate(indicator_specs):
        points = _polyline_points(chart[column], x_values, y_min, y_max, price_top, price_height)
        svg.append(f'<polyline points="{points}" fill="none" stroke="{color}" stroke-width="2" />')
        svg.append(
            f'<text x="{right_panel_x}" y="{145 + legend_index * 20}" fill="{color}" '
            f'font-size="13" font-family="Menlo, Consolas, monospace">{label}</text>'
        )

    trigger_y = _price_y(trigger_price, y_min, y_max, price_top, price_height)
    entry_zone_top_price = max(entry_price, ema8_value if above_trigger else entry_price * 1.005)
    entry_zone_bottom_price = min(entry_price, trigger_price if above_trigger else entry_price)
    entry_zone_top_y = _price_y(entry_zone_top_price, y_min, y_max, price_top, price_height)
    entry_zone_bottom_y = _price_y(entry_zone_bottom_price, y_min, y_max, price_top, price_height)
    entry_zone_y = min(entry_zone_top_y, entry_zone_bottom_y)
    entry_zone_height = max(abs(entry_zone_bottom_y - entry_zone_top_y), 10.0)
    svg.append(
        f'<rect x="{left}" y="{entry_zone_y:.1f}" width="{plot_width}" height="{entry_zone_height:.1f}" fill="#22c55e" opacity="0.08" />'
    )
    svg.append(
        f'<line x1="{left}" y1="{trigger_y:.1f}" x2="{left + plot_width}" y2="{trigger_y:.1f}" '
        f'stroke="#eab308" stroke-dasharray="6 4" stroke-width="1.5" />'
    )
    svg.append(
        f'<text x="{left + plot_width + 10}" y="{trigger_y + 4:.1f}" fill="#eab308" font-size="12" '
        f'font-family="Menlo, Consolas, monospace">{escape(trigger_label)} {trigger_price:.2f}</text>'
    )

    entry_y = _price_y(entry_price, y_min, y_max, price_top, price_height)
    svg.append(
        f'<line x1="{left}" y1="{entry_y:.1f}" x2="{left + plot_width}" y2="{entry_y:.1f}" '
        f'stroke="{entry_color}" stroke-dasharray="2 6" stroke-width="1.2" />'
    )
    svg.append(
        f'<text x="{left + plot_width + 10}" y="{entry_y - 10:.1f}" fill="{entry_color}" font-size="12" '
        f'font-family="Menlo, Consolas, monospace">Entry ref {entry_price:.2f}</text>'
    )

    stop_y = _price_y(stop_price, y_min, y_max, price_top, price_height)
    invalid_zone_y = stop_y
    invalid_zone_height = max(price_top + price_height - stop_y, 12.0)
    svg.append(
        f'<rect x="{left}" y="{invalid_zone_y:.1f}" width="{plot_width}" height="{invalid_zone_height:.1f}" fill="#ef4444" opacity="0.08" />'
    )
    svg.append(
        f'<line x1="{left}" y1="{stop_y:.1f}" x2="{left + plot_width}" y2="{stop_y:.1f}" '
        f'stroke="{stop_color}" stroke-dasharray="8 4" stroke-width="1.2" />'
    )
    svg.append(
        f'<text x="{left + plot_width + 10}" y="{stop_y + 16:.1f}" fill="{stop_color}" font-size="12" '
        f'font-family="Menlo, Consolas, monospace">Stop ref {stop_price:.2f}</text>'
    )
    svg.append(
        f'<text x="{left + plot_width + 10}" y="{entry_zone_y - 10:.1f}" fill="#22c55e" font-size="12" '
        f'font-family="Menlo, Consolas, monospace">Entry zone</text>'
    )
    svg.append(
        f'<text x="{left + plot_width + 10}" y="{min(price_top + price_height - 8, stop_y + 34):.1f}" fill="#ef4444" font-size="12" '
        f'font-family="Menlo, Consolas, monospace">Invalid below</text>'
    )

    prior_50_y = _price_y(prior_50_high, y_min, y_max, price_top, price_height)
    svg.append(
        f'<line x1="{left}" y1="{prior_50_y:.1f}" x2="{left + plot_width}" y2="{prior_50_y:.1f}" '
        f'stroke="#14b8a6" stroke-dasharray="3 5" stroke-width="1.0" />'
    )
    svg.append(
        f'<text x="{left + plot_width + 10}" y="{prior_50_y + 4:.1f}" fill="#14b8a6" font-size="12" '
        f'font-family="Menlo, Consolas, monospace">50d pivot {prior_50_high:.2f}</text>'
    )

    latest_y = _price_y(latest_close, y_min, y_max, price_top, price_height)
    svg.append(f'<circle cx="{x_values[-1]:.1f}" cy="{latest_y:.1f}" r="4" fill="#f8fafc" />')
    svg.append(
        f'<text x="{x_values[-1] + 10:.1f}" y="{latest_y - 10:.1f}" fill="#f8fafc" font-size="12" '
        f'font-family="Menlo, Consolas, monospace">Close {latest_close:.2f}</text>'
    )

    rs_points = _polyline_points(rs_line, x_values, rs_min, rs_max, rs_top, rs_height)
    svg.append(f'<polyline points="{rs_points}" fill="none" stroke="#22c55e" stroke-width="2.1" />')
    for step in range(4):
        y = rs_top + step * (rs_height / 3)
        value = rs_max - step * (rs_range / 3)
        svg.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left + plot_width}" y2="{y:.1f}" stroke="#1e293b" stroke-width="1" />')
        svg.append(
            f'<text x="{left - 12}" y="{y + 4:.1f}" fill="#94a3b8" font-size="12" text-anchor="end" '
            f'font-family="Menlo, Consolas, monospace">{value:.3f}</text>'
        )

    svg.append(f'<text x="{left}" y="{volume_top - 12}" fill="#94a3b8" font-size="13" font-family="Menlo, Consolas, monospace">Volume</text>')
    svg.append(
        f'<text x="{left}" y="{rs_top - 12}" fill="#94a3b8" font-size="13" font-family="Menlo, Consolas, monospace">Relative Strength vs SPY (daily close ratio)</text>'
    )

    info_lines = [
        f"Close: {latest_close:.2f}",
        f"Trigger status: {'above watch level' if above_trigger else 'below watch level'}",
        f"Entry ref: {entry_price:.2f}",
        f"Stop ref: {stop_price:.2f}",
        f"20d pivot: {prior_20_high:.2f}",
        f"50d pivot: {prior_50_high:.2f}",
        f"Rel volume 20d: {relative_volume20:.2f}",
        f"Avg volume 20d: {avg_volume20:,.0f}",
        f"ADR 20d: {adr_percent:.2f}%",
        f"Above EMA 8: {'yes' if latest_close > float(latest['ema8']) else 'no'}",
        f"Above EMA 21: {'yes' if latest_close > float(latest['ema21']) else 'no'}",
        f"Above SMA 50: {'yes' if latest_close > float(latest['sma50']) else 'no'}",
    ]
    for index, line in enumerate(info_lines):
        svg.append(
            f'<text x="{right_panel_x}" y="{250 + index * 23}" fill="#e2e8f0" font-size="14" font-family="Menlo, Consolas, monospace">{escape(line)}</text>'
        )

    sector_header_y = 515
    svg.append(
        f'<text x="{right_panel_x}" y="{sector_header_y}" fill="#38bdf8" font-size="14" font-family="Menlo, Consolas, monospace">Sector Snapshot</text>'
    )
    sector_lines = [
        f"Sector: {sector_snapshot['sector']} | ETF: {sector_snapshot['etf']}",
        f"Industry: {sector_snapshot['industry']}",
        f"Sector 5d: {sector_snapshot['ret5']} | 20d: {sector_snapshot['ret20']}",
        f"Sector trend: {sector_snapshot['trend']}",
    ]
    for index, line in enumerate(sector_lines):
        svg.append(
            f'<text x="{right_panel_x}" y="{sector_header_y + 22 + index * 18}" fill="#f8fafc" font-size="13" font-family="Menlo, Consolas, monospace">{escape(line)}</text>'
        )

    entry_header_y = 620
    svg.append(
        f'<text x="{right_panel_x}" y="{entry_header_y}" fill="{entry_color}" font-size="14" font-family="Menlo, Consolas, monospace">Entry Guide</text>'
    )
    for index, line in enumerate(entry_lines):
        svg.append(
            f'<text x="{right_panel_x}" y="{entry_header_y + 22 + index * 20}" fill="#f8fafc" font-size="13" font-family="Menlo, Consolas, monospace">{escape(line)}</text>'
        )
    svg.append(
        f'<text x="{right_panel_x}" y="{entry_header_y + 86}" fill="#cbd5e1" font-size="13" font-family="Menlo, Consolas, monospace">{escape(rr_comment)}</text>'
    )

    risk_header_y = 715
    svg.append(
        f'<text x="{right_panel_x}" y="{risk_header_y}" fill="{stop_color}" font-size="14" font-family="Menlo, Consolas, monospace">Risk Guide</text>'
    )
    for index, line in enumerate(stop_lines):
        svg.append(
            f'<text x="{right_panel_x}" y="{risk_header_y + 22 + index * 20}" fill="#f8fafc" font-size="13" font-family="Menlo, Consolas, monospace">{escape(line)}</text>'
        )

    cursor_y = 790
    cursor_y += _text_block(svg, f"Summary: {entry.summary}", right_panel_x, cursor_y, "#f8fafc", 14, width=40) * 20
    cursor_y += 12
    _text_block(svg, f"Master note: {entry.master_note}", right_panel_x, cursor_y, "#94a3b8", 13, width=42)

    svg.append("</svg>")
    output_file.write_text("\n".join(svg))
    return output_file


def render_watchlist_index(entries: list[WatchlistEntry], output_path: str | Path, chart_dir_name: str = "charts") -> Path:
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    cards: list[str] = []
    for entry in entries:
        cards.append(
            f"""
            <article class="card">
              <h2>{escape(entry.ticker)} <span>{escape(entry.setup_label)}</span></h2>
              <p>{escape(entry.summary)}</p>
              <img src="{chart_dir_name}/{escape(entry.ticker)}.svg" alt="{escape(entry.ticker)} chart" loading="lazy" />
              <pre>{escape(entry.master_note)}</pre>
            </article>
            """
        )
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Trade Master Watchlist</title>
  <style>
    :root {{
      color-scheme: dark;
      --bg: #06101d;
      --panel: rgba(15, 23, 42, 0.88);
      --border: rgba(148, 163, 184, 0.18);
      --text: #e2e8f0;
      --muted: #94a3b8;
      --accent: #38bdf8;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: "SF Mono", "Menlo", "Consolas", monospace;
      background:
        radial-gradient(circle at top left, rgba(56, 189, 248, 0.16), transparent 32%),
        radial-gradient(circle at top right, rgba(34, 197, 94, 0.10), transparent 28%),
        linear-gradient(180deg, #050c16 0%, var(--bg) 100%);
      color: var(--text);
    }}
    main {{
      width: min(1440px, calc(100vw - 32px));
      margin: 0 auto;
      padding: 32px 0 64px;
    }}
    header {{
      margin-bottom: 28px;
      padding: 24px;
      border: 1px solid var(--border);
      border-radius: 22px;
      background: rgba(7, 16, 30, 0.82);
      backdrop-filter: blur(12px);
    }}
    h1 {{
      margin: 0 0 8px;
      font-size: clamp(28px, 4vw, 42px);
    }}
    header p {{
      margin: 0;
      color: var(--muted);
      line-height: 1.6;
      max-width: 920px;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
      gap: 18px;
    }}
    .card {{
      margin: 0;
      padding: 18px;
      border: 1px solid var(--border);
      border-radius: 20px;
      background: var(--panel);
      box-shadow: 0 24px 60px rgba(2, 8, 23, 0.35);
    }}
    .card h2 {{
      margin: 0 0 10px;
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      align-items: baseline;
      font-size: 22px;
    }}
    .card h2 span {{
      color: var(--accent);
      font-size: 13px;
      letter-spacing: 0.06em;
      text-transform: uppercase;
    }}
    .card p {{
      margin: 0 0 14px;
      color: var(--text);
      line-height: 1.55;
    }}
    .card img {{
      width: 100%;
      border-radius: 16px;
      border: 1px solid rgba(148, 163, 184, 0.14);
      background: #07101e;
      display: block;
    }}
    .card pre {{
      margin: 14px 0 0;
      white-space: pre-wrap;
      line-height: 1.5;
      color: var(--muted);
      font-size: 12px;
    }}
  </style>
</head>
<body>
  <main>
    <header>
      <h1>Trade Master Watchlist</h1>
      <p>Daily setup charts generated from live market data. Each chart shows candles, EMA 8, EMA 21, SMA 50, SMA 200, a watch level, 50-day pivot context, volume, and daily relative strength versus SPY.</p>
    </header>
    <section class="grid">
      {"".join(cards)}
    </section>
  </main>
</body>
</html>
"""
    output_file.write_text(html)
    return output_file


def _read_svg_parts(path: Path) -> tuple[float, float, str]:
    text = path.read_text()
    size_match = SVG_SIZE_RE.search(text)
    if not size_match:
        raise ValueError(f"Could not read width/height from {path}")
    width = float(size_match.group("width"))
    height = float(size_match.group("height"))
    start = text.find(">") + 1
    end = text.rfind("</svg>")
    if start <= 0 or end < 0:
        raise ValueError(f"Could not extract SVG body from {path}")
    return width, height, text[start:end].strip()


def render_split_montage_pages(
    chart_paths: list[Path],
    output_dir: Path,
    charts_per_page: int,
    columns: int,
    card_width: int,
    title_prefix: str,
) -> list[Path]:
    if not chart_paths:
        return []

    base_width, base_height, _ = _read_svg_parts(chart_paths[0])
    scale = card_width / base_width
    card_height = math.ceil(base_height * scale)
    gap = 20
    padding = 28
    header_height = 96
    pages: list[Path] = []

    for offset in range(0, len(chart_paths), charts_per_page):
        chunk = chart_paths[offset : offset + charts_per_page]
        rows = math.ceil(len(chunk) / columns)
        total_width = padding * 2 + columns * card_width + (columns - 1) * gap
        total_height = header_height + padding + rows * card_height + (rows - 1) * gap + padding
        page_num = offset // charts_per_page + 1
        parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{total_width}" height="{total_height}" viewBox="0 0 {total_width} {total_height}">',
            '<defs>',
            '  <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">',
            '    <stop offset="0%" stop-color="#040b14" />',
            '    <stop offset="100%" stop-color="#06101d" />',
            '  </linearGradient>',
            '</defs>',
            f'<rect width="{total_width}" height="{total_height}" fill="url(#bg)" />',
            f'<text x="{padding}" y="42" fill="#f8fafc" font-size="34" font-family="Menlo, Consolas, monospace">{escape(title_prefix)} · Page {page_num}</text>',
            f'<text x="{padding}" y="68" fill="#94a3b8" font-size="16" font-family="Menlo, Consolas, monospace">{len(chunk)} tickers | split montage page</text>',
        ]
        for index, path in enumerate(chunk):
            _, _, body = _read_svg_parts(path)
            row = index // columns
            column = index % columns
            x = padding + column * (card_width + gap)
            y = header_height + row * (card_height + gap)
            parts.append(f'<g transform="translate({x},{y}) scale({scale:.8f})">{body}</g>')
        parts.append("</svg>")
        page_path = output_dir / f"watchlist_page_{page_num}.svg"
        page_path.write_text("\n".join(parts))
        pages.append(page_path)
    return pages


def load_watchlist_entries(args: argparse.Namespace) -> list[WatchlistEntry]:
    if args.watchlist_file:
        raw_entries = json.loads(Path(args.watchlist_file).read_text())
        return [WatchlistEntry(**entry) for entry in raw_entries]

    if args.ticker_file:
        tickers = [line.strip().upper() for line in Path(args.ticker_file).read_text().splitlines() if line.strip()]
    else:
        tickers = [ticker.upper() for ticker in args.tickers]
    return [
        WatchlistEntry(
            ticker=ticker,
            setup_label="Unspecified setup",
            summary="Ticker provided without structured trade-master notes.",
            master_note=f"${ticker} generated from ticker-only input.",
        )
        for ticker in tickers
    ]


def to_summary(entry: WatchlistEntry, close: float, trigger: float | None, trigger_status: str) -> dict[str, object]:
    return {
        "ticker": entry.ticker,
        "setup_label": entry.setup_label,
        "close": round(close, 2),
        "trigger_price": round(trigger, 2) if trigger is not None else None,
        "trigger_status": trigger_status,
    }


def main() -> int:
    args = parse_args()
    entries = load_watchlist_entries(args)
    output_dir = Path(args.output_dir)
    charts_dir = output_dir / "charts"
    output_dir.mkdir(parents=True, exist_ok=True)
    charts_dir.mkdir(parents=True, exist_ok=True)

    benchmark_history = fetch_history(args.benchmark, period=args.period)
    profile_cache: dict[str, dict[str, str]] = {}
    sector_history_cache: dict[str, pd.DataFrame] = {}
    generated: list[WatchlistEntry] = []
    summaries: list[dict[str, object]] = []
    failed: dict[str, str] = {}

    for entry in entries:
        try:
            history = fetch_history(entry.ticker, period=args.period)
            if entry.ticker not in profile_cache:
                profile_cache[entry.ticker] = fetch_company_profile(entry.ticker)
            profile = profile_cache[entry.ticker]
            sector_snapshot = build_sector_snapshot(
                profile=profile,
                period=args.period,
                sector_history_cache=sector_history_cache,
            )
            chart_path = render_watchlist_chart(
                entry=entry,
                history=history,
                benchmark_history=benchmark_history,
                output_path=charts_dir / f"{entry.ticker}.svg",
                lookback=args.lookback,
                profile=profile,
                sector_snapshot=sector_snapshot,
            )
            chart_text = chart_path.read_text()
            close_match = re.search(r"Close: ([0-9.]+)", chart_text)
            trigger_match = re.search(r"Watch level ([0-9.]+)|Break above ([0-9.]+)|Close above ([0-9.]+)|Resistance ([0-9.]+)|Clear area ([0-9.]+)", chart_text)
            trigger_status_match = re.search(r"Trigger status: ([^<]+)", chart_text)
            generated.append(entry)
            summaries.append(
                to_summary(
                    entry,
                    close=float(close_match.group(1)) if close_match else float("nan"),
                    trigger=float(next(group for group in trigger_match.groups() if group is not None)) if trigger_match else entry.trigger_price,
                    trigger_status=trigger_status_match.group(1) if trigger_status_match else "unknown",
                )
            )
            print(f"[done] {entry.ticker}")
        except Exception as exc:
            failed[entry.ticker] = str(exc)
            print(f"[warn] {entry.ticker}: {exc}", file=sys.stderr)

    render_watchlist_index(generated, output_dir / "index.html")
    montage_pages: list[str] = []
    if args.split_pages > 0:
        chart_paths = [charts_dir / f"{entry.ticker}.svg" for entry in generated]
        montage_pages = [
            str(path)
            for path in render_split_montage_pages(
                chart_paths=chart_paths,
                output_dir=output_dir,
                charts_per_page=args.split_pages,
                columns=args.montage_columns,
                card_width=args.card_width,
                title_prefix="Trade Master Watchlist",
            )
        ]

    summary = {
        "generated_count": len(generated),
        "generated_tickers": [entry.ticker for entry in generated],
        "chart_pages": montage_pages,
        "ticker_summaries": summaries,
        "failed": failed,
    }
    (output_dir / "run_summary.json").write_text(json.dumps(summary, indent=2))
    print(f"Wrote watchlist output to {output_dir}")
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
