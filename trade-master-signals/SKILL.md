---
name: trade-master-signals
description: Learn repeatable trade signals and strategy patterns from posts by named trade masters, organize multiple strategies per master, translate them into scanner-ready rules, and generate supporting daily candle charts for watchlists or named tickers. Use when Codex needs to infer setups from chart posts, annotate a master's vocabulary, structure signal logic, compare examples across masters, prepare market-wide ticker scans from learned patterns, or render annotated setup charts from live market data.
---

# Trade Master Signals

## Overview

Infer reusable trading setups from concrete examples instead of treating each post as a one-off stock pick. Build a structured library of trade-master vocabulary, strategies, examples, and scan translations so the skill can improve over time as more posts and scanner details are added.

## Workflow

1. Start from raw artifacts.
Use the actual post text, chart image, and any user annotations before inferring a strategy. Prefer concrete evidence over generic trading lore.

2. Identify whether the post expresses a reusable pattern.
Separate "this ticker looks good" from "this ticker demonstrates a repeatable setup." Create or update a strategy only when the post contains a recognizable sequence, vocabulary, or chart structure that could generalize.

If the post says "another example" or similar language, treat that as strong evidence that the master is referencing an existing recurring setup rather than improvising a one-off idea.

3. Translate trade-master language into explicit structure.
Map informal terms such as "fake break," "squat," "tight," or "pivot reclaim" into observable conditions. Keep both:
- the master's original phrasing
- the normalized interpretation

If the master explicitly says to know the levels, preserve the referenced support, resistance, or gap levels as part of the setup logic instead of paraphrasing them away.
If the master mentions liquidity, float, or thin trading, preserve those as contextual filters around the setup rather than confusing them with the chart trigger itself.
If the post discusses major indices or ETFs such as `SPY` or `QQQ`, treat it as market-context evidence unless the post clearly defines a tradeable single-instrument setup.
If the post references a moving average such as `8ema` as part of the entry zone, preserve it as dynamic support or resistance inside the setup rather than collapsing everything into a single horizontal level.
If the post references higher-timeframe support language such as `8 week support`, `10 week`, or `8 week support pivot`, preserve that weekly support interaction explicitly instead of flattening it into a generic daily pullback.
If the post says a support level is being tested repeatedly, preserve that pressure as part of the regime logic because repeated tests can materially change the odds of failure.
If the post discusses management rather than entry, preserve the management rule explicitly. Notes about trimming, extension, or leadership often describe reusable heuristics even when they are not standalone setup triggers.
If the post advises preserving mental capital, staying cautious, or not forcing trades, preserve that as master-level participation guidance rather than forcing it into a directional setup family.
If the post explicitly frames a conditional short entry on a single stock, preserve it as a stock-specific bearish setup rather than collapsing it into index-regime commentary.
If the post mentions `RS`, `RS line`, `RS Rating`, or phrases like `RS new high before price`, interpret them using [references/rs-glossary.md](references/rs-glossary.md) instead of generic trading shorthand.
If the post explains how tops or bottoms develop over time, preserve that as regime-framework knowledge. Educational posts about buyer exhaustion, breadth deterioration, or rolling-over structure should inform market-context interpretation even when they are not tied to a precise entry trigger.
If the post is a simplified system diagram rather than a ticker-specific chart, preserve the geometry explicitly: the reference level, the undercut or reclaim, the moving-average role, the intended entry zone, and the stop placement.
If the post is a checklist or acronym-based stock-selection framework, preserve each gate separately and distinguish company-quality filters from market-regime filters and from actual chart-entry triggers.
If the post teaches a named chart-pattern taxonomy, preserve both layers: the specific pattern mechanics when they are shown, and the broader pattern library when the post is summarizing multiple valid bases.
If the post is a hard numeric screen, preserve every threshold exactly and keep the screen separate from looser narrative frameworks. Explicit valuation, leverage, growth, and size cutoffs should survive normalization.
If the post teaches a platform-specific indicator workflow, preserve the exact tool, anchor event, configuration values, and the purpose of the resulting chart reference. Do not reduce a configured indicator to a generic moving average or support line.
If the post teaches a management heuristic with numeric volatility thresholds, preserve the exact range or multiple, what the threshold means, and whether it is a filter, a trim signal, or a final exit rule.
If the post shares a favorite indicator stack, preserve the indicator names, authors when given, and the role each tool plays. Treat the stack as a reusable toolkit layer rather than a buy trigger by itself.
If the post teaches a waiting rule around a known catalyst such as earnings, preserve the catalyst, the wait duration, what behavior it is meant to avoid, and which opposite behavior the master prefers instead.
If the post describes a multi-stage watchlist workflow, preserve the pipeline order, the source watchlists, the selection criteria used to promote names, and the meaning of each final bucket.
If the post states a general rule about environment or situational awareness, preserve it as a regime-gating heuristic. Rules about the setup being secondary to the tape should influence ranking and participation across all strategy families.
If the post combines a higher-timeframe setup with a lower-timeframe pivot for risk definition, preserve both layers explicitly. The lower timeframe may refine entry quality without changing the broader setup family.
If the post teaches how to validate or reject a breakout, preserve those rules as breakout-quality heuristics. Volume confirmation, re-tests, candle closes, and buffer rules can sit on top of multiple setup families rather than replacing them.
If the post links a sector ETF setup to individual stock selection, preserve the top-down workflow explicitly. The ETF can act as the group-level trigger while the constituent chart provides the specific trade candidate.
If the post is a basket of tickers described as examples of the same setup, treat the grouped list as cross-sectional evidence for a reusable pattern rather than as a loose watchlist with no shared structure.

4. Store multiple strategies per trade master.
Do not force all examples from a master into one pattern. Split them when the setup logic, timeframe, or trigger sequence is meaningfully different.

5. Record uncertainty explicitly.
If a post is ambiguous, preserve that ambiguity. Mark confidence as low or medium and explain what is inferred versus directly shown.
If the master says a chart "had all the ingredients" or urges the reader to study it, treat that as a strong canonical example for the existing setup family and preserve the named ingredients explicitly.
If the user proposes an extension the master did not state directly, preserve it as an inference or candidate subtype rather than promoting it to confirmed master vocabulary.

6. Translate patterns into scanner-ready rules only after the setup is defined.
Use the user's existing project and terminology once available. Avoid inventing technical fields or thresholds the scanner does not support.

7. Generate charts only after the setup notes are structured enough to preserve.
When the user asks for candle charts or watchlist visuals, preserve the master's original note, normalized setup label, and any explicit trigger price before rendering. Use `scripts/render_watchlist_candles.py` so the chart workflow stays deterministic and portable.

## Core Outputs

When extracting a new setup, produce these artifacts:

- A normalized strategy record following [references/signal-schema.md](references/signal-schema.md)
- A trade-master vocabulary update in [references/trade-masters.md](references/trade-masters.md)
- One or more annotated examples in [references/examples.md](references/examples.md)
- A scan translation draft using [references/scan-integration.md](references/scan-integration.md) once the scanner project is known

When the user also wants chart output, add:

- A structured watchlist JSON file with `ticker`, `setup_label`, `summary`, `master_note`, and optional `trigger_price` and `trigger_label`
- One SVG candle chart per ticker generated by `scripts/render_watchlist_candles.py`
- Optional split montage pages if the user wants a combined visual overview

## Interpretation Rules

- Prefer sequence over isolated indicators. A good setup usually has an order of events, not just a single signal.
- Preserve timeframe if the chart or post implies it.
- Keep multi-timeframe roles explicit when the post references them, such as monthly support defining context and daily structure defining the trigger.
- Preserve higher-timeframe support language as its own structure. An `8 week support pivot` is not interchangeable with a generic daily bounce.
- Preserve diagrammatic system posts as reusable frameworks. If the master teaches with a sketch instead of a real ticker chart, keep the structural roles of the level, the undercut, the reclaim, the `8 EMA`, the entry, and the stop.
- Preserve acronym and checklist frameworks as selection layers. A framework like `CAN SLIM` should sit above chart entries by defining which names and which environments qualify before timing is considered.
- Preserve named pattern libraries as timing frameworks. A master can use a broad taxonomy such as O'Neil base patterns to choose the entry archetype, while a separate selection framework decides which stocks deserve attention first.
- Preserve numeric screens as exact gates. When a master gives specific cutoffs such as P/E, debt/equity, PEG, EPS growth, or market-cap bounds, keep them as explicit screen criteria rather than paraphrased notions of quality.
- Preserve platform-specific indicator configurations as reference frameworks. If a master specifies how to draw or configure an indicator such as Anchored VWAP, keep the anchor event and exact settings as part of the knowledge rather than flattening it into a vague support concept.
- Preserve volatility heuristics as exact operating ranges. If a master says ADR between `3%` and `10%` is the sweet spot or that `3x ATR` from the `50-day SMA` marks extension, keep those numbers and their decision role intact.
- Preserve indicator stacks as toolkit frameworks. A named list of favorite indicators should stay separate from stock-selection filters and separate from entry or exit triggers.
- Preserve catalyst waiting rules as participation filters. If a master says to wait `3 trading days` after an earnings gap down, keep that delay, the reason for the delay, and the preferred alternative focus area such as strong earnings gap-ups.
- Preserve watchlist pipelines as workflow frameworks. If a master moves names from discovery lists into a FocusList and then into sub-buckets like `A` and `B`, keep the promotion logic and bucket meaning explicit.
- Distinguish stock-specific setups from market-regime signals. Index posts may be best stored as contextual filters for later stock selection rather than as standalone stock strategies.
- Distinguish stock-specific bearish setups from bearish market-regime warnings. A short-entry idea on one name should not be merged into broad tape commentary just because the bias is negative.
- Preserve market bias explicitly for index-regime signals. Broad-tape posts can be bullish, bearish, or transitional, and that distinction should remain visible for downstream scan gating.
- Keep higher-timeframe market-regime signals separate from lower-timeframe tape commentary when the trigger materially changes, such as a weekly EMA crossover versus a daily moving-average rejection.
- Keep structurally different daily market warnings separate when the trigger materially changes, such as a failed rally into declining moving averages versus a decisive loss of the 200 SMA after an EMA crossover.
- When multiple posts show the same ticker before and after resolution, treat them as linked evidence for one strategy unless the trigger logic materially changes.
- When a post names several tickers as examples of one setup, treat that basket as evidence that the master is naming a reusable family across multiple charts rather than making isolated stock calls.
- Preserve trade-master vocabulary even when normalizing it.
- Treat repeated master-level preference statements as priority heuristics. If a master says a certain style continues to be their best trade, preserve that as a weighting cue across relevant strategy families.
- Preserve relative-strength leadership and extension management as separate signals. A post can simultaneously describe why a name is a leader and why it is no longer in the best entry zone.
- Preserve neutral or cautionary participation guidance as a separate layer of regime interpretation. Advice about not forcing trades or preserving mental capital should influence exposure posture even when it does not create a new chart pattern.
- Preserve regime-framework posts separately from trigger posts. Explanations of topping processes, breadth deterioration, or rolling-over psychology can sharpen how existing market-context families are weighted even before a breakdown fully resolves.
- Preserve environment-first rules explicitly. If the master says the best setup can still fail in the wrong environment, treat market context as a gating layer over otherwise attractive setups.
- Preserve multi-timeframe entry refinement when present. A daily or swing thesis paired with a `30 min pivot` or similar lower-timeframe trigger should keep both the broader idea and the tighter-risk execution detail.
- Distinguish the first higher-timeframe support pivot from a later support retest when the stock remains a momentum leader. A retest can be a secondary entry, but mark clearly whether that logic comes from the master or from user inference.
- Preserve breakout-validation frameworks separately from breakout setups. Rules about volume, re-tests, closing strength, and confirmation buffers should help confirm or reject many families instead of being forced into a single chart pattern.
- Preserve top-down setup logic when present. A sector or industry ETF can be the screening lens, while the actual trade candidate may be one of the strongest names inside that group.
- Favor conservative interpretation when the post does not show enough detail.
- Distinguish chart observations from execution assumptions.
- Do not claim a setup is validated historically unless the user supplies backtest or forward-test evidence.
- Do not generate broker or auto-trading instructions unless the user explicitly asks.

## Strategy Boundaries

Create a new strategy when any of these change materially:

- the sequence of events
- the dominant timeframe
- the type of trigger
- the type of support or resistance interaction
- the intended trade style, such as continuation versus reversal

Otherwise, update an existing strategy with another example.

## Working With The Scanner Project

When the user provides an existing market-scanning project:

1. Inspect the project before inventing scan syntax.
2. Reuse the project's existing concepts, indicators, naming, and thresholds.
3. Translate each strategy into the narrowest rule set the project can actually express.
4. If the project cannot express an element of the setup, record the gap instead of pretending it can.
5. Keep the strategy definition independent from any single scanner implementation so it can evolve later.

Use [references/scan-integration.md](references/scan-integration.md) as the canonical place for scanner mapping notes.

## Chart Script

Use `scripts/render_watchlist_candles.py` when the user wants daily candle charts for one ticker, a list of tickers, or a structured watchlist derived from trade-master notes.

Prefer this flow:

1. Normalize the watchlist into JSON first.
2. Preserve explicit trigger prices from the post when given.
3. Run the script against the JSON file or ticker list.
4. Review failures ticker by ticker instead of silently dropping them.
5. If the user wants a combined image, use the script's split montage pages rather than shrinking too many charts into one export.

Supported inputs:

- `--watchlist-file path/to/watchlist.json`
- `--ticker-file path/to/tickers.txt`
- `--tickers NVDA APP CRWD`

Useful options:

- `--output-dir output/weekly_watchlist_2026-04-27`
- `--lookback 120`
- `--split-pages 3`

The watchlist JSON schema is intentionally simple:

```json
[
  {
    "ticker": "AEIS",
    "setup_label": "High-tight flag at highs",
    "summary": "Precision power supplier tied to semiconductor manufacturing and AI data centers, flagging near highs.",
    "master_note": "$AEIS flagging at highs driven by its critical role in providing precision power for semiconductor manufacturing and AI data centers.",
    "trigger_price": 397.44,
    "trigger_label": "Watch level"
  }
]
```

The script writes:

- `charts/<TICKER>.svg`
- `index.html`
- `run_summary.json`
- optional `watchlist_page_<N>.svg` split montage pages

## RS Glossary

Use [references/rs-glossary.md](references/rs-glossary.md) when a master refers to relative strength. Keep the distinction explicit between:

- `RS line`: a price-relative line such as `stock / benchmark`
- `RS Rating`: a percentile-style or rank-style score derived from longer-term relative performance
- `RS new high before price`: the RS line making a lookback high before price makes its own lookback high
- `buy RS on weakness`: favoring names whose relative performance holds up during controlled pullbacks or weak tape

## Current Trade Masters

Read [references/trade-masters.md](references/trade-masters.md) before adding or updating a master. Start with existing vocabulary and strategy families, then extend carefully.

## Current Examples

Use [references/examples.md](references/examples.md) to ground strategy updates in concrete artifacts. Prefer adding a small number of high-signal examples over many shallow examples.

## Extension Guidance

Keep the core workflow stable while allowing the knowledge base to grow:

- Add new masters to `references/trade-masters.md`
- Add new examples to `references/examples.md`
- Revise `references/signal-schema.md` if the team later needs extra fields
- Add scripts only when repetitive transformation work becomes deterministic enough to automate
- Keep chart-generation logic in `scripts/render_watchlist_candles.py` rather than re-implementing it inline
