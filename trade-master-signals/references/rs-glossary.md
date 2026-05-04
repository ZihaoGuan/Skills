# RS Glossary

Use this file to standardize how the skill interprets relative-strength language in chart posts.

## Core Terms

- `RS`: shorthand for `Relative Strength`, not `RSI`
- `RSI`: a separate overbought or oversold oscillator and not the same thing as relative strength

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

Practical interpretation:

- higher `RS Rating` means stronger relative performance versus the benchmark or market universe
- lower `RS Rating` means weaker relative performance

## RS New High Before Price

For this skill, `RS new high before price` means:

- the `RS line` is making a new high over the chosen lookback window
- price has not yet made its own new high over that same lookback window

This is a leadership signal. It suggests the stock is already outperforming before price has fully broken out.

## Buy RS On Weakness

For this skill, `buy RS on weakness` means:

- the stock is pulling back or consolidating
- relative performance versus the benchmark remains strong
- the name is holding up better than the market or peers during weakness

This should be treated as a quality and ranking cue, not as a standalone indicator.
