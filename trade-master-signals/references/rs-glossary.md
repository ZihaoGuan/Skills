# RS Glossary

Use this file to standardize how the skill interprets relative-strength language in chart posts.

## Chinese Mapping

- `RS`: `相对强弱`
- `RS line`: `相对强弱线`
- `RS Rating`: `相对强弱评分` or `RS 评级`
- `RS new high before price`: `相对强弱线先于股价创新高`
- `Historical RS new highs`: `历史 RS 新高`
- `Historical RS new highs before price`: `历史上 RS 先于股价创新高`
- `buy RS on weakness`: `在回调中买入相对强势股`

## Core Terms

- `RS`: shorthand for `Relative Strength`, not `RSI`
- `RSI`: a separate overbought or oversold oscillator and not the same thing as relative strength
- `Relative Strength Rating` or `RS Rating`: a percentile-style `1-99` score intended to describe how a stock performed over roughly the last twelve months versus the market universe

## RS Line

For this skill, the default interpretation of the `RS line` follows the TradingView-style construction supplied by the user:

```text
RS line = stock price / benchmark price
```

In the provided script:

- the comparison symbol defaults to `SP:SPX`
- the plotted line is the relative-price curve scaled for visual placement on the chart
- the scaling does not change the meaning of the line; it only changes where it is drawn

Practical interpretation:

- rising `RS line` means the stock is outperforming the benchmark
- falling `RS line` means the stock is underperforming the benchmark

## RS Rating

For this skill, `RS Rating` should be interpreted as a rank-style score derived from longer-term performance relative to a benchmark universe, not as the plotted `RS line`.

In the provided script:

- daily stock and `SPX` closes are compared over approximately 63, 126, 189, and 252 trading days
- the most recent quarter gets double weight
- the weighted stock performance is divided by the weighted benchmark performance
- that result is mapped into an approximate `1-99` rating scale
- the script uses `SP:SPX` as the reference index for the rating calculation even if the plotted `RS line` uses another comparison symbol

Practical interpretation:

- higher `RS Rating` means stronger relative performance versus the benchmark or market universe
- lower `RS Rating` means weaker relative performance
- the rating is a universe-ranking proxy, while the plotted `RS line` is a direct price-relative curve

## RS New High Before Price

For this skill, `RS new high before price` means:

- the `RS line` is making a new high over the chosen lookback window
- price has not yet made its own new high over that same lookback window

This is a leadership signal. It suggests the stock is already outperforming before price has fully broken out.

## RS New-High Modes

When a post or screenshot comes from the supplied TradingView indicator, preserve which new-high mode is being used instead of flattening them together:

- `RS New Highs`: current-bar RS-line new high
- `RS New Highs Before Price`: current-bar RS-line new high while price itself has not yet made the matching lookback high
- `Historical RS New Highs`: prior bars where the RS line made a new lookback high
- `Historical RS New Highs Before Price`: prior bars where the RS line led before price over the same lookback window

Interpretation guidance:

- current-bar modes are actionable live leadership signals
- historical modes are evidence-gathering tools used to study how prior leaders behaved before breakout
- `RS new high on the weekly` should be treated as a higher-timeframe leadership clue with more weight than the same phrase on a daily chart
- if the user says to "flip between" these modes, preserve that as part of the analysis workflow rather than as a separate trade trigger

## Buy RS On Weakness

For this skill, `buy RS on weakness` means:

- the stock is pulling back or consolidating
- relative performance versus the benchmark remains strong
- the name is holding up better than the market or peers during weakness

This should be treated as a quality and ranking cue, not as a standalone indicator.

When `buy RS on weakness` is paired with a `30 min pivot`, preserve two layers explicitly:

- the daily or weekly RS behavior explains why the stock deserves attention
- the `30 min pivot` is the execution trigger that defines tight risk inside that broader leadership thesis
