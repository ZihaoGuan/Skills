# Examples

Use this file for grounded examples that justify strategy creation or refinement. Each example should include the original phrasing, the observed chart structure, and the normalized interpretation.

## Example 1: PLAB

Trade master: `Elite Swing Traders`

Original post:

> `$PLAB good one to study. Fake break, squat, breakout.`

Observed context:

- Weekly chart
- Prior resistance is tested and initially does not resolve cleanly
- Pullback remains constructive instead of collapsing
- Price appears to stabilize near support and rising moving averages
- Breakout resumes after the pause

Normalized strategy:

- `fake-break-squat-breakout`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: fake-break-squat-breakout
ticker_example: PLAB
setup_type: continuation breakout
market_bias: bullish
timeframe: weekly

pattern_sequence:
  - prior breakout attempt stalls or briefly fails near resistance
  - pullback holds constructively instead of breaking trend
  - price squats near support or a rising moving average
  - price re-expands through the pivot or range high

trigger_conditions:
  - prior failed breakout or rejection near resistance
  - pullback holds above key support
  - price remains near rising short or intermediate moving averages
  - breakout closes above the recent range high or pivot

confirmation_conditions:
  - tightening price action before breakout
  - improving relative strength
  - volume expansion on breakout

invalidation_conditions:
  - breakdown below the squat low
  - loss of key moving-average support
  - immediate failed breakout back into the range

trade_master_terms:
  - fake break
  - squat
  - breakout

scan_translation:
  scanner_features_needed:
    - moving averages
    - support or pivot detection
    - short-range breakout detection
    - volume comparison
  candidate_rules:
    - existing uptrend or bullish structure
    - recent failed breakout or stalled breakout near resistance
    - orderly pullback holding support
    - fresh breakout above recent range high
  open_questions:
    - which moving averages should the user's scanner prefer
    - how should the scanner define a failed breakout
    - what breakout volume threshold is meaningful in the existing project

example_posts:
  - Elite Swing Traders / PLAB / fake break, squat, breakout

confidence: medium
risk_notes: breakout can fail if the reset loses support before expansion
notes: sequence matters more than any single indicator
```

## Example 2: MSFT

Trade master: `Elite Swing Traders`

Original post:

> `msft Pivot on the monthly chart off the 50. Breaking DTR on the daily and approaching base resistance. Change in character here. -> base breakout`

Observed context:

- Monthly chart shows price reacting from the 50-period moving average
- Daily chart shows recovery from a local low and a break through the daily downtrend line
- Price is improving before the full base breakout, not after it
- The post frames the setup as a developing shift in character that can lead into a base breakout

Normalized strategy:

- `monthly-50-pivot-dtr-base-breakout`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: monthly-50-pivot-dtr-base-breakout
ticker_example: MSFT
setup_type: multi-timeframe base breakout
market_bias: bullish
timeframe: monthly context with daily trigger

pattern_sequence:
  - monthly chart pivots constructively from the 50-period moving average
  - daily chart begins to recover and reclaim structure
  - price breaks the daily downtrend line
  - price approaches base resistance with improving character
  - price breaks out through the top of the base

trigger_conditions:
  - monthly support reaction from the 50-period moving average
  - daily break of the downtrend line or daily trendline resistance
  - price is near but not yet rejected from base resistance

confirmation_conditions:
  - higher low or constructive pivot on the daily chart
  - improving price expansion after the trendline break
  - decisive close through base resistance

invalidation_conditions:
  - failure back below the daily pivot low
  - rejection that preserves the broken downtrend structure as resistance
  - inability to break or hold above base resistance

trade_master_terms:
  - pivot on the monthly chart off the 50
  - DTR
  - base resistance
  - change in character
  - base breakout

scan_translation:
  scanner_features_needed:
    - monthly moving averages
    - daily trendline or downtrend-break proxy
    - base or range-resistance detection
    - multi-timeframe context
  candidate_rules:
    - monthly chart near or reclaiming the 50-period moving average
    - daily chart making a constructive pivot from a recent low
    - daily close above recent downtrend proxy or resistance proxy
    - price within breakout distance of the base high
  open_questions:
    - how the user's scanner approximates a daily downtrend-line break
    - whether monthly moving-average context is available directly
    - how the scanner defines a base and its resistance level

example_posts:
  - Elite Swing Traders / MSFT / pivot on the monthly chart off the 50 ... base breakout

confidence: medium
risk_notes: the setup can fail if the daily character change does not progress into an actual base breakout
notes: this example is explicitly multi-timeframe, with monthly support setting context and daily structure supplying the trigger path
```

## Example 3: HIMS

Trade master: `Elite Swing Traders`

Original post:

> `$HIMS snipe yesterday R/R off the charts`

Observed context:

- Daily chart appears to show a rounded recovery and right-side advance after a prior decline
- Price tightens above rising short-term moving averages before expanding
- The highlighted "yesterday" entry appears to come before the full upside extension is obvious
- The chart suggests the emphasis is on catching the move early with tight risk rather than chasing confirmation late

Normalized strategy:

- `right-side-snipe-into-breakout`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: right-side-snipe-into-breakout
ticker_example: HIMS
setup_type: anticipatory right-side entry
market_bias: bullish
timeframe: daily

pattern_sequence:
  - stock builds a right-side recovery after a prior decline or base repair
  - price tightens near short-term support or a nearby pivot area
  - an early entry is taken before the full breakout becomes obvious
  - price expands quickly, creating asymmetric reward relative to the initial stop

trigger_conditions:
  - constructive right-side advance or repair is already underway
  - price holds above or near rising short-term moving averages
  - entry is taken near a tight pivot, reclaim, or pre-breakout inflection

confirmation_conditions:
  - immediate follow-through after the early entry
  - expansion away from the entry zone with limited adverse movement
  - continued strength toward or through nearby resistance

invalidation_conditions:
  - failure back below the entry pivot or nearby support
  - loss of short-term moving-average support immediately after entry
  - no upside follow-through after the anticipatory entry

trade_master_terms:
  - snipe
  - R/R off the charts

scan_translation:
  scanner_features_needed:
    - short-term moving averages
    - right-side recovery detection
    - tight-range or pivot detection
    - early breakout or pre-breakout context
  candidate_rules:
    - stock recovering on the right side of a base or repair structure
    - price tight relative to short-term support
    - recent reclaim or pivot that offers a nearby invalidation level
    - price still close enough to the inflection point that upside remains asymmetric
  open_questions:
    - how the user's scanner should define a "snipe" entry mechanically
    - whether the project can distinguish pre-breakout entries from confirmed breakouts
    - what distance from support is still considered favorable R/R

example_posts:
  - Elite Swing Traders / HIMS / snipe yesterday R/R off the charts

confidence: low
risk_notes: anticipatory entries lose their edge quickly if price is already extended or if the tight support level fails
notes: this looks more like an entry-quality label than a fully specified chart pattern, so the normalized setup should remain tentative until more examples confirm the same behavior
```

## Example 4: RKLB

Trade master: `Elite Swing Traders`

Original posts:

> `$RKLB clustered MA's starting to cross back over. Need to clear this 75 level resistance to get going. ->`

> `$RKLB with huge move out of the base.`

Observed context:

- Daily chart shows moving averages compressing and beginning to turn back up together
- Price is coiling below a clear horizontal resistance area near 75
- The first post frames the setup as conditional: the stock needs to clear resistance to activate
- The second post confirms the anticipated result, with price expanding strongly once it breaks from the base

Normalized strategy:

- `clustered-ma-cross-into-base-breakout`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: clustered-ma-cross-into-base-breakout
ticker_example: RKLB
setup_type: base breakout after moving-average compression
market_bias: bullish
timeframe: daily

pattern_sequence:
  - short and intermediate moving averages cluster tightly after consolidation
  - the moving averages begin crossing back into bullish alignment
  - price sits just below a clearly defined horizontal resistance level
  - price clears the resistance and breaks out of the base
  - expansion follows quickly once the base resolves

trigger_conditions:
  - clustered short and intermediate moving averages
  - moving averages beginning to cross back over bullishly
  - price close to a known resistance level or base high
  - breakout through that resistance level

confirmation_conditions:
  - decisive close above the resistance level
  - increased expansion or volume on the breakout
  - price separates from the moving-average cluster after clearing the level

invalidation_conditions:
  - failure to clear resistance after the moving-average compression
  - rejection back into the base immediately after breakout
  - bearish re-separation of the moving averages

trade_master_terms:
  - clustered MA's
  - starting to cross back over
  - clear this 75 level resistance
  - huge move out of the base

scan_translation:
  scanner_features_needed:
    - multiple moving averages
    - moving-average compression or proximity detection
    - moving-average cross detection
    - horizontal resistance or base-high detection
    - breakout confirmation
  candidate_rules:
    - short and intermediate moving averages tightly clustered
    - recent bullish crossover or reordering of those moving averages
    - price within breakout distance of a well-defined resistance level
    - fresh close above the base high or resistance level
  open_questions:
    - which moving averages the user's project should treat as the cluster set
    - how tightly grouped the moving averages must be to count as clustered
    - what breakout strength filter the scanner should require after the level clears

example_posts:
  - Elite Swing Traders / RKLB / clustered MA's starting to cross back over...
  - Elite Swing Traders / RKLB / huge move out of the base

confidence: medium
risk_notes: moving-average compression loses value if the resistance level is not actually cleared or if the breakout immediately reverses
notes: this is a useful linked example because the first post identifies the pre-breakout condition and the second confirms the intended outcome
```

## Example 5: NFLX

Trade master: `Elite Swing Traders`

Original post:

> `NFLX just another example of buying gap support pivots. They offer up some of the best R/R entry.`

Observed context:

- Daily chart shows a prior upside gap that appears to establish an important support reference
- Price pulls back or consolidates into that support zone instead of losing it
- The highlighted pivots appear to occur as price stabilizes and turns back up from the gap-support area
- The post emphasizes the quality of the entry because the support level is nearby and the invalidation appears tight

Normalized strategy:

- `gap-support-pivot-entry`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: gap-support-pivot-entry
ticker_example: NFLX
setup_type: support-pivot entry
market_bias: bullish
timeframe: daily

pattern_sequence:
  - stock gaps up and leaves behind a meaningful support shelf
  - price later revisits or tightens around that gap-support zone
  - price pivots constructively from the support instead of breaking down
  - the entry is taken near the pivot while risk remains tightly defined
  - upside develops as price re-accelerates away from the support area

trigger_conditions:
  - identifiable prior gap creating a visible support zone
  - price holding or reclaiming that support zone
  - constructive pivot from the gap-support area
  - entry still close enough to support that the stop remains tight

confirmation_conditions:
  - higher low, reclaim, or bullish pivot candle at support
  - immediate separation from the support zone after entry
  - continued strength toward nearby resistance or trend continuation

invalidation_conditions:
  - loss of the gap-support zone
  - failed pivot that closes back below support
  - weak bounce that cannot separate from the support area

trade_master_terms:
  - buying gap support pivots
  - best R/R entry

scan_translation:
  scanner_features_needed:
    - gap detection
    - support-zone persistence
    - pivot or reclaim detection
    - distance-from-support measurement
  candidate_rules:
    - prior bullish gap that remains relevant on the chart
    - price revisiting or consolidating near the lower edge of the gap-support zone
    - constructive pivot or reclaim from that support area
    - entry still within a favorable distance of invalidation
  open_questions:
    - how the user's scanner identifies and stores prior gap-support levels
    - how long a gap remains valid as support in the project
    - what maximum distance from support still qualifies as elite R/R

example_posts:
  - Elite Swing Traders / NFLX / buying gap support pivots

confidence: medium
risk_notes: the setup loses its edge quickly if price is no longer close to the gap-support zone or if support fails on the retest
notes: this post explicitly labels the pattern as a recurring setup, so it should be treated as a true strategy family instead of a one-off chart comment
```

## Example 6: VRT

Trade master: `Elite Swing Traders`

Original post:

> `$VRT good chart to study. Buying earnings gap ups when they pullback to gap support is one of my favorite trades. Hard to find better risk to reward. Know the levels and trade them accordingly.`

Observed context:

- Daily chart shows a prior earnings-driven gap up that establishes a clear support zone
- Price later pulls back into that gap-support area instead of fully losing the post-gap structure
- The annotations highlight both fake breakout behavior and the eventual constructive pivot from gap support
- The post stresses that the edge comes from knowing the exact levels and trading against them rather than taking a loose discretionary bounce

Normalized strategy:

- `gap-support-pivot-entry`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: gap-support-pivot-entry
ticker_example: VRT
setup_type: earnings gap-support pivot entry
market_bias: bullish
timeframe: daily

pattern_sequence:
  - stock gaps up on earnings and leaves behind a meaningful support shelf
  - price later pulls back toward the gap-support zone
  - weak hands may get shaken out through fake breakout or shakeout behavior
  - price pivots constructively from the gap-support area instead of losing it
  - upside resumes once price reclaims strength from the support pivot

trigger_conditions:
  - identifiable earnings gap creating a visible support zone
  - pullback into or near that gap-support area
  - constructive pivot or reclaim from the support zone
  - entry still taken close enough to the support level that risk remains tight

confirmation_conditions:
  - clear defense of the gap-support level
  - higher low, reclaim, or bullish pivot candle from support
  - immediate separation from support or continuation toward breakout territory

invalidation_conditions:
  - loss of the earnings gap-support zone
  - failed pivot that cannot hold above support after the attempted turn
  - entry taken too far from support to preserve asymmetric R/R

trade_master_terms:
  - buying earnings gap ups when they pullback to gap support
  - hard to find better risk to reward
  - know the levels and trade them accordingly

scan_translation:
  scanner_features_needed:
    - earnings gap detection
    - gap-support zone persistence
    - pivot or reclaim detection
    - distance-from-support measurement
    - optional fake-break or shakeout context
  candidate_rules:
    - prior earnings gap up that remains structurally relevant
    - price revisiting or undercutting the edge of the gap-support zone without fully failing
    - constructive pivot or reclaim from that support area
    - entry still near enough to the level that invalidation remains tight
  open_questions:
    - how the user's scanner distinguishes earnings gaps from ordinary gaps
    - whether the project can store precise support bands rather than a single point
    - what tolerance around the gap-support level should still count as tradable

example_posts:
  - Elite Swing Traders / VRT / buying earnings gap ups when they pullback to gap support

confidence: medium
risk_notes: this setup loses quality fast if the entry is no longer close to the earnings gap-support level or if the support shelf is decisively lost
notes: this reinforces `gap-support-pivot-entry` as a real recurring family and sharpens it by making earnings gaps and exact level awareness explicit
```

## Example 7: APEI

Trade master: `Elite Swing Traders`

Original post:

> `$APEI Trades a little thin but has a low 17mil float and a beautiful earnings flag tight as a drum.`

Observed context:

- Daily chart shows a strong earnings-driven impulse move followed by a very tight sideways consolidation near the highs
- Price appears to hold above rising short-term moving averages while volatility contracts
- The post frames the setup as a continuation pattern rather than a pullback-to-support reversal
- Float and thin trading are mentioned as contextual traits, not as the actual trigger

Normalized strategy:

- `earnings-flag-tight-continuation`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: earnings-flag-tight-continuation
ticker_example: APEI
setup_type: post-earnings continuation flag
market_bias: bullish
timeframe: daily

pattern_sequence:
  - stock expands sharply on an earnings-related move
  - price does not meaningfully give back the impulse
  - a tight flag or shelf forms near the highs
  - volatility contracts while price holds constructive support
  - continuation becomes possible once the tight range resolves upward

trigger_conditions:
  - identifiable earnings impulse or earnings gap-up move
  - tight consolidation near the highs after the impulse
  - price holds above key short-term support or rising moving averages
  - range remains compressed enough to qualify as a flag rather than a loose base

confirmation_conditions:
  - upside resolution from the tight flag
  - continued closes near the top of the range before breakout
  - expansion in price or volume once the flag resolves

invalidation_conditions:
  - loose or sloppy consolidation that breaks the tight-flag character
  - decisive loss of short-term support during the flag
  - breakdown below the lower edge of the earnings flag

trade_master_terms:
  - trades a little thin
  - low 17mil float
  - earnings flag
  - tight as a drum

scan_translation:
  scanner_features_needed:
    - earnings move detection
    - flag or tight-range detection
    - short-term moving-average support
    - float or liquidity filters
  candidate_rules:
    - recent earnings-driven expansion
    - tight post-earnings consolidation near the highs
    - range compression above short-term support
    - optional low-float or minimum-liquidity constraints
  open_questions:
    - how the user's scanner should define an earnings flag mechanically
    - whether the project can measure tightness or range contraction after earnings
    - how thin is too thin for the user's actual execution preferences

example_posts:
  - Elite Swing Traders / APEI / beautiful earnings flag tight as a drum

confidence: medium
risk_notes: thin trading and low float can improve upside expansion, but they can also worsen fills and increase failure volatility if the flag breaks down
notes: this looks like a distinct post-earnings continuation family, with liquidity commentary acting as a secondary filter rather than the core setup
```

## Example 8: SNDK

Trade master: `Elite Swing Traders`

Original post:

> `$SNDK first pullback after the new ATH, Tested the 50ema put in an inside day, Fake break "squat" breakout. Buy RS on weakness, Had all the ingredients I look for. Gave an incredible opportunity. Study it if you missed it.`

Observed context:

- Daily chart shows a strong uptrend that has already broken to new all-time highs
- The setup appears on the first meaningful pullback after that breakout, not deep into a mature downtrend
- Price tests the 50 EMA, compresses with an inside day, and then resolves higher
- The post explicitly ties the chart to the `fake break` / `squat` / `breakout` language while adding a more precise checklist around relative strength and pullback quality

Normalized strategy:

- `fake-break-squat-breakout`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: fake-break-squat-breakout
ticker_example: SNDK
setup_type: continuation breakout after first pullback
market_bias: bullish
timeframe: daily

pattern_sequence:
  - stock makes a new all-time high
  - the first constructive pullback develops after the breakout
  - price tests the 50 EMA without materially damaging trend structure
  - an inside day or tight contraction forms during the pullback
  - the pullback behaves like a fake break or squat rather than a true failure
  - price resolves higher into breakout continuation

trigger_conditions:
  - first pullback after a new all-time high
  - successful test of the 50 EMA or equivalent trend support
  - inside day or similar tight contraction near support
  - relative strength remains firm despite the pullback
  - breakout through the tight pullback structure

confirmation_conditions:
  - price quickly reclaims strength after the fake break or squat
  - inside-day resolution occurs to the upside
  - relative strength line stays constructive through the pullback

invalidation_conditions:
  - loss of the 50 EMA without immediate recovery
  - inside day breaks lower and follow-through confirms weakness
  - pullback becomes too deep or too loose to qualify as a controlled first pullback

trade_master_terms:
  - first pullback after the new ATH
  - tested the 50ema
  - inside day
  - fake break
  - squat
  - breakout
  - buy RS on weakness
  - had all the ingredients I look for

scan_translation:
  scanner_features_needed:
    - all-time-high or recent breakout detection
    - first-pullback logic
    - 50 EMA support test
    - inside-day detection
    - relative-strength filter
  candidate_rules:
    - stock recently made a new high or breakout
    - current pullback is the first meaningful retracement after that breakout
    - price testing and holding the 50 EMA
    - inside day or tight contraction during the pullback
    - relative strength remaining strong during price weakness
  open_questions:
    - how the user's scanner should define "first pullback" mechanically
    - whether the project has a built-in relative-strength metric or proxy
    - how tight the inside-day or contraction requirement should be

example_posts:
  - Elite Swing Traders / SNDK / first pullback after the new ATH ... fake break squat breakout

confidence: high
risk_notes: the setup loses quality if the first pullback turns into a deeper trend break or if the 50 EMA test fails decisively
notes: this is a canonical checklist-style example for `fake-break-squat-breakout` because it explicitly names the pattern and the supporting ingredients the master wants present
```

## Example 8B: SNDK

Trade master: `Elite Swing Traders`

Original post:

> `$SNDK Fake break, squat and now setting up for the real move? This is a perfect example playing out so far.`

Observed context:

- Daily chart labels a failed breakout near resistance, followed by a `squat to flush out support`
- Price appears to recover from the flush area and re-approach resistance rather than breaking trend
- The post frames the setup as still developing, with the expected "real move" potentially still ahead
- The master explicitly calls this a perfect example, which makes it a strong reference chart for the family

Normalized strategy:

- `fake-break-squat-breakout`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: fake-break-squat-breakout
ticker_example: SNDK
setup_type: continuation breakout after support flush
market_bias: bullish
timeframe: daily

pattern_sequence:
  - price attempts a breakout and produces a fake break near resistance
  - the setup squats by flushing out support and weak holders
  - price stabilizes and reclaims constructive posture after the flush
  - the chart sets up for the real move through resistance

trigger_conditions:
  - failed breakout or fake break near a clear resistance area
  - squat or support flush that does not destroy the broader structure
  - constructive recovery from the flush zone
  - renewed pressure back into resistance with the breakout still ahead

confirmation_conditions:
  - support flush is quickly absorbed rather than extended
  - price reclaims short-term control after the squat
  - breakout through resistance follows the reset

invalidation_conditions:
  - flush continues into true breakdown rather than a controlled squat
  - failure to recover after the support flush
  - repeated rejection at resistance without renewed strength

trade_master_terms:
  - fake break
  - squat
  - squat to flush out support
  - real move
  - perfect example

scan_translation:
  scanner_features_needed:
    - failed-breakout detection
    - support-flush or shakeout proxy
    - recovery-after-flush logic
    - resistance retest or breakout detection
  candidate_rules:
    - recent failed breakout near resistance
    - brief downside flush that holds broader structure
    - constructive rebound from the flush zone
    - price pressing back toward resistance for the real move
  open_questions:
    - how the user's scanner should proxy a support flush mechanically
    - how much downside excursion still counts as a squat instead of a breakdown
    - whether pre-breakout setups like this should rank separately from already-triggered breakouts

example_posts:
  - Elite Swing Traders / SNDK / fake break squat and setting up for the real move

confidence: high
risk_notes: the setup fails if the squat is not absorbed and the support flush becomes a real breakdown instead of a reset
notes: this is a textbook reinforcement of `fake-break-squat-breakout` because the chart itself labels the fake break, the support flush, and the anticipated real move
```

## Example 9: QQQ and SPY

Trade master: `Elite Swing Traders`

Original post:

> `$QQQ & $SPY up on well above average volume yesterday. SPY highest up day volume since last April reversal. Both gapping up this morning.`

Observed context:

- The post is about major index ETFs rather than a single tradeable stock setup
- Both QQQ and SPY show strong upside volume, suggesting broad institutional participation
- The message emphasizes that the strength is not isolated to one index and is continuing with next-morning gap follow-through
- The post appears intended to frame the overall tape as supportive rather than to define a precise entry pattern in QQQ or SPY alone

Normalized strategy:

- `index-accumulation-gap-follow-through`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: index-accumulation-gap-follow-through
ticker_example: QQQ, SPY
setup_type: market-context accumulation signal
market_bias: bullish
timeframe: daily with next-session follow-through

pattern_sequence:
  - major indices post strong upside days
  - volume is materially above average on the up move
  - one or more indices show historically notable upside participation
  - the next session opens with upside gaps, confirming follow-through
  - the broader market environment becomes more supportive for long setups

trigger_conditions:
  - QQQ and SPY both show upside price expansion
  - up-day volume is well above average
  - at least one index shows unusually strong upside participation relative to recent history
  - next-session gap-up follow-through is present

confirmation_conditions:
  - strength is broad across both major indices rather than isolated
  - follow-through continues after the opening gap
  - individual leaders begin responding positively in the same environment

invalidation_conditions:
  - next-session gap fails immediately and reverses the signal
  - strong volume is driven by one-off event noise without sustained breadth
  - broad market rolls back over and fails to hold the reversal effort

trade_master_terms:
  - QQQ & SPY
  - up on well above average volume
  - highest up day volume since last April reversal
  - both gapping up this morning

scan_translation:
  scanner_features_needed:
    - index ETF monitoring
    - average-volume comparison
    - historical volume ranking or reference-point comparison
    - next-session gap detection
    - optional market regime flagging for downstream stock scans
  candidate_rules:
    - QQQ and SPY both close up on above-average volume
    - one or both print a top-tier upside-volume day versus recent history
    - next session opens above the prior close
    - mark market regime as supportive for bullish setups
  open_questions:
    - how the user's scanner or project stores market regime context
    - what lookback should define "well above average" volume
    - whether this context should filter stock scans or only influence ranking

example_posts:
  - Elite Swing Traders / QQQ & SPY / up on well above average volume and gapping up

confidence: medium
risk_notes: strong index accumulation signals can improve the odds for long setups, but the edge weakens quickly if the follow-through gap reverses or breadth narrows
notes: this is a market-context family, not a single-stock entry pattern, and should likely be used as a regime filter for other setups
```

## Example 10: QQQ

Trade master: `Elite Swing Traders`

Original post:

> `$QQQ heading back for support. Every rally into declining MA's continues to be sold.`

Observed context:

- The post is about QQQ as a market proxy rather than a single-stock entry
- Price appears to be rallying weakly into downward-sloping moving averages and failing there
- The message emphasizes persistent supply on rebounds, not one isolated rejection
- The expected path is a move back toward support rather than immediate trend repair

Normalized strategy:

- `index-rally-into-declining-ma-selloff`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: index-rally-into-declining-ma-selloff
ticker_example: QQQ
setup_type: bearish market-context rejection
market_bias: bearish
timeframe: daily

pattern_sequence:
  - index is in a corrective or weak-tape phase
  - rallies attempt to lift price back into declining moving averages
  - those rallies fail as sellers defend the falling averages
  - price rotates lower again toward known support
  - weak market context persists until the rejection pattern changes

trigger_conditions:
  - QQQ or comparable index ETF trading below declining short or intermediate moving averages
  - repeated rejection on rallies into those moving averages
  - support level below current price acting as the likely magnet

confirmation_conditions:
  - multiple failed rebound attempts into declining MAs
  - continued lower highs during the corrective phase
  - downside follow-through toward support after the rejection

invalidation_conditions:
  - decisive reclaim of the declining moving averages
  - rally that holds above the moving averages instead of being sold
  - support test that reverses the weak-tape character with breadth confirmation

trade_master_terms:
  - heading back for support
  - every rally into declining MA's continues to be sold
  - declining MA's

scan_translation:
  scanner_features_needed:
    - index ETF monitoring
    - moving-average slope detection
    - moving-average rejection logic
    - support-level detection
    - optional bearish market regime flagging for downstream scans
  candidate_rules:
    - QQQ below declining short or intermediate moving averages
    - recent rally attempts failing near those moving averages
    - price positioned above a nearby support level with downside room toward it
    - mark market regime as cautious or bearish for long setups
  open_questions:
    - which moving averages the user's project should use for regime assessment
    - how many failed rallies should be required before flipping market context bearish
    - whether this signal should suppress long setups entirely or only lower their rank

example_posts:
  - Elite Swing Traders / QQQ / heading back for support and rallies into declining MAs sold

confidence: medium
risk_notes: bearish tape context can ease quickly if indices reclaim the declining moving averages, so the regime signal should be refreshed frequently rather than assumed to persist
notes: this is the bearish counterpart to the accumulation-style index context and should be used as a weak-tape filter for downstream stock selection
```

## Example 11: PL

Trade master: `Elite Swing Traders`

Original post:

> `$PL Buying earnings gappers when they pullback to gap support/ 8ema is a great risk to reward entry.`

Observed context:

- Daily chart shows an earnings-driven gap move followed by a controlled pullback rather than a full gap failure
- The pullback appears to hold in the area where horizontal gap support and the rising 8 EMA converge
- The post frames the edge as the combination of two support references, not just a generic bounce
- The emphasis is again on favorable risk/reward because the entry can be taken close to clearly defined support

Normalized strategy:

- `gap-support-pivot-entry`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: gap-support-pivot-entry
ticker_example: PL
setup_type: earnings gap-support plus 8 EMA entry
market_bias: bullish
timeframe: daily

pattern_sequence:
  - stock gaps up on earnings and establishes a meaningful support shelf
  - price later pulls back in an orderly way rather than collapsing
  - the pullback meets the combined support of the gap area and the rising 8 EMA
  - price stabilizes and pivots from that overlapping support zone
  - continuation resumes with favorable risk/reward because invalidation remains nearby

trigger_conditions:
  - identifiable earnings gap creating a visible support zone
  - pullback into or near the gap-support area
  - rising 8 EMA overlapping or closely supporting the same zone
  - constructive pivot or reclaim from that combined support area

confirmation_conditions:
  - price respects both the gap-support area and the 8 EMA
  - bullish pivot or reclaim candle from the overlap zone
  - immediate separation higher after testing the support cluster

invalidation_conditions:
  - decisive loss of the gap-support area
  - failure to hold the 8 EMA during the pullback
  - weak bounce that cannot separate from the combined support zone

trade_master_terms:
  - buying earnings gappers
  - pullback to gap support
  - 8ema
  - great risk to reward entry

scan_translation:
  scanner_features_needed:
    - earnings gap detection
    - gap-support zone persistence
    - 8 EMA support test
    - overlap or confluence detection between horizontal and dynamic support
    - pivot or reclaim detection
  candidate_rules:
    - prior earnings gap up remains structurally relevant
    - price revisits the gap-support zone while the 8 EMA rises into the same area
    - constructive pivot or reclaim from that confluence zone
    - entry still close enough to invalidation to preserve asymmetric R/R
  open_questions:
    - how the user's scanner should detect support overlap between the gap zone and the 8 EMA
    - what tolerance around the 8 EMA and gap-support band should count as confluence
    - whether this confluence should rank higher than gap support alone

example_posts:
  - Elite Swing Traders / PL / buying earnings gappers when they pullback to gap support / 8ema

confidence: medium
risk_notes: the setup loses its advantage quickly if price decisively loses either the earnings-gap support or the 8 EMA, because the overlapping support thesis breaks down
notes: this reinforces `gap-support-pivot-entry` and sharpens it by showing that the master often prefers confluence between horizontal gap support and fast dynamic support
```

## Example 12: QQQ

Trade master: `Elite Swing Traders`

Original post:

> `$QQQ EMA crossover on the weekly and rolling over. Careful out there.`

Observed context:

- The post is about QQQ as a broad market proxy rather than a single tradeable stock pattern
- The signal is explicitly weekly, making it a higher-timeframe regime warning rather than short-term tape commentary
- The master is pointing to an EMA crossover plus rollover behavior, implying deterioration in trend structure
- The tone is cautionary and appears intended to warn against aggressive long exposure in a weakening environment

Normalized strategy:

- `weekly-ema-crossover-rollover`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: weekly-ema-crossover-rollover
ticker_example: QQQ
setup_type: higher-timeframe bearish market-context signal
market_bias: bearish
timeframe: weekly

pattern_sequence:
  - major index weakens after an extended advance
  - weekly EMA relationship crosses into a bearish configuration
  - price begins rolling over rather than stabilizing
  - higher-timeframe caution increases for long exposure
  - weak regime context persists until the weekly structure improves

trigger_conditions:
  - QQQ or comparable index ETF showing a bearish weekly EMA crossover
  - weekly price action rolling over after the crossover
  - market context no longer supporting aggressive bullish positioning

confirmation_conditions:
  - continued weekly weakness after the crossover
  - inability to reclaim the faster weekly EMA or crossover zone
  - lower highs or failed rebounds on the weekly chart

invalidation_conditions:
  - bullish reclaim of the weekly EMA structure
  - crossover reverses back in favor of the bulls
  - weekly price action stabilizes and invalidates the rollover thesis

trade_master_terms:
  - EMA crossover
  - on the weekly
  - rolling over
  - careful out there

scan_translation:
  scanner_features_needed:
    - weekly moving-average calculations
    - moving-average crossover detection
    - weekly trend-state tracking
    - optional market regime flagging for downstream scans
  candidate_rules:
    - QQQ weekly fast EMA crossing below or weakening relative to the slower EMA
    - weekly price action deteriorating after the crossover
    - mark market regime as cautious or bearish with higher-timeframe weight
  open_questions:
    - which exact weekly EMAs the user's project should use for this regime signal
    - how the scanner should combine weekly bearish context with daily bullish setups
    - whether weekly regime warnings should hard-filter long scans or only down-rank them

example_posts:
  - Elite Swing Traders / QQQ / EMA crossover on the weekly and rolling over

confidence: medium
risk_notes: higher-timeframe bearish signals can stay relevant longer than daily tape warnings, but they can also reverse if the weekly crossover quickly recovers, so the regime state should be refreshed on each weekly close
notes: this is a higher-timeframe bearish regime family and should likely carry more durable weight than daily weak-tape commentary when the scanner combines context layers
```

## Example 13: DJI

Trade master: `Elite Swing Traders`

Original post:

> `$DJI lost the 200sma and MA's are running downhill after the EMA crossover.`

Observed context:

- The post is about the Dow Jones Industrial Average as a market proxy rather than a single-stock entry
- Price has lost the 200-day simple moving average, which turns a key longer-term support reference into evidence of deterioration
- The moving averages are sloping lower together, suggesting the weakness is not isolated to one bar
- The warning is explicitly tied to a prior EMA crossover, implying that the bearish regime has already been weakening before the 200 SMA loss

Normalized strategy:

- `index-200sma-loss-post-crossover`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: index-200sma-loss-post-crossover
ticker_example: DJI
setup_type: structural bearish market-context breakdown
market_bias: bearish
timeframe: daily

pattern_sequence:
  - index weakens after a bearish EMA crossover
  - moving averages begin sloping lower together
  - price loses the 200-day simple moving average
  - longer-term support is no longer holding the tape
  - bearish market context strengthens until the structure improves

trigger_conditions:
  - bearish EMA crossover already in place
  - daily price breaking below the 200 SMA
  - moving averages trending lower rather than flattening or recovering

confirmation_conditions:
  - continued closes below the 200 SMA
  - moving-average slopes remain negative
  - rebound attempts fail to quickly reclaim the 200 SMA

invalidation_conditions:
  - decisive reclaim of the 200 SMA
  - moving averages flatten or turn back up
  - EMA crossover deterioration reverses instead of deepening

trade_master_terms:
  - lost the 200sma
  - MA's are running downhill
  - after the EMA crossover

scan_translation:
  scanner_features_needed:
    - index monitoring
    - 200 SMA detection
    - moving-average slope detection
    - EMA crossover state tracking
    - optional bearish market regime flagging for downstream scans
  candidate_rules:
    - major index below its 200 SMA
    - bearish EMA crossover already active
    - key moving averages sloping lower together
    - mark market regime as structurally bearish for long setups
  open_questions:
    - which moving averages the user's project should include in the downhill-slope test
    - how long the index must remain below the 200 SMA before the regime flag is considered active
    - whether this context should fully suppress longs or only reduce ranking and size

example_posts:
  - Elite Swing Traders / DJI / lost the 200sma and MA's are running downhill after the EMA crossover

confidence: medium
risk_notes: structural bearish context can persist longer than short-term tape warnings, but it can also reverse quickly if the index reclaims the 200 SMA and the moving-average slopes stabilize
notes: this is a daily structural bearish regime family and should likely carry more weight than a simple failed-rally warning because it combines crossover weakness with the loss of a major long-term average
```

## Example 14: QQQ

Trade master: `Elite Swing Traders`

Original post:

> `$QQQ Bear flag testing support again. The more times we test the level the more likely it will fail. Every rally into declining MA's is being sold. Gapping down near the 200sma this morning. Conditions are deteriorating rapidly. Careful out there.`

Observed context:

- The post is about QQQ as a market proxy rather than a single-stock setup
- The core weak-tape feature remains repeated failed rallies into declining moving averages
- The bearish case is sharper here because price is also forming a bear flag and repeatedly testing support
- The market is gapping down near the 200 SMA, which increases pressure on an already weakened support zone

Normalized strategy:

- `index-rally-into-declining-ma-selloff`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: index-rally-into-declining-ma-selloff
ticker_example: QQQ
setup_type: bearish market-context rejection with support pressure
market_bias: bearish
timeframe: daily

pattern_sequence:
  - index is in a weak-tape phase with declining moving averages overhead
  - countertrend rallies continue to fail into those moving averages
  - price forms a bear-flag style consolidation rather than true repair
  - support is tested repeatedly, weakening the level
  - downside pressure increases further as price gaps down near major support such as the 200 SMA

trigger_conditions:
  - QQQ or comparable index ETF trading below declining short or intermediate moving averages
  - repeated rejection on rallies into those moving averages
  - support level tested multiple times without durable recovery
  - downside pressure building near the 200 SMA or comparable long-term support

confirmation_conditions:
  - bear-flag structure resolves lower or fails to improve
  - repeated support tests continue to weaken the level
  - gap-down or downside follow-through appears as support pressure increases

invalidation_conditions:
  - decisive reclaim of the declining moving averages
  - support holds and produces a real change in character instead of another failed rally
  - bear-flag structure breaks upward and invalidates the weak-tape thesis

trade_master_terms:
  - bear flag
  - the more times we test the level the more likely it will fail
  - every rally into declining MA's is being sold
  - gapping down near the 200sma
  - conditions are deteriorating rapidly
  - careful out there

scan_translation:
  scanner_features_needed:
    - index ETF monitoring
    - moving-average slope detection
    - moving-average rejection logic
    - repeated support-test detection
    - 200 SMA proximity or support-pressure detection
    - optional bearish market regime flagging for downstream scans
  candidate_rules:
    - QQQ below declining short or intermediate moving averages
    - repeated rally failures into those moving averages
    - support tested multiple times in a short window
    - price near or pressing into the 200 SMA with downside pressure increasing
    - mark market regime as weakening or bearish for long setups
  open_questions:
    - how the user's project should count repeated tests of support
    - whether bear-flag detection is available directly or needs a proxy
    - how close to the 200 SMA the scanner should consider "pressure on major support"

example_posts:
  - Elite Swing Traders / QQQ / bear flag testing support again and rallies into declining MAs sold

confidence: medium
risk_notes: weak-tape conditions can snowball quickly once repeatedly tested support fails, but this context can still improve if the index reclaims moving averages and support stabilizes instead of breaking
notes: this reinforces `index-rally-into-declining-ma-selloff` and sharpens it by adding bear-flag structure, repeated support tests, and pre-breakdown pressure near the 200 SMA
```

## Example 15: DELL

Trade master: `Elite Swing Traders`

Original post:

> `Buying earnings gap support is one of the best R/R entry tactics you will come across.`

Observed context:

- Daily chart shows a large earnings-driven gap that leaves behind a clearly defined support shelf
- Price later interacts with that support zone without fully failing the post-earnings structure
- The entry thesis depends on the support shelf remaining intact, which keeps invalidation nearby
- The wording is broader than a one-off chart comment and reads like a general principle illustrated by the chart

Normalized strategy:

- `gap-support-pivot-entry`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: gap-support-pivot-entry
ticker_example: DELL
setup_type: earnings gap-support entry
market_bias: bullish
timeframe: daily

pattern_sequence:
  - stock gaps strongly on earnings and creates a meaningful support shelf
  - price later pulls back toward that earnings-gap support
  - the support area continues to hold rather than fully failing
  - entry is taken close to the support zone while invalidation remains nearby
  - upside resumes with asymmetric reward if the support pivot works

trigger_conditions:
  - identifiable earnings gap creating a visible support zone
  - pullback into or near that support shelf
  - support remains intact enough to allow a defined-risk entry
  - constructive pivot or stabilization from the earnings-gap support area

confirmation_conditions:
  - clear defense of the earnings-gap support
  - bullish pivot or reclaim from the support shelf
  - separation away from support after the test

invalidation_conditions:
  - decisive loss of the earnings-gap support
  - failure to stabilize after touching the support zone
  - entry taken too far from support to preserve strong asymmetry

trade_master_terms:
  - buying earnings gap support
  - best R/R entry tactics

scan_translation:
  scanner_features_needed:
    - earnings gap detection
    - support-zone persistence
    - pivot or stabilization detection near support
    - distance-from-support measurement
  candidate_rules:
    - prior earnings gap up remains structurally relevant
    - price revisits the earnings-gap support shelf
    - support holds well enough to allow a nearby invalidation level
    - constructive pivot or reclaim occurs from that zone
  open_questions:
    - how the user's scanner should define an earnings-gap support shelf
    - how long the gap-support level remains valid after the earnings event
    - whether this family should receive higher rank than other bullish entries because of the master's stated conviction

example_posts:
  - Elite Swing Traders / DELL / buying earnings gap support is one of the best R/R entry tactics

confidence: medium
risk_notes: the edge comes from proximity to a clean support shelf, so it degrades quickly if price is no longer close to the gap support or if the level has already been damaged
notes: this reinforces `gap-support-pivot-entry` as a top-conviction family for this master and makes the conviction statement explicit, not just the chart pattern
```

## Example 16: FSLY

Trade master: `Elite Swing Traders`

Original post:

> `$FSLY RS new high before price. I'm still long from 17.09 but I had to trim it back at 49% gain as it was getting pretty extended at over 12 ATR% Multiple from the 50.`

Observed context:

- Daily chart shows strong relative-strength behavior, with the RS line leading price by making a new high first
- The post is partly diagnostic and partly managerial: the stock is still a leader, but no longer in the best risk/reward zone for a full-sized hold
- The master remains constructive enough to stay long, which implies the trend is intact
- The trim decision is tied to extension from the 50-period moving average using an ATR-based metric rather than a breakdown signal

Normalized strategy:

- `rs-leads-price-extension-trim`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: rs-leads-price-extension-trim
ticker_example: FSLY
setup_type: leadership confirmation with extension management
market_bias: bullish but extended
timeframe: daily

pattern_sequence:
  - stock establishes leadership and the relative-strength line makes a new high before price
  - price continues trending higher with the thesis still intact
  - extension from the 50-period moving average grows unusually large
  - position management shifts from full-size hold to trimming because the stock is stretched

trigger_conditions:
  - RS line making a new high before price fully confirms
  - stock still in a constructive trend
  - ATR-based extension from the 50-period moving average reaching an unusually high multiple

confirmation_conditions:
  - relative-strength leadership persists even as price becomes extended
  - price remains above key trend support despite the trim decision
  - trimming is driven by extension rather than by outright technical failure

invalidation_conditions:
  - RS leadership breaks down instead of leading
  - price loses the 50-period moving average in a meaningful way
  - extension cools off through damage rather than orderly digestion

trade_master_terms:
  - RS new high before price
  - trim it back
  - pretty extended
  - ATR% Multiple from the 50

scan_translation:
  scanner_features_needed:
    - relative-strength line or proxy
    - relative-strength new-high detection
    - 50-period moving-average distance measurement
    - ATR-based extension calculation
    - optional position-management flagging rather than fresh-entry ranking
  candidate_rules:
    - RS line or proxy making a new high before price
    - stock trending constructively above the 50-period moving average
    - price extension from the 50-period moving average exceeding a high ATR-based threshold
    - mark as leader but extended rather than ideal new entry
  open_questions:
    - whether the user's project has a true RS line or only a proxy metric
    - how ATR% Multiple from the 50 should be defined in the existing codebase
    - what extension threshold should trigger a trim-style warning instead of a buy ranking

example_posts:
  - Elite Swing Traders / FSLY / RS new high before price and trim because extended

confidence: medium
risk_notes: strong leaders can stay extended longer than expected, so trimming on extension should be treated as management guidance rather than a blanket exit signal
notes: this is more about leadership quality and extension management than entry timing, and it should likely inform ranking and position-sizing logic rather than create a standalone buy trigger
```

## Example 17: QQQ

Trade master: `Elite Swing Traders`

Original posts:

> `With current conditions I'm not leaning one way or the other but I am certainly cautious. No reason to try and force anything. Better times always come so preserve your mental capital so that you're fresh and ready to go when conditions improve.`

> `$QQQ seems testing the 200sma (590) is inevitable at this point.`

> `$QQQ Printed a weekly gravestone doji.`

Observed context:

- The first statement is not a setup call at all; it is master-level posture guidance about participation and caution
- The daily QQQ note suggests downside pressure is strong enough that a test of the 200 SMA is becoming the most likely near-term path
- The weekly QQQ note adds a higher-timeframe reversal-style warning via the gravestone doji
- Taken together, the batch reinforces a cautious market-regime stance rather than a fresh directional trade setup

Normalized strategy:

- `weekly-ema-crossover-rollover`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: weekly-ema-crossover-rollover
ticker_example: QQQ
setup_type: higher-timeframe bearish market-context warning with caution overlay
market_bias: cautious to bearish
timeframe: weekly context with daily pressure into the 200 SMA

pattern_sequence:
  - market conditions deteriorate enough that the master explicitly shifts into a cautious participation stance
  - daily QQQ action weakens toward a likely test of the 200 SMA
  - weekly structure adds reversal-style evidence through a gravestone doji
  - the combined message is to avoid forcing exposure until conditions improve

trigger_conditions:
  - major index showing persistent daily weakness toward long-term support such as the 200 SMA
  - weekly chart printing a reversal-style warning candle or otherwise failing to improve
  - master-level posture shifting from opportunity-seeking to caution and capital preservation

confirmation_conditions:
  - daily price continues pressing toward the 200 SMA instead of reclaiming strength
  - weekly weakness remains unresolved after the gravestone doji
  - market participation guidance remains cautious rather than opportunistic

invalidation_conditions:
  - decisive reclaim of daily structure before the 200 SMA test meaningfully develops
  - weekly warning fails and price quickly repairs higher-timeframe damage
  - master-level caution is replaced by constructive follow-through and improving tape

trade_master_terms:
  - not leaning one way or the other
  - no reason to try and force anything
  - preserve your mental capital
  - fresh and ready to go when conditions improve
  - testing the 200sma is inevitable
  - weekly gravestone doji

scan_translation:
  scanner_features_needed:
    - market regime state
    - 200 SMA proximity tracking
    - weekly candle-pattern or reversal-warning proxy
    - optional participation or exposure flagging for downstream scans
  candidate_rules:
    - QQQ pressing toward the 200 SMA with weak daily structure
    - weekly chart showing reversal-style warning rather than repair
    - mark regime as cautious or risk-reduced even if not fully directional
  open_questions:
    - whether the user's project can represent neutral-cautious regime states or only bullish versus bearish
    - how the scanner should approximate a weekly gravestone-doji warning if candlestick patterns are unsupported
    - whether caution-only guidance should suppress long scans or primarily reduce ranking and aggressiveness

example_posts:
  - Elite Swing Traders / QQQ / testing the 200sma is inevitable
  - Elite Swing Traders / QQQ / weekly gravestone doji
  - Elite Swing Traders / general caution / preserve mental capital and do not force anything

confidence: medium
risk_notes: cautionary regime guidance can shift quickly if price repairs, so the skill should treat this as a live posture layer that needs refreshing rather than as a permanent bearish thesis
notes: this example strengthens the higher-timeframe caution layer and preserves the master's explicit advice about participation quality, not just chart direction
```

## Example 18: SPY

Trade master: `Elite Swing Traders`

Original post:

> `$SPY Rounding top breakdown losing support and heading for the 200sma.`

Observed context:

- The post is about SPY as a broad market proxy rather than a single-stock trade
- Price has already broken down from a broad topping structure instead of simply failing one short rally
- Support is no longer holding, and the next major reference point is the 200 SMA below
- The message is more structurally bearish than a routine weak-tape comment, but it still stops short of an actual 200 SMA loss

Normalized strategy:

- `index-breakdown-into-200sma-test`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: index-breakdown-into-200sma-test
ticker_example: SPY
setup_type: structural bearish market-context breakdown into long-term support
market_bias: bearish
timeframe: daily

pattern_sequence:
  - index forms a broad rounding-top style structure
  - support begins to fail rather than hold or repair
  - breakdown resolves lower out of the topping structure
  - price starts heading toward the 200 SMA as the next major support reference

trigger_conditions:
  - broad topping or rounding-top structure visible on the daily chart
  - breakdown below meaningful support rather than another contained pullback
  - downside path opening toward the 200 SMA

confirmation_conditions:
  - continued lower movement after support breaks
  - failed attempts to quickly reclaim the broken support
  - 200 SMA becoming the next obvious downside reference point

invalidation_conditions:
  - rapid reclaim of the broken support zone
  - rounding-top breakdown fails and reverses into constructive repair
  - 200 SMA test is avoided because price regains trend structure first

trade_master_terms:
  - rounding top breakdown
  - losing support
  - heading for the 200sma

scan_translation:
  scanner_features_needed:
    - index monitoring
    - support-break detection
    - structural topping or rolling-top proxy
    - 200 SMA distance or path tracking
    - optional bearish regime flagging for downstream scans
  candidate_rules:
    - SPY below recently important daily support
    - price structure rolling over out of a broader top rather than tightening constructively
    - downside path extending toward the 200 SMA
    - mark market regime as structurally weakening before an actual 200 SMA loss
  open_questions:
    - how the user's project should approximate a rounding-top breakdown without subjective chart drawing
    - whether the scanner can distinguish support loss from an ordinary pullback
    - how close price must be to the 200 SMA before this regime family becomes active

example_posts:
  - Elite Swing Traders / SPY / rounding top breakdown losing support and heading for the 200sma

confidence: medium
risk_notes: structural bearish breakdowns can still snap back sharply if support is quickly reclaimed, so this should remain a refreshed regime signal rather than a fixed long-term state
notes: this fills the gap between weak-tape deterioration and a full post-crossover 200 SMA loss by capturing the phase where structure has already broken and the 200 SMA has become the next likely destination
```

## Example 19: DELL

Trade master: `Elite Swing Traders`

Original post:

> `$DELL Triggered but more importantly the gap support entry it offered up Tuesday is worth studying. Buying off gap support offers up some of the best risk to reward entries out there.`

Observed context:

- The chart shows a prior earnings-driven gap that established a clear support shelf before the later trigger
- The post explicitly distinguishes between the later confirmation and the earlier, better-risk entry near gap support
- The master is pointing readers back to the support-based entry as the real lesson, not just the breakout continuation
- This reinforces that the edge comes from entering near clearly defined support while invalidation remains tight

Normalized strategy:

- `gap-support-pivot-entry`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: gap-support-pivot-entry
ticker_example: DELL
setup_type: earnings gap-support entry with later trigger confirmation
market_bias: bullish
timeframe: daily

pattern_sequence:
  - stock gaps strongly and leaves behind a meaningful support shelf
  - price later revisits or pivots from that gap-support zone
  - support entry offers tight risk and strong asymmetry before the move becomes obvious
  - a later trigger confirms continuation, but the superior reward/risk was at the earlier support buy

trigger_conditions:
  - identifiable gap support from a prior impulse move
  - constructive touch, hold, or pivot from that support zone
  - entry available close enough to the support shelf that invalidation remains nearby

confirmation_conditions:
  - price separates higher from gap support before becoming extended
  - later trigger or breakout confirms that the support entry was correctly positioned
  - support zone remains intact throughout the continuation

invalidation_conditions:
  - decisive loss of gap support
  - weak bounce that cannot separate from the support shelf
  - later trigger fails immediately back into the support zone

trade_master_terms:
  - triggered but more importantly the gap support entry
  - worth studying
  - buying off gap support
  - best risk to reward entries

scan_translation:
  scanner_features_needed:
    - gap-support zone detection
    - support-touch or pivot detection
    - optional distinction between early support entry and later breakout confirmation
    - ranking logic for entry quality
  candidate_rules:
    - prior gap support still active and nearby
    - price offering an orderly support-based entry before a later trigger fully resolves
    - rank the support entry above the later confirmation if both are visible
  open_questions:
    - whether the user's scanner can separately surface early support entries versus later breakout triggers
    - how the project should define a valid pivot from gap support
    - how much distance from the support shelf still preserves the master's preferred R/R profile

example_posts:
  - Elite Swing Traders / DELL / gap support entry worth studying even more than the later trigger

confidence: high
risk_notes: once the stock is triggering away from support, the setup may still work, but the asymmetric edge is no longer as strong as it was at the original support entry
notes: this sharpens `gap-support-pivot-entry` by explicitly teaching that the support-based buy and the later trigger are related but not equivalent in reward/risk quality
```

## Example 20: APP

Trade master: `Elite Swing Traders`

Original post:

> `$APP bounced back to the 200sma turning old support into new resistance. If we struggle to clear the 200 then I would look for short entry.`

Observed context:

- The chart is about a single stock, not a market proxy
- Price has rallied back into the 200-day simple moving average after prior damage
- The 200 SMA appears to coincide with an area that previously acted as support, but is now functioning as overhead resistance
- The short thesis is conditional: the master wants evidence that price cannot cleanly reclaim the 200 before acting

Normalized strategy:

- `failed-200sma-reclaim-short-entry`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: failed-200sma-reclaim-short-entry
ticker_example: APP
setup_type: bearish reclaim-failure short setup
market_bias: bearish
timeframe: daily

pattern_sequence:
  - stock breaks down enough to lose a previously important support area and the 200 SMA
  - price bounces back toward the 200 SMA after the damage
  - the old support zone now overlaps with or reinforces the 200 SMA as new resistance
  - price struggles to clear that resistance cleanly
  - short entry becomes attractive if the reclaim attempt fails

trigger_conditions:
  - stock trading into or just under the 200 SMA after prior weakness
  - prior support now acting as overhead resistance
  - evidence that price is failing or struggling to reclaim the 200 SMA

confirmation_conditions:
  - rejection candle, stalled advance, or failed breakout through the 200 SMA
  - price remains below or loses the 200 SMA quickly after testing it
  - resistance holds where old support has flipped into supply

invalidation_conditions:
  - decisive reclaim and hold above the 200 SMA
  - old support successfully reclaims instead of acting as resistance
  - continued upside acceptance above the reclaim zone

trade_master_terms:
  - bounced back to the 200sma
  - turning old support into new resistance
  - struggle to clear the 200
  - look for short entry

scan_translation:
  scanner_features_needed:
    - 200 SMA detection
    - prior support or support-flip detection
    - failed reclaim or resistance-rejection detection
    - optional short-setup ranking
  candidate_rules:
    - stock below or testing the 200 SMA after prior breakdown
    - former support zone overlapping with the current reclaim attempt
    - price failing to gain acceptance above the 200 SMA
    - rank as a conditional short if rejection becomes visible
  open_questions:
    - how the user's scanner should approximate old support turning into new resistance
    - whether the project can detect failed reclaims versus simple proximity to the 200 SMA
    - what evidence should be required before surfacing a short candidate rather than a neutral alert

example_posts:
  - Elite Swing Traders / APP / bounced back to the 200sma and old support becoming new resistance

confidence: medium
risk_notes: reclaim-failure shorts can reverse sharply if the stock actually regains the 200 SMA, so the setup depends on waiting for visible failure rather than assuming resistance will hold automatically
notes: this is a stock-specific bearish setup, not a broad market-context warning, and it should remain separate from the index deterioration families
```

## Example 21: QQQ and SPY

Trade master: `Elite Swing Traders`

Original post:

> `$QQQ & $SPY`
>
> `Tops are a Process (The "Rounding" Shape)`
>
> `Market tops are rarely a single moment. Instead, they are a gradual exhaustion of buyers.`
>
> `The Psychology: Greed and "FOMO" (Fear Of Missing Out) keep investors in the game even as fundamentals deteriorate. People are reluctant to admit the party is over.`
>
> `The Action: This creates rounding tops or "Head and Shoulders" patterns. The market makes several attempts to go higher, fails, and trades sideways for months.`
>
> `The Speed: Breadth begins to thin—meaning while the main index (like the S&P 500) is still at highs, most individual stocks have already started falling. It is a slow "rolling over" rather than a sudden drop.`

Observed context:

- The post is explicitly educational and regime-focused rather than a direct entry alert
- Both QQQ and SPY weekly charts are shown in rounded topping structures near the highs
- The master emphasizes that tops develop through repeated failed pushes, sideways churn, and slow loss of participation
- Breadth deterioration is presented as a key internal warning: the index can still look fine while most stocks are already weakening

Normalized strategy:

- `index-top-process-rounding-rollover`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: index-top-process-rounding-rollover
ticker_example: QQQ and SPY
setup_type: early bearish market-regime deterioration
market_bias: cautious to bearish
timeframe: weekly

pattern_sequence:
  - major indices advance toward highs and begin losing momentum
  - topping structure becomes rounded rather than sharply impulsive
  - repeated attempts to push higher fail and resolve into sideways churn
  - market breadth thins as individual stocks weaken before the index fully breaks
  - the tape slowly rolls over before a cleaner breakdown becomes obvious

trigger_conditions:
  - index forming a rounding-top or head-and-shoulders style structure on the weekly chart
  - repeated failed attempts to continue higher
  - breadth deterioration visible beneath headline index strength
  - rolling-over behavior rather than clean bullish continuation

confirmation_conditions:
  - index remains unable to regain upside momentum after multiple attempts
  - breadth continues weakening while index structure deteriorates
  - later bearish families such as support loss, 200 SMA tests, or crossover weakness begin appearing

invalidation_conditions:
  - decisive upside continuation that negates the topping structure
  - renewed broad participation rather than thinning breadth
  - rolling-over action resolves into real accumulation instead of breakdown risk

trade_master_terms:
  - tops are a process
  - rounding shape
  - head and shoulders
  - gradual exhaustion of buyers
  - breadth begins to thin
  - slow rolling over

scan_translation:
  scanner_features_needed:
    - index monitoring
    - weekly structure assessment
    - repeated-failure or stalled-upside detection
    - breadth proxy or market-internals proxy
    - regime sequencing across early and late bearish phases
  candidate_rules:
    - major index near highs but momentum and participation deteriorating
    - topping structure becoming rounded or repeatedly failing rather than trending cleanly higher
    - breadth proxy weakening before headline index breakdown
    - mark regime as early deterioration before later breakdown triggers confirm
  open_questions:
    - what breadth proxies the user's scanner project can access
    - how the project should approximate a rounding-top or head-and-shoulders process without subjective drawing
    - whether this family should act as a caution overlay or a direct suppressor for bullish setups

example_posts:
  - Elite Swing Traders / QQQ and SPY / tops are a process and breadth begins to thin

confidence: medium
risk_notes: topping-process signals can persist for a long time before resolving, so they should be treated as regime deterioration evidence rather than as immediate timing signals on their own
notes: this family captures the early market-top process before the cleaner support-loss and 200-SMA breakdown families appear
```

## Example 22: ROIV

Trade master: `Elite Swing Traders`

Original post:

> `$ROIV RS new high setting up under ATH 28 resistance. ->Blue skies breakout.`

Observed context:

- The chart is about a single stock setting up just beneath all-time-high resistance near 28
- The RS behavior is highlighted first, implying leadership is already present before price fully clears
- Price appears to be tightening or consolidating directly under the all-time-high area rather than breaking down from it
- The expected outcome is a `blue skies breakout`, meaning price enters open territory with little overhead resistance once the level is cleared

Normalized strategy:

- `rs-led-ath-blue-skies-breakout`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: rs-led-ath-blue-skies-breakout
ticker_example: ROIV
setup_type: leadership-led all-time-high breakout
market_bias: bullish
timeframe: daily

pattern_sequence:
  - stock establishes leadership with RS strength before price fully confirms
  - price sets up constructively just beneath all-time-high resistance
  - tightening or orderly consolidation continues under the key level
  - breakout clears ATH resistance and enters blue-sky territory with little overhead supply

trigger_conditions:
  - RS line or RS behavior making a new high before price
  - stock trading directly under all-time-high resistance
  - constructive setup rather than rejection at the resistance zone

confirmation_conditions:
  - decisive breakout through the ATH level
  - follow-through after the breakout instead of immediate failure
  - continued RS leadership as price enters new-high territory

invalidation_conditions:
  - repeated failure at ATH resistance without breakout
  - RS leadership fades before price clears the level
  - breakout fails immediately back below the prior ATH area

trade_master_terms:
  - RS new high
  - setting up under ATH resistance
  - blue skies breakout

scan_translation:
  scanner_features_needed:
    - RS line or RS proxy
    - RS new-high detection
    - all-time-high resistance detection
    - near-resistance setup detection
    - breakout confirmation
  candidate_rules:
    - stock within breakout distance of all-time highs
    - RS line or RS proxy already at a fresh lookback high
    - price tightening or holding constructively under ATH resistance
    - rank highly if breakout would move into open price territory
  open_questions:
    - whether the user's scanner has a true RS line or only an RS Rating proxy
    - how close to ATH should count as "setting up under" resistance
    - what confirmation threshold should define a blue-sky breakout in the existing project

example_posts:
  - Elite Swing Traders / ROIV / RS new high setting up under ATH 28 resistance
  - Elite Swing Traders / ROIV / RS new high setting up under ATH resistance into blue skies breakout

confidence: medium
risk_notes: leadership-led ATH setups can fail if the stock repeatedly stalls under resistance or if the breakout lacks follow-through, so the leadership cue should improve quality but not replace the breakout test itself
notes: this family highlights the master's preference for RS leadership appearing before price clears the final resistance level, and this shorter ROIV phrasing works well as the precursor version before the actual breakout outcome is attached
```

## Example 23: AXTI

Trade master: `Elite Swing Traders`

Original post:

> `$AXTI example of buying RS on weakness. The 30 min pivot gave a $1.50 risk entry. Gapping up over 5% this morning. Study it. 8 ema pullback pretty good place to look for an entry.`

Observed context:

- The core idea is a `buy RS on weakness` setup on the daily chart rather than a weak stock bounce
- A lower-timeframe `30 min pivot` is used to define the actual entry with tight risk
- The strong follow-through gap the next morning validates the setup and shows the advantage of the tighter-risk trigger
- After the initial move, the rising `8 ema` is identified as a constructive pullback zone for a later or secondary entry

Normalized strategy:

- `rs-on-weakness-ltf-pivot-continuation`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: rs-on-weakness-ltf-pivot-continuation
ticker_example: AXTI
setup_type: relative-strength weakness buy with lower-timeframe trigger
market_bias: bullish
timeframe: daily thesis with 30-minute execution trigger

pattern_sequence:
  - stock shows leadership and relative strength despite a controlled pullback or pause
  - broader swing setup remains constructive rather than damaged
  - a 30-minute pivot creates a defined, tight-risk entry inside the larger setup
  - stock follows through strongly, including gap-up continuation the next session
  - later pullbacks toward the rising 8 EMA become preferred follow-on entry zones

trigger_conditions:
  - stock qualifies as an RS-on-weakness candidate on the higher timeframe
  - lower-timeframe pivot forms with clearly defined nearby risk
  - entry is still close enough to the pivot that the stop remains tight

confirmation_conditions:
  - immediate follow-through after the lower-timeframe pivot
  - next-session continuation or gap-up strength
  - price respects the rising 8 EMA on later pullbacks

invalidation_conditions:
  - lower-timeframe pivot fails and breaks the defined risk level
  - daily structure weakens enough that the RS-on-weakness thesis no longer holds
  - 8 EMA pullback fails to act as support after the move confirms

trade_master_terms:
  - buying RS on weakness
  - 30 min pivot
  - $1.50 risk entry
  - gapping up over 5% this morning
  - study it
  - 8 ema pullback pretty good place to look for an entry

scan_translation:
  scanner_features_needed:
    - RS leadership or RS-on-weakness detection
    - multi-timeframe support
    - 30-minute pivot detection or lower-timeframe trigger proxy
    - next-session gap follow-through detection
    - 8 EMA pullback detection
  candidate_rules:
    - stock remains a leader while pulling back or pausing constructively
    - lower-timeframe pivot offers unusually tight defined risk
    - follow-through confirms the pivot and preserves the 8 EMA as dynamic support
    - allow primary entry and secondary pullback-entry interpretations within the same setup family
  open_questions:
    - whether the user's scanner project supports intraday timeframe triggers like 30-minute pivots
    - how the project should define a valid `buy RS on weakness` candidate mechanically
    - whether 8 EMA pullback entries should be ranked as add-on entries or fresh standalone opportunities

example_posts:
  - Elite Swing Traders / AXTI / buying RS on weakness with 30 min pivot and 8 ema pullback

confidence: medium
risk_notes: lower-timeframe pivot entries can improve reward/risk substantially, but they also fail quickly if the pivot is lost, so the multi-timeframe thesis needs both swing quality and execution discipline
notes: this family formalizes how the master can pair a daily RS-on-weakness thesis with a lower-timeframe trigger and then use the 8 EMA as the next constructive support test
```

## Example 24: ROIV

Trade master: `Elite Swing Traders`

Original post:

> `$ROIV RS new high before price. Closed at high of day.`

Observed context:

- The chart is still focused on ROIV beneath or near the all-time-high area rather than after a fully mature breakout
- The key message is leadership first: the RS line is ahead of price
- `Closed at high of day` adds a useful execution clue, showing buyers maintained control into the close instead of fading
- This reads like a strengthening setup-quality comment for the existing ATH-breakout family rather than a separate pattern

Normalized strategy:

- `rs-led-ath-blue-skies-breakout`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: rs-led-ath-blue-skies-breakout
ticker_example: ROIV
setup_type: leadership-led breakout pressure building under ATH resistance
market_bias: bullish
timeframe: daily

pattern_sequence:
  - RS line leads by making a new high before price fully confirms
  - stock remains positioned beneath major resistance or all-time-high territory
  - buyers maintain control through the session and the stock closes at the high of day
  - breakout pressure continues building ahead of the expected move through resistance

trigger_conditions:
  - RS new high before price
  - stock still close to key resistance rather than extended far above it
  - close at or very near the high of day, showing strength into the session finish

confirmation_conditions:
  - subsequent breakout through the resistance or ATH zone
  - continued strength after the strong close instead of immediate fade
  - RS leadership remains intact as price follows through

invalidation_conditions:
  - strong-close setup stalls repeatedly and fails to clear resistance
  - RS leadership fades before price confirms
  - next session reverses the strong close and weakens the setup structure

trade_master_terms:
  - RS new high before price
  - closed at high of day

scan_translation:
  scanner_features_needed:
    - RS new-high detection
    - resistance or ATH proximity detection
    - close-location-in-range measurement
    - breakout follow-through tracking
  candidate_rules:
    - stock within breakout distance of major resistance or ATH
    - RS line already making a new high before price
    - stock closes near or at session highs to show pressure is still building
    - up-rank if breakout follow-through becomes likely rather than already extended
  open_questions:
    - what close-location threshold the user's scanner should use for "closed at high of day"
    - whether the project can combine RS leadership with resistance proximity in one ranking rule
    - how long this strong-close signal should remain actionable if breakout does not happen immediately

example_posts:
  - Elite Swing Traders / ROIV / RS new high before price and closed at high of day

confidence: medium
risk_notes: strong closes beneath resistance can still fail if the breakout does not arrive quickly or if the next session reverses, so the close-strength cue should improve quality but not replace the need for actual follow-through
notes: this reinforces `rs-led-ath-blue-skies-breakout` by showing that the master values not just RS leadership, but also strong closes that suggest pressure is building into the eventual breakout
```

## Example 25: Fake-Out Versus Trend Framework

Trade master: `Elite Swing Traders`

Original post:

> `A "fake-out" (or bull/bear trap) is one of the most frustrating experiences for a trader. It happens when the price breaks through a consolidation boundary, lures everyone in, and then sharply reverses.`
>
> `To big players, these are "liquidity grabs." They need a surge of buying or selling volume to fill their large orders, and nothing creates volume like a bunch of retail traders rushing into a breakout.`
>
> `Here is how to spot the difference between a trap and a trend.`
>
> `1. The Volume Confirmation`
>
> `A Real Breakout: Should be accompanied by a massive spike in volume (usually 50% higher than the average volume of the previous days). This shows institutional conviction.`
>
> `A Fake-Out: The price drifts above resistance on low or average volume. If the "big money" isn't participating, the move likely won't hold.`
>
> `2. The "Re-test" Requirement`
>
> `After a stock breaks out of consolidation, it often returns to the level it just broke (the old "ceiling") to see if it now acts as a "floor" (support).`
>
> `True Move: The price hits the old resistance level, bounces, and heads higher.`
>
> `Fake-Out: The price falls right back through the level and settles back into the old consolidation range.`
>
> `3. The "Closing" Rule`
>
> `The Filter: Never trust a breakout until the candle closes on the timeframe you are trading (e.g., the Daily or 4-hour chart). If the price leaves a long "wick" at the top and closes back inside the range, it was a trap.`
>
> `Pro-Tip: The "2% Rule"`
>
> `Many institutional traders won't consider a breakout valid unless the price holds at least 2% beyond the resistance level. This "buffer" helps filter out the noise of minor stop-loss hunting.`

Observed context:

- This is an educational framework rather than a single ticker setup
- The master is defining how to confirm or reject a breakout after price moves through consolidation boundaries
- The framework is symmetric enough to help with both bullish breakouts and bearish breakdowns, even though the examples are phrased mostly from the long side
- The key filters are volume quality, successful re-test behavior, timeframe-close confirmation, and a small confirmation buffer beyond resistance

Normalized strategy:

- `breakout-validation-fakeout-filter`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: breakout-validation-fakeout-filter
ticker_example: framework
setup_type: breakout validation and trap detection
market_bias: neutral framework
timeframe: depends on traded timeframe

pattern_sequence:
  - price moves through a consolidation boundary or key level
  - initial participation surges as traders react to the apparent breakout or breakdown
  - quality of the move is judged by volume, re-test behavior, and candle close
  - true moves hold outside the range and continue
  - fake-outs slip back inside the range and reveal the move as a trap or liquidity grab

trigger_conditions:
  - price attempts to break out of or break down from consolidation
  - move can be evaluated using volume, retest behavior, and the relevant timeframe close

confirmation_conditions:
  - volume materially above recent average
  - successful retest of the broken level
  - candle closes outside the range on the traded timeframe
  - price holds a modest buffer beyond the level instead of barely poking through

invalidation_conditions:
  - move occurs on low or average volume
  - retest fails and price settles back into the old range
  - candle leaves a long wick and closes back inside the range
  - move cannot maintain a small confirmation buffer beyond the level

trade_master_terms:
  - fake-out
  - bull/bear trap
  - liquidity grabs
  - volume confirmation
  - re-test requirement
  - closing rule
  - 2% rule

scan_translation:
  scanner_features_needed:
    - breakout and breakdown detection
    - relative volume or volume-spike measurement
    - retest detection
    - close-location relative to prior range
    - distance-beyond-level measurement
  candidate_rules:
    - up-rank breakout families when volume expands, retest holds, and the close remains outside the range
    - down-rank or reject breakout families when price drifts through resistance without volume or closes back inside the range
    - apply same logic inversely to bearish breakdowns
  open_questions:
    - how the user's scanner should define recent average volume
    - whether the project can detect retests and closes relative to prior consolidation ranges
    - whether the 2% buffer should be configurable by asset class or volatility

example_posts:
  - Elite Swing Traders / framework / fake-out versus real breakout validation rules

confidence: high
risk_notes: confirmation filters can improve breakout quality but may also delay entry, so they should be treated as validation layers rather than guarantees
notes: this framework should sit on top of multiple breakout and breakdown families rather than replace them, because it explains how the master confirms whether a move is real
```

## Example 26: XLI and DE

Trade master: `Elite Swing Traders`

Original post:

> `$XLI Double inside week leads to blue skies breakout. When a sector ETF is setting up go find the best charts setting up in the ETF. $DE perfect example. This is a top down approach.`

Observed context:

- The post starts with a sector ETF, not a single stock
- `XLI` is the group-level trigger, using a `double inside week` compression that resolves into a `blue skies breakout`
- The master then explicitly shifts into stock selection, saying to go find the best charts inside that ETF
- `DE` is presented as the aligned constituent example, showing how the ETF setup leads the search for individual names

Normalized strategy:

- `sector-etf-top-down-blue-skies-breakout`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: sector-etf-top-down-blue-skies-breakout
ticker_example: XLI and DE
setup_type: top-down sector-led breakout workflow
market_bias: bullish
timeframe: weekly

pattern_sequence:
  - sector ETF compresses through a double-inside-week style setup
  - ETF resolves upward into a blue-sky breakout
  - group strength becomes the screening lens for stock selection
  - trader searches the ETF constituents for the strongest aligned charts
  - leading stock examples inside the group become the actual trade candidates

trigger_conditions:
  - sector ETF showing a tight weekly compression such as a double inside week
  - breakout through key resistance or into blue-sky territory
  - constituent stock charts in the same ETF setting up constructively at the same time

confirmation_conditions:
  - ETF breakout follows through rather than failing immediately
  - selected constituent charts show aligned strength and actionable setups
  - group leadership helps the best stocks inside the ETF expand with it

invalidation_conditions:
  - ETF breakout fails and falls back into the prior range
  - constituent charts are weak or poorly aligned despite the ETF setup
  - top-down group strength does not translate into strong individual stock action

trade_master_terms:
  - double inside week
  - blue skies breakout
  - sector ETF is setting up
  - go find the best charts setting up in the ETF
  - top down approach

scan_translation:
  scanner_features_needed:
    - sector ETF monitoring
    - weekly inside-bar or compression detection
    - breakout detection
    - ETF constituent mapping
    - ranking of strongest charts within a selected ETF or industry group
  candidate_rules:
    - detect sector ETFs breaking out from tight weekly compression
    - surface the strongest aligned constituent charts within that ETF
    - allow the ETF breakout to increase ranking for names inside the same group
    - keep ETF trigger and stock candidate as linked but separate outputs
  open_questions:
    - whether the user's scanner project can map ETFs to their constituents directly
    - how the project should detect a double inside week mechanically
    - whether the ETF breakout should hard-filter constituents or simply boost their rank

example_posts:
  - Elite Swing Traders / XLI and DE / double inside week leads to blue skies breakout and top-down selection

confidence: medium
risk_notes: a strong ETF can improve the odds for leading names inside the group, but weak constituent selection can still underperform even when the ETF breaks out, so the top-down lens should guide filtering rather than replace chart quality
notes: this family captures the master's explicit workflow of starting with a sector ETF setup and then drilling down into the best individual charts inside that group
```

## Example 27: PL

Trade master: `Elite Swing Traders`

Original post:

> `$PL working on an engulfing candle. Approaching the next pivot`

Observed context:

- The chart appears to show PL continuing to hold up after the earlier earnings-gap advance rather than failing the structure
- The post is more tactical than foundational: it is focused on the current candle and nearby pivot progression inside an already-constructive chart
- `Engulfing candle` suggests renewed buyer control or continuation quality in the current daily action
- `Approaching the next pivot` implies the move is not done at support; price is now pressing toward the next resistance or trigger level

Normalized strategy:

- `gap-support-pivot-entry`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: gap-support-pivot-entry
ticker_example: PL
setup_type: post-gap continuation candle into next pivot
market_bias: bullish
timeframe: daily

pattern_sequence:
  - stock holds the constructive post-gap structure rather than backfilling or breaking down
  - daily candle action strengthens through an engulfing-style reversal or continuation bar
  - buyers regain control and push price higher within the existing trend
  - price advances toward the next pivot or nearby resistance objective

trigger_conditions:
  - prior bullish structure remains intact after the gap-driven move
  - engulfing or strong reclaim candle appears in a constructive location
  - price still has room to work toward the next pivot

confirmation_conditions:
  - candle follow-through after the engulfing day
  - continued respect of short-term support such as the 8 EMA or prior gap structure
  - push into or through the next pivot instead of immediate stall

invalidation_conditions:
  - engulfing candle fails immediately and gives back the reclaimed ground
  - price loses the underlying post-gap support structure
  - move stalls below the next pivot and rolls back into weakness

trade_master_terms:
  - engulfing candle
  - approaching the next pivot

scan_translation:
  scanner_features_needed:
    - bullish engulfing or strong reversal-candle detection
    - prior gap-support or continuation context
    - pivot or nearby resistance detection
    - short-term support tracking
  candidate_rules:
    - stock remains in a valid post-gap continuation structure
    - bullish engulfing or equivalent strong reclaim candle appears
    - price is advancing toward the next pivot with support intact
    - up-rank if the candle appears after constructive consolidation rather than after extension
  open_questions:
    - whether the user's scanner can detect engulfing candles directly or needs a proxy
    - how the project defines the next pivot in a reusable way
    - whether this should be ranked as a continuation add-on signal versus a fresh entry

example_posts:
  - Elite Swing Traders / PL / engulfing candle approaching the next pivot

confidence: medium
risk_notes: engulfing candles can fail quickly if they appear too late in the move or without follow-through, so this should act as a continuation-quality signal layered on top of the broader post-gap structure
notes: this reinforces `gap-support-pivot-entry` by showing how the master also monitors the post-gap continuation phase through bullish candle quality and progress toward the next pivot
```

## Example 28: COHR basket

Trade master: `Elite Swing Traders`

Original post:

> `@1ChartMaster`
>
> `$COHR`
> `$TESM`
> `$PL`
> `$GLW`
> `$LITE`
> `$SMTC`
> `$UCTT`
> `$CIEN`
> `$FIVE`
> `$AXTI`
> `$CLS`
>
> `some of the stocks that made 8 week support pivots. Buy RS on weakness.`

Observed context:

- This is a basket post rather than a single-chart callout, which is strong evidence that the master sees a reusable setup family across multiple names
- The shared feature is not just a pullback, but a constructive pivot from higher-timeframe `8 week` support
- `Buy RS on weakness` frames the ranking logic: favor leaders and momentum names whose relative strength holds up during the pullback
- The user-suggested idea that a clean retest of 8-week support can also be an entry for momentum leaders is reasonable, but it should be stored as an inferred extension rather than as direct master wording

Normalized strategy:

- `rs-on-weakness-8-week-support-pivot`

Suggested strategy record:

```yaml
trade_master: Elite Swing Traders
strategy_name: rs-on-weakness-8-week-support-pivot
ticker_example: COHR
setup_type: relative-strength weekly support pivot in a momentum leader
market_bias: bullish
timeframe: weekly support context with daily execution

pattern_sequence:
  - leadership or momentum stock pulls back in an orderly way after prior strength
  - price tests the 8-week support zone rather than breaking trend outright
  - stock pivots constructively from that higher-timeframe support area
  - relative strength holds up well enough that the weakness is treated as a buy zone instead of structural failure
  - upside continuation can resume from the initial pivot or from a later clean retest if leadership remains intact

trigger_conditions:
  - stock qualifies as a momentum or RS leader rather than a laggard rebound
  - price interacts constructively with 8-week support
  - pivot occurs close enough to support that risk remains defined

confirmation_conditions:
  - pivot day or subsequent sessions show constructive reclaim or continuation away from 8-week support
  - RS behavior remains firm during the pullback
  - later retests, if any, continue to respect 8-week support rather than slicing through it

invalidation_conditions:
  - stock loses 8-week support decisively instead of pivoting
  - RS deteriorates enough that the name no longer behaves like a leader on weakness
  - repeated retests weaken support and change the setup from controlled pullback to breakdown risk

trade_master_terms:
  - 8 week support pivots
  - Buy RS on weakness

scan_translation:
  scanner_features_needed:
    - RS leadership or momentum-leader detection
    - weekly support interaction detection centered on the 8-week moving average or support zone
    - pivot or reclaim detection after touching weekly support
    - support-retest tracking
  candidate_rules:
    - rank stocks with strong RS that pull back constructively into 8-week support
    - require evidence of a pivot or constructive hold rather than a simple touch
    - allow a later retest entry only when the stock is still behaving like a true momentum leader
    - down-rank names with too many support tests or obvious loss of trend quality
  open_questions:
    - whether the scanner project uses an explicit 8-week moving average, a 40-day proxy, or a price-to-support approximation
    - how the project should define a valid pivot versus a mere pause at weekly support
    - whether retest entries should be modeled inside this family or as a separate inferred subtype

example_posts:
  - Elite Swing Traders / COHR TESM PL GLW LITE SMTC UCTT CIEN FIVE AXTI CLS / 8 week support pivots and buy RS on weakness

confidence: medium
risk_notes: higher-timeframe support pivots in leaders can offer favorable continuation entries, but the edge fades quickly if the name stops acting like a leader or if repeated tests weaken the support shelf
notes: this is a cross-sectional basket example, which makes it strong evidence that `8 week support pivots` is a reusable family for this master; the retest idea is a reasonable extension for momentum leaders, but it should be tagged as an inference unless future master posts state it directly
```

## Example 29: Sean trades system diagram

Trade master: `Sean trades`

Original post:

> `The entire system that made me over 100k today...`
>
> `Keep it simple.`

Observed context:

- This is a generalized system diagram rather than a real ticker chart, so the main evidence is the structure being taught
- The setup begins with a `leading stock`, which acts as a quality filter before the trigger appears
- Price pulls back into a rising `8 EMA` while interacting with a horizontal reference level
- The stock briefly `undercuts` that level, then reclaims and turns higher
- The diagram implies a long entry around the reclaim zone, with the `stop loss` placed beneath the undercut low

Normalized strategy:

- `leading-stock-undercut-8ema-reclaim`

Suggested strategy record:

```yaml
trade_master: Sean trades
strategy_name: leading-stock-undercut-8ema-reclaim
setup_type: leading-stock undercut reclaim near rising 8 EMA
market_bias: bullish
timeframe: daily, inferred from the 8 EMA framing

pattern_sequence:
  - stock establishes itself as a leader before the setup begins
  - price pulls back toward a horizontal reference level while the 8 EMA continues rising underneath or nearby
  - price briefly undercuts the reference low or support area to shake out weak holders
  - stock reclaims the area and offers a tight-risk entry as it turns back up
  - upside continuation resumes once the reclaim holds

trigger_conditions:
  - stock is a leading name rather than a weak oversold bounce
  - price undercuts a clear prior support or pivot level
  - reclaim occurs in constructive proximity to a rising 8 EMA
  - entry is still close enough to the reclaim that risk can stay tight

confirmation_conditions:
  - reclaim holds instead of immediately failing back below the undercut low
  - price starts to separate upward from the reclaim area
  - 8 EMA continues acting as rising dynamic support rather than flattening or rolling over

invalidation_conditions:
  - price loses the undercut low after the reclaim attempt
  - stock fails to hold the reclaimed support area
  - 8 EMA support no longer aligns with the setup and trend quality deteriorates

trade_master_terms:
  - keep it simple
  - leading stock
  - undercut
  - 8 EMA
  - entry
  - stop loss

scan_translation:
  scanner_features_needed:
    - leadership filter
    - prior-low or support-level detection
    - undercut-and-reclaim detection
    - 8 EMA trend and proximity detection
    - tight-risk or stop-distance estimation
  candidate_rules:
    - start with leading stocks in established uptrends
    - detect names that briefly trade below a recent support or pivot low
    - require a reclaim back through the level while the 8 EMA is still rising
    - prefer entries that remain close to the reclaim so the stop can sit beneath the sweep low
  open_questions:
    - whether the intended trigger is the intraday reclaim, the close back above the level, or the first constructive pullback after reclaim
    - how the user's scanner should define a `leading stock`
    - whether the horizontal level should be modeled as a prior day low, pivot low, short base support, or another support proxy

example_posts:
  - Sean trades / system diagram / leading stock undercut reclaim near 8 EMA

confidence: medium
risk_notes: undercut-and-reclaim entries can offer tight risk and strong continuation when the stock is a true leader, but failed reclaims often reverse quickly, so stop discipline beneath the sweep low is central to the setup
notes: this is a diagrammatic teaching post rather than a ticker-specific alert, so the structural logic is clearer than the exact mechanical trigger; the reclaim interpretation is strong, but the precise entry rule should stay slightly provisional until more Sean examples are added
```

## Example 30: Venu CAN SLIM framework

Trade master: `Venu`

Original post:

> `The 7 rules every CAN SLIM stock must pass:`
>
> `C - current quarterly EPS up 25%+ YoY, accelerating`
>
> `A - 3 year annual EPS growth above 25%`
>
> `N - new product, new highs, or new management`
>
> `S - supply tight (buybacks, insider holds, low float)`
>
> `L - leader in its industry`
>
> `I - institutional sponsorship rising QoQ`
>
> `M - market in confirmed uptrend`
>
> `Only 2% of stocks pass all 7.`
>
> `That's where the real leaders come from.`

Observed context:

- This is an educational stock-selection framework, not a ticker-specific alert or a chart-entry diagram
- The post mixes fundamental growth filters, supply and sponsorship filters, leadership filters, and a broad market-regime filter
- `Only 2% of stocks pass all 7` shows that the framework is intentionally selective and designed to isolate elite leadership candidates
- The framework does not specify a precise entry trigger, so it should be stored as an upstream qualification layer that can rank or filter names before chart timing is applied

Normalized strategy:

- `canslim-leadership-selection-framework`

Suggested strategy record:

```yaml
trade_master: Venu
strategy_name: canslim-leadership-selection-framework
ticker_example: framework
setup_type: CAN SLIM leadership qualification framework
market_bias: bullish selection framework
timeframe: mixed fundamental and regime framework

pattern_sequence:
  - stock passes strong current earnings-growth tests
  - longer-term annual earnings growth confirms the business has persistent quality
  - company or chart has a meaningful new catalyst, new high, or new leadership event
  - share supply characteristics remain favorable rather than bloated
  - stock proves it is an industry leader rather than a laggard
  - institutional sponsorship is increasing
  - broad market remains in a confirmed uptrend before aggressive participation

trigger_conditions:
  - current quarterly EPS growth of at least 25% year over year, ideally accelerating
  - annual EPS growth above 25% over a three-year period
  - at least one valid `N` catalyst such as new product, new highs, or new management
  - favorable supply characteristics and leadership evidence
  - market in confirmed uptrend

confirmation_conditions:
  - multiple CAN SLIM dimensions align instead of only one or two
  - stock ranks as a true leader within its industry peer group
  - institutional sponsorship continues rising as the stock remains in a favorable market regime

invalidation_conditions:
  - earnings acceleration weakens materially
  - stock loses leadership status within its group
  - sponsorship deteriorates or the market exits confirmed uptrend conditions
  - too many CAN SLIM gates fail for the stock to remain elite-quality

trade_master_terms:
  - CAN SLIM
  - current quarterly EPS up 25%+ YoY, accelerating
  - 3 year annual EPS growth above 25%
  - new product, new highs, or new management
  - supply tight
  - leader in its industry
  - institutional sponsorship rising QoQ
  - market in confirmed uptrend
  - only 2% of stocks pass all 7
  - real leaders

scan_translation:
  scanner_features_needed:
    - quarterly EPS growth data
    - annual EPS growth history
    - catalyst or new-high detection
    - float, buyback, or insider-holding proxies
    - industry-relative leadership ranking
    - institutional ownership trend data
    - broad-market regime filter
  candidate_rules:
    - require strong earnings growth now and over the multi-year window
    - require evidence of novelty, leadership, and tightening supply
    - require rising institutional sponsorship
    - apply the framework as a ranking and filtering layer before chart-entry rules
    - block or down-rank candidates when the broad market is not in confirmed uptrend
  open_questions:
    - which available project fields can approximate the `N` and `S` letters most faithfully
    - whether institutional sponsorship data exists directly in the user's scanner project
    - how the project defines `market in confirmed uptrend`, such as S&P above the 200 DMA or another regime model

example_posts:
  - Venu / CAN SLIM / seven-rule leadership framework

confidence: high
risk_notes: a strong qualification framework can improve the quality of the watchlist, but it does not replace timing, risk management, or market-context shifts, so passing CAN SLIM should qualify a stock for attention rather than guarantee a successful trade
notes: this framework is best treated as a top-of-funnel leadership selector that can feed later entry models such as breakouts, pullbacks, or reclaim setups; `M` should remain an explicit market-regime gate rather than being absorbed into the stock-specific letters
```

## Example 31: Venu cup and handle

Trade master: `Venu`

Original post:

> `THE CUP & HANDLE`
>
> `ONeils #1 Pattern`
>
> `Buy at pivot. Stop at -8%. Ride the leader.`

Observed context:

- This is a schematic chart-pattern lesson rather than a live ticker callout, but the pattern mechanics are shown clearly
- The structure includes a rounded cup, a prior `left lip`, a shorter `handle`, and a `pivot point` near the handle high
- The breakout is expected to occur with a `volume surge`, not on weak participation
- The post gives both an execution rule and a risk rule: buy at the pivot and cut the trade if it falls roughly 8% below entry

Normalized strategy:

- `cup-handle-pivot-breakout`

Suggested strategy record:

```yaml
trade_master: Venu
strategy_name: cup-handle-pivot-breakout
ticker_example: framework
setup_type: O'Neil cup-and-handle breakout
market_bias: bullish
timeframe: multi-week base with breakout trigger

pattern_sequence:
  - stock forms a rounded cup over a multi-week period
  - price recovers toward the prior left-lip resistance area
  - a shorter handle forms near the highs as the final shakeout or pause
  - stock clears the pivot point from the handle area
  - breakout follows through with a volume surge

trigger_conditions:
  - cup base is sufficiently developed rather than a tiny short-term wiggle
  - handle forms near the top of the base
  - pivot point is clearly identifiable from the handle resistance area
  - breakout occurs through the pivot with supporting volume

confirmation_conditions:
  - breakout day shows strong volume expansion
  - price holds above the pivot rather than instantly falling back into the handle
  - stock behaves like a true leader after breakout instead of stalling immediately

invalidation_conditions:
  - breakout fails and falls back below the pivot
  - handle deepens enough to damage the structure materially
  - trade violates the approximate -8 percent stop rule after entry

trade_master_terms:
  - O'Neil's #1 pattern
  - cup & handle
  - left lip
  - 5-7 week base
  - pivot point
  - breakout + volume
  - volume surge
  - buy at pivot
  - stop at -8%
  - ride the leader

scan_translation:
  scanner_features_needed:
    - multi-week rounded-base detection
    - handle detection near highs
    - pivot-point identification
    - breakout and volume-surge detection
    - post-entry stop-distance monitoring
  candidate_rules:
    - detect stocks forming multi-week cups that recover close to prior highs
    - require a smaller handle near the top of the structure
    - trigger on breakout through the pivot with volume support
    - down-rank or reject breakouts that are already extended far beyond the pivot
  open_questions:
    - how the user's scanner should quantify a valid cup versus any generic rounded recovery
    - how deep the handle can be before the pattern quality is considered impaired
    - whether the project can encode the -8 percent stop rule as a downstream alert rather than a scan filter

example_posts:
  - Venu / cup and handle / buy at pivot, stop at -8%, ride the leader

confidence: high
risk_notes: cup-and-handle breakouts can produce powerful trend continuation when true leaders clear the pivot on volume, but failed breakouts often reverse back into the base quickly, which is why the stop discipline is part of the pattern rather than an optional add-on
notes: this functions as the chart-entry layer beneath Venu's CAN SLIM stock-selection framework; the post is schematic, but the core breakout mechanics are explicit enough to preserve with high confidence
```

## Example 32: Venu O'Neil five patterns

Trade master: `Venu`

Original post:

> `ONeils 5 CHART PATTERNS`
>
> `CUP & HANDLE`
>
> `Most reliable.`
>
> `FLAT BASE`
>
> `5+ wks tight, <15% range.`
>
> `DOUBLE BOTTOM`
>
> `W-shape, 7+ wks.`
>
> `SAUCER`
>
> `Long, shallow, patient.`
>
> `HIGH TIGHT FLAG`
>
> `Rare. Strongest. +100% prior run.`
>
> `Find the pattern.`
>
> `Wait for pivot.`
>
> `Cut at -8%.`

Observed context:

- This is a taxonomy post that organizes several O'Neil-style base patterns rather than drilling into one live setup
- The post supplies brief defining cues for each pattern and a shared execution rule set
- `Wait for pivot` shows that pattern recognition alone is not enough; timing still depends on a specific breakout trigger
- `Cut at -8%` is presented as a universal risk rule across the pattern family, not just one special-case tactic

Normalized strategy:

- `oneil-five-base-patterns-framework`

Suggested strategy record:

```yaml
trade_master: Venu
strategy_name: oneil-five-base-patterns-framework
ticker_example: framework
setup_type: O'Neil base-pattern timing framework
market_bias: bullish timing framework
timeframe: multi-week base taxonomy

pattern_sequence:
  - identify a valid base archetype rather than forcing every chart into the same shape
  - wait for the correct pivot associated with that base
  - enter only when price confirms through the pivot
  - enforce loss control if the breakout fails

trigger_conditions:
  - stock forms one of the named O'Neil base patterns
  - pivot point is clearly defined for that pattern
  - breakout trigger occurs rather than premature anticipation

confirmation_conditions:
  - pattern fits the expected structural cues for its type
  - breakout shows constructive follow-through, ideally with strong participation
  - stock remains a leader after the pivot rather than immediately failing

invalidation_conditions:
  - pattern morphs into a lower-quality or damaged structure
  - breakout fails after the pivot
  - trade violates the approximate -8 percent stop rule

trade_master_terms:
  - cup & handle
  - most reliable
  - flat base
  - 5+ wks tight, <15% range
  - double bottom
  - W-shape, 7+ wks
  - saucer
  - long, shallow, patient
  - high tight flag
  - rare
  - strongest
  - +100% prior run
  - find the pattern
  - wait for pivot
  - cut at -8%

scan_translation:
  scanner_features_needed:
    - pattern-classification or pattern-specific detection
    - pivot-point identification by base type
    - breakout confirmation
    - risk-rule tracking after entry
  candidate_rules:
    - classify candidate charts into cup-and-handle, flat-base, double-bottom, saucer, or high-tight-flag buckets
    - require each bucket to satisfy its own structural constraints before activating a pivot watch
    - trigger only when price confirms through the relevant pivot
    - attach a common post-entry failure rule near -8 percent
  open_questions:
    - which of the five patterns the user's scanner can realistically express first
    - how much structural precision is available for rare patterns like high tight flag
    - whether the scanner should treat this as one framework output or several separate pattern modules

example_posts:
  - Venu / O'Neil 5 chart patterns / find the pattern, wait for pivot, cut at -8%

confidence: medium
risk_notes: a broad pattern taxonomy can help organize timing setups, but each pattern still needs its own structural checks and a failed breakout can happen in any family, so the shared -8 percent rule remains central
notes: this framework sits downstream from Venu's CAN SLIM selector and upstream from specific breakout entries; cup and handle is the most fully specified member so far, while the other four are preserved as pattern families with lighter detail until more examples arrive
```

## Example 33: Venu Lynch six-rule screen

Trade master: `Venu`

Original post:

> `Lynch's 6 rules for finding multi-baggers:`
>
> `• Trailing P/E < 25`
>
> `• Forward P/E < 15`
>
> `• Debt/Equity < 35%`
>
> `• EPS Growth > 15%`
>
> `• PEG Ratio < 2`
>
> `• Market Cap > $5B`
>
> `All six. At the same time. That's the screen.`

Observed context:

- This is a strict numeric stock screen, not a chart setup and not a broad acronym framework
- The edge of the post is the simultaneous use of six thresholds rather than any one metric in isolation
- The screen blends valuation, growth, leverage, and size filters to narrow the universe before any pattern timing is considered
- `That's the screen` implies the framework is meant to be used mechanically as a hard gate

Normalized strategy:

- `lynch-six-rule-multibagger-screen`

Suggested strategy record:

```yaml
trade_master: Venu
strategy_name: lynch-six-rule-multibagger-screen
ticker_example: framework
setup_type: Lynch-style multibagger numeric screen
market_bias: bullish selection framework
timeframe: mixed fundamental screen

pattern_sequence:
  - start with stocks large enough to clear the minimum size threshold
  - require valuation to remain reasonable on both trailing and forward earnings
  - require leverage to stay controlled
  - require earnings growth strong enough to justify the growth label
  - require the full set of constraints to pass simultaneously before a stock qualifies

trigger_conditions:
  - trailing P/E below 25
  - forward P/E below 15
  - debt/equity below 35 percent
  - EPS growth above 15 percent
  - PEG ratio below 2
  - market capitalization above 5 billion dollars

confirmation_conditions:
  - all six conditions pass at the same time
  - valuation and growth remain aligned rather than one metric deteriorating sharply
  - stock still looks like a viable leadership candidate after the numeric screen is applied

invalidation_conditions:
  - one or more thresholds fail materially
  - leverage or valuation expands enough to break the screen
  - growth slows below the required hurdle

trade_master_terms:
  - Lynch's 6 rules
  - trailing P/E < 25
  - forward P/E < 15
  - debt/equity < 35%
  - EPS growth > 15%
  - PEG ratio < 2
  - market cap > $5B
  - all six
  - at the same time
  - that's the screen

scan_translation:
  scanner_features_needed:
    - trailing P/E data
    - forward P/E estimates
    - debt/equity ratio
    - EPS growth data
    - PEG ratio
    - market capitalization
  candidate_rules:
    - filter the universe to names that satisfy all six numeric rules simultaneously
    - treat failed thresholds as hard exclusions rather than soft ranking penalties
    - use the resulting list as an upstream candidate pool for later chart-based timing
  open_questions:
    - whether the user's project has all six fields directly available
    - how EPS growth should be measured, such as quarterly, annual, or trailing composite growth
    - whether market cap should be evaluated in nominal dollars only or inflation-adjusted for historical studies

example_posts:
  - Venu / Lynch's 6 rules / all six at the same time

confidence: high
risk_notes: a strict numeric screen can narrow the field to better-quality candidates, but it does not specify timing, market context, or catalyst quality on its own, so names that pass still need downstream entry and regime filters
notes: this is best stored as a mechanical prefilter that can feed Venu's broader CAN SLIM and O'Neil timing layers; it is narrower and more exact than those frameworks because the post centers on simultaneous threshold enforcement
```

## Example 34: Venu IPO anchored VWAP

Trade master: `Venu`

Original post:

> `How to draw Anchored VWAP in TradingView:`
>
> `- Click on "Indicators" (bottom left).`
>
> `- Search for "Anchored VWAP" and add it to your favorites.`
>
> `- Select Anchored VWAP, then left-click on the IPO date to anchor it.`
>
> `VWAP settings:`
>
> `Band calculation mode: Standard`
>
> `- Bands multiplier #1: 1x (enabled)`
>
> `- Source: Close`
>
> `- VWAP line: Red`
>
> `- Price label: On`
>
> `- All upper/lower deviation bands: Off`
>
> `That will give you a clean IPO VWAP setup.`

Observed context:

- This is a platform-specific indicator-configuration workflow rather than a chart pattern or numeric stock screen
- The key idea is not just `use Anchored VWAP`, but `anchor it at the IPO date`
- The configuration values are explicit and should be preserved as part of the framework rather than treated as cosmetic trivia
- The stated goal is a clean IPO VWAP reference layer that can be used consistently across charts

Normalized strategy:

- `ipo-anchored-vwap-indicator-framework`

Suggested strategy record:

```yaml
trade_master: Venu
strategy_name: ipo-anchored-vwap-indicator-framework
ticker_example: framework
setup_type: TradingView IPO anchored VWAP configuration framework
market_bias: neutral indicator framework
timeframe: anchored from IPO date

pattern_sequence:
  - add Anchored VWAP in TradingView
  - anchor the indicator at the IPO date
  - keep the band-calculation mode on Standard
  - enable only the 1x first band and disable the rest of the upper and lower deviation bands
  - use the resulting IPO-anchored VWAP as a clean chart reference

trigger_conditions:
  - chart has a meaningful IPO date available for anchoring
  - Anchored VWAP is anchored specifically to the IPO date
  - source is set to Close
  - extra deviation bands remain off except for the enabled 1x first band

confirmation_conditions:
  - resulting VWAP reference remains visually clean and uncluttered
  - chart clearly displays the IPO-anchored VWAP line and label
  - same settings can be reused consistently across multiple charts

invalidation_conditions:
  - indicator is anchored to the wrong event or date
  - settings drift away from the specified configuration
  - extra deviation bands are turned on and the clean reference framework is lost

trade_master_terms:
  - Anchored VWAP
  - IPO date
  - Band calculation mode: Standard
  - Bands multiplier #1: 1x
  - Source: Close
  - VWAP line: Red
  - Price label: On
  - all upper/lower deviation bands: Off
  - clean IPO VWAP setup

scan_translation:
  scanner_features_needed:
    - anchored VWAP support tied to a custom historical event
    - event-date anchoring such as IPO date
    - custom indicator-setting persistence
  candidate_rules:
    - if the project supports anchored VWAP, preserve IPO date as the anchor event
    - if the project does not support anchored VWAP, record the gap instead of approximating it with generic VWAP
    - treat this framework primarily as a chart-analysis layer rather than a hard universe screen
  open_questions:
    - whether the user's scanner or charting project can compute anchored VWAP from IPO date directly
    - whether the enabled 1x band is used analytically or simply retained as a minimal visual aid
    - how this IPO VWAP framework should interact with Venu's CAN SLIM and O'Neil timing layers in practice

example_posts:
  - Venu / Anchored VWAP in TradingView / clean IPO VWAP setup

confidence: high
risk_notes: anchored VWAP can create a consistent reference layer, but the setup loses fidelity if the anchor date or settings drift, and by itself it does not define a complete entry or exit rule
notes: this is best stored as a chart-configuration framework that can sit alongside Venu's selection and timing frameworks; the anchor event and exact settings are the main transferable knowledge, not a directional trade call
```

## Example 35: Venu ADR sweet spot

Trade master: `Venu`

Original post:

> `what is ADR? how to use it?`
>
> `ADR (average daily range) measures how much a stock typically moves in a day`
>
> `for example, take LGN - it has an ADR of 5%, which is a sweet spot.`
>
> `generally, I focus on stocks with ADR between 3% and 10%.`
>
> `below 3%`
>
> `these stocks tend to move very slowly`
>
> `above 10%`
>
> `these are very volatile`
>
> `the 3%–10% range offers the best balance`
>
> `ADR doesn’t predict direction - it helps set expectations and manage risk.`

Observed context:

- This is an educational tradability filter, not a direction signal or an entry pattern
- The edge of the post is the preferred operating range: ADR between 3 percent and 10 percent
- The post explicitly defines the tradeoff on both sides of the range: too slow below 3 percent, too unstable above 10 percent
- Venu is using ADR as a practical expectation and risk-planning tool for swing trades

Normalized strategy:

- `adr-volatility-sweet-spot-screen`

Suggested strategy record:

```yaml
trade_master: Venu
strategy_name: adr-volatility-sweet-spot-screen
ticker_example: LGN
setup_type: ADR-based swing-tradability filter
market_bias: neutral selection framework
timeframe: recent daily volatility lookback

pattern_sequence:
  - measure recent average daily range
  - filter out names that move too little to matter for swing trading
  - filter out names that move so much they become hard to manage
  - focus on the middle zone where movement and risk remain balanced

trigger_conditions:
  - ADR between 3 percent and 10 percent
  - stock has enough daily movement to produce meaningful swing opportunities
  - volatility is still manageable for sizing and stop placement

confirmation_conditions:
  - ADR remains in the preferred zone rather than drifting into lethargic or chaotic extremes
  - stock remains tradable with defined risk
  - volatility characteristics fit the intended swing-trading style

invalidation_conditions:
  - ADR drops below 3 percent and the stock becomes too slow
  - ADR rises above 10 percent and the stock becomes too unstable for the intended approach
  - trader can no longer size or manage stops comfortably because volatility regime changed

trade_master_terms:
  - ADR
  - ADR of 5% is a sweet spot
  - ADR between 3% and 10%
  - below 3%
  - above 10%
  - ADR doesn't predict direction

scan_translation:
  scanner_features_needed:
    - ADR or ADR-percent calculation
    - volatility-range filtering
  candidate_rules:
    - prioritize stocks with ADR in the 3 to 10 percent zone
    - down-rank or exclude names below 3 percent ADR for swing-trading workflows
    - down-rank or exclude names above 10 percent ADR when risk becomes too difficult to manage
  open_questions:
    - whether the user's project uses 14-day ADR, 20-day ADR, or another lookback by default
    - whether ADR should be expressed in percent, dollars, or both in the existing scanner
    - whether the 3 to 10 percent range should be a hard filter or a ranking preference

example_posts:
  - Venu / ADR / 3 to 10 percent sweet spot

confidence: high
risk_notes: ADR can improve stock selection and risk planning, but it does not predict direction or replace a timing edge, so stocks inside the sweet spot still need separate entry and exit logic
notes: this works best as an upstream tradability filter that can feed Venu's other selection and timing frameworks
```

## Example 36: Venu ATR extension trim and trail

Trade master: `Venu`

Original post:

> `when to sell?`
>
> `sell into strength using ATR extension`
>
> `when price stretches multiple ATRs above the 50-day SMA (typically 3x ATR)`
>
> `that’s when I trim or sell into strength and wait for a reset`
>
> `sell some into strength - trim and trail`
>
> `once price shows an ATR extension from the 50-day SMA (green dot), sell a partial`
>
> `hold the rest and trail it using the 9-day moving average`
>
> `exit the remaining shares only after a clean close below the 9-day MA`

Observed context:

- This is a trade-management and exit framework for swing trades, not a fresh entry setup
- The first decision point is statistical extension relative to the 50-day SMA, usually around 3 ATRs
- Venu explicitly separates partial profit-taking from final exit
- The framework is designed to lock in gains without forcing an exact top call

Normalized strategy:

- `atr-extension-trim-trail-management`

Suggested strategy record:

```yaml
trade_master: Venu
strategy_name: atr-extension-trim-trail-management
ticker_example: RCAT
setup_type: ATR-extension trim and moving-average trail
market_bias: bullish management framework
timeframe: swing-trade management

pattern_sequence:
  - stock advances strongly away from the 50-day SMA
  - price reaches a statistically extended zone, often around 3 ATRs above the 50-day SMA
  - partial profits are taken into strength rather than waiting for full reversal
  - remaining shares stay in the trend while they continue to hold the 9-day moving average
  - final exit occurs only after a clean close below the 9-day moving average

trigger_conditions:
  - price stretches roughly 3 ATRs above the 50-day SMA
  - stock is extended enough that reward/risk shifts even if the trend remains intact
  - partial position can be trimmed without fully abandoning the trend

confirmation_conditions:
  - extension is visible enough to justify taking some gains
  - remaining shares continue respecting the 9-day moving average
  - trend persists after the trim, validating the trail portion of the process

invalidation_conditions:
  - stock closes cleanly below the 9-day moving average after extension
  - post-extension trend fails quickly enough that the remainder should not be held
  - volatility regime changes so the 3x ATR heuristic no longer reflects a manageable stretch

trade_master_terms:
  - sell into strength
  - ATR extension from the 50-day SMA
  - 3x ATR
  - green dots
  - trim and trail
  - 9-day moving average
  - clean close below the 9-day MA

scan_translation:
  scanner_features_needed:
    - ATR calculation
    - 50-day SMA
    - ATR-percent or ATR-multiple-from-50 calculation
    - 9-day moving average
    - close-below-moving-average detection
  candidate_rules:
    - flag names roughly 3 ATRs above the 50-day SMA as trim candidates
    - separate partial-profit alerts from final-exit alerts
    - keep remainder positions active while the stock continues closing above the 9-day moving average
  open_questions:
    - whether the user's project already has `ATR% multiple from 50-MA` available directly
    - how strict the project should be about `clean close below the 9-day MA`
    - whether partial-trim sizing should be recorded as a fixed fraction or left discretionary

example_posts:
  - Venu / ATR extension / trim and trail

confidence: high
risk_notes: extension-based selling can protect reward/risk when a stock becomes statistically stretched, but selling too aggressively can also cut winners short, which is why the trailing remainder rule is part of the framework
notes: this is a management layer for swing trades and should remain separate from stock-selection and entry frameworks
```

## Example 37: Venu favorite indicator stack

Trade master: `Venu`

Original post:

> `Attaching my list of favorite indicators:`
>
> `3EMA - VictorGrego`
>
> `ATR% multiple from 50-MA - jfsrev`
>
> `Institutional Moving Averages (50/100/...) - Venu_7_`
>
> `Relative Strength Index - built-in`
>
> `Stan Weinstein 30-week Moving Average`
>
> `Swing Data – ADR% / RVol / PVol / Float … - jfsrev`
>
> `Volume - built-in`

Observed context:

- This is a toolkit post that describes Venu's preferred analysis stack rather than a single signal
- The list combines trend references, volatility tools, relative-strength context, and swing-trading dashboards
- Several indicators are tied to specific authors, which is useful for reproducibility
- The stack helps reconstruct the master's charting lens even when no standalone trigger is defined

Normalized strategy:

- `favorite-indicator-stack-framework`

Suggested strategy record:

```yaml
trade_master: Venu
strategy_name: favorite-indicator-stack-framework
ticker_example: framework
setup_type: preferred swing-trading indicator toolkit
market_bias: neutral toolkit framework
timeframe: multi-timeframe chart toolkit

pattern_sequence:
  - use short-term trend references
  - measure extension relative to the 50-day moving average
  - track institutional moving-average structure
  - monitor relative strength and long-term trend context
  - overlay swing-data statistics such as ADR, relative volume, prior volume, and float
  - keep standard price and volume context visible

trigger_conditions:
  - indicator stack is configured and available on the chart
  - tools cover trend, volatility, participation, and tradability dimensions

confirmation_conditions:
  - indicator set gives a consistent lens across swing-trade candidates
  - same indicators can be reused across selection, management, and review workflows

invalidation_conditions:
  - key indicators are unavailable or replaced with materially different tools
  - stack loses reproducibility because the named tools or settings are unclear

trade_master_terms:
  - 3EMA - VictorGrego
  - ATR% multiple from 50-MA - jfsrev
  - Institutional Moving Averages (50/100/...) - Venu_7_
  - Relative Strength Index - built-in
  - Stan Weinstein 30-week Moving Average
  - Swing Data – ADR% / RVol / PVol / Float … - jfsrev
  - Volume - built-in

scan_translation:
  scanner_features_needed:
    - indicator metadata or documentation layer
    - support for ADR, ATR multiple, moving averages, RSI, relative volume, and float metrics
  candidate_rules:
    - treat this as a reusable charting toolkit rather than a hard universe filter
    - prefer reproducing the named tools when the project or platform supports them
    - record gaps explicitly when platform-specific authored indicators are unavailable
  open_questions:
    - which of these authored indicators the user's project can reproduce directly
    - whether any of the listed indicators need a separate settings reference file later
    - which indicators Venu treats as mandatory versus optional in practice

example_posts:
  - Venu / favorite indicators / swing-trading toolkit

confidence: medium
risk_notes: a strong toolkit can improve consistency and context, but indicators do not substitute for a well-defined setup or risk plan, so this stack should support other frameworks rather than replace them
notes: this is best stored as a lens and reproducibility layer that complements Venu's stock-selection, timing, and trade-management frameworks
```

## Example 38: Venu earnings gap 3-day rule

Trade master: `Venu`

Original post:

> `Buying the dip after an earnings gap down is one of the most common mistakes traders/investors make.`
>
> `Most people rush in thinking they’re getting a "discount." Institutions don’t.`
>
> `This is where the 3-day rule comes in.`
>
> `The 3-day rule for earnings means waiting at least three trading days after a major earnings move, especially a gap down.`
>
> `Large funds need time to digest earnings, adjust exposure, and distribute shares.`
>
> `Early dip buyers often end up catching a falling knife while institutions are still exiting.`
>
> `The goal is not to react. Let price and volume tell the story.`
>
> `My focus is always on gap-up stocks with strong earnings and strong demand, not weak names trying to bounce.`
>
> `Every earnings season, I update my Power Earnings Gap watchlist. That’s where leadership comes from.`

Observed context:

- This is a catalyst-specific participation rule, not a generic dip-buying lesson
- The rule is asymmetric: Venu explicitly avoids weak earnings gap-down bounces and prefers strong earnings gap-ups
- The waiting period is part of the method, not a vague suggestion; at least three trading days are required after a major earnings move, especially a gap down
- The framework treats institutions as the real pacing mechanism, with price and volume used to confirm whether damage is real or merely emotional

Normalized strategy:

- `earnings-gap-3-day-rule-framework`

Suggested strategy record:

```yaml
trade_master: Venu
strategy_name: earnings-gap-3-day-rule-framework
ticker_example: framework
setup_type: post-earnings waiting rule and leadership filter
market_bias: bullish participation framework
timeframe: first three trading days after earnings

pattern_sequence:
  - stock makes a major earnings move, especially a gap down
  - avoid immediate dip-buying while institutional digestion and distribution may still be underway
  - wait at least three trading days for volatility to settle
  - let price and volume reveal whether damage is real or whether demand can actually stabilize
  - prefer to shift focus toward gap-up stocks with strong earnings and strong demand instead of weak bounce attempts

trigger_conditions:
  - major earnings move has just occurred
  - if the move is a gap down, do not treat the apparent discount as a buy signal
  - wait at least three trading days before evaluating whether the chart deserves attention

confirmation_conditions:
  - price and volume begin to show a clearer post-earnings character after the waiting period
  - institutional selling pressure appears to have settled rather than remaining active
  - strong earnings gap-ups and Power Earnings Gap names continue to show demand and leadership traits

invalidation_conditions:
  - early dip buying occurs before the waiting period and the stock continues lower
  - post-earnings action keeps showing distribution instead of demand
  - stock remains a weak bounce candidate rather than evolving into a true leadership name

trade_master_terms:
  - buying the dip after an earnings gap down is one of the most common mistakes
  - discount
  - institutions don't
  - 3-day rule
  - catching a falling knife
  - let price and volume tell the story
  - gap-up stocks with strong earnings and strong demand
  - Power Earnings Gap watchlist
  - that's where leadership comes from

scan_translation:
  scanner_features_needed:
    - earnings-event tagging
    - gap-up and gap-down detection
    - trading-day counting after earnings
    - post-event price and volume behavior tracking
    - earnings-gap watchlist support
  candidate_rules:
    - suppress or down-rank fresh earnings gap-down dip buys during the first three trading days
    - re-evaluate only after the waiting window has passed and price-volume behavior improves
    - prioritize earnings gap-ups with strong demand for leadership watchlists
  open_questions:
    - how the user's project identifies a `major earnings move`
    - whether the three-day rule should be a hard block or a severe ranking penalty
    - how Power Earnings Gap names are defined operationally in the existing workflow

example_posts:
  - Venu / 3-day rule / avoid earnings gap-down dip buys and focus on strong earnings gap-ups

confidence: high
risk_notes: waiting rules can reduce the odds of buying into unresolved institutional distribution, but they may also delay re-entry into rare fast recoveries, so the edge comes from avoiding weak reflex bounces rather than catching every reversal
notes: this is best stored as a post-earnings participation filter that complements Venu's leadership-first orientation; the preferred positive focus remains strong earnings gap-ups rather than reactive buying in damaged names
```

## Example 39: Venu Power Earnings Gap / Episodic Pivot

Trade master: `Venu`

Original post:

> `Power Earnings Gap (PEG) setups also called Episodic Pivots (EP) are among the highest success-rate setups in bull markets.`
>
> `A PEG forms when:`
>
> `- A stock gaps up on strong earnings`
>
> `- The gap holds (no immediate fill)`
>
> `- Volume is significantly above average`
>
> `- Clear institutional accumulation is present`
>
> `This signals a potential character change.`
>
> `How to trade it:`
>
> `- The low of the PEG candle defines your risk.`
>
> `- As long as the gap holds, the trend remains intact.`
>
> `In strong markets, PEG setups often lead the next expansion leg.`
>
> `Many will assume the trend is extended. But in true Stage 2 advances, the move doesn’t end until you see clear distribution - heavy sell volume meaningfully above the 30-day average.`

Observed context:

- This is a bullish post-earnings continuation setup, distinct from Venu's separate rule about avoiding weak earnings gap-down dip buys
- The setup requires strong earnings, a gap up that does not fill, volume confirmation, and visible institutional demand
- The setup has a precise initial risk reference: the low of the PEG candle
- Venu links repeated PEG signals in the same stock to an ongoing Stage 2 trend rather than assuming the move is over just because the stock appears extended
- When price does not offer the initial PEG-low entry cleanly, Venu prefers patience for either a controlled retest or a pullback into the 9/21-day EMA zone

Normalized strategy:

- `power-earnings-gap-episodic-pivot`

Suggested strategy record:

```yaml
trade_master: Venu
strategy_name: power-earnings-gap-episodic-pivot
ticker_example: TER
setup_type: earnings gap-up institutional continuation setup
market_bias: bullish
timeframe: earnings event into Stage 2 continuation

pattern_sequence:
  - stock reports strong earnings and gaps up sharply
  - gap holds instead of filling immediately
  - volume expands well above normal and implies institutional accumulation
  - post-earnings action marks a character change into leadership behavior
  - initial advance can continue directly or reset through a controlled retest before the next expansion leg

trigger_conditions:
  - strong earnings-driven gap up
  - gap remains open and constructive rather than filling immediately
  - volume is significantly above average
  - clear signs of institutional accumulation are present

confirmation_conditions:
  - PEG low continues to hold as support
  - trend persists in a Stage 2 advance rather than showing clear distribution
  - later pullbacks hold constructively, including possible support at the 9/21-day EMA zone

invalidation_conditions:
  - low of the PEG candle fails
  - gap fills quickly enough to negate the institutional-strength message
  - heavy sell volume meaningfully above the 30-day average signals distribution and trend deterioration

trade_master_terms:
  - Power Earnings Gap
  - Episodic Pivot
  - gap holds
  - clear institutional accumulation
  - potential character change
  - low of the PEG candle defines your risk
  - Stage 2 trend
  - Phase 3 of a Stage 2 uptrend
  - 9/21-day EMA zone
  - clear distribution

scan_translation:
  scanner_features_needed:
    - earnings-event tagging
    - gap-up detection
    - no-immediate-fill or gap-hold detection
    - volume expansion relative to average
    - institutional-accumulation proxy
    - 9-day and 21-day EMA support tracking
    - abnormal sell-volume versus 30-day average detection
  candidate_rules:
    - prioritize earnings gap-ups that hold their gap and print large volume
    - set initial risk off the PEG-candle low
    - allow continuation candidates to remain valid while the gap and Stage 2 structure hold
    - prefer patient entries on controlled retests or 9/21-day EMA pullbacks when immediate entry is gone
    - invalidate when heavy distribution appears rather than merely because price looks extended
  open_questions:
    - how the user's project will approximate `clear institutional accumulation`
    - whether PEG names should be tracked as a dedicated watchlist bucket separate from other earnings-gap names
    - how strict the project should be about defining a filled gap versus a harmless intraday shakeout

example_posts:
  - Venu / TER / clean PEG around July 30, 2025 leading to continuation
  - Venu / TER / PEG around October 28, 2025 followed by reclaim and continuation
  - Venu / TER / third PEG candle with patience for PEG-low retest or 9/21-day EMA pullback

confidence: high
risk_notes: PEG setups can be among the strongest continuation patterns when earnings demand is real, but the setup loses its edge quickly if the gap fails or if clear institutional distribution replaces accumulation
notes: this should sit alongside Venu's 3-day earnings rule as the positive asymmetric counterpart: avoid weak earnings-gap-down dip buys, but aggressively study strong earnings gap-ups that hold and attract institutional demand
```

## Example 40: Venu FocusList pipeline

Trade master: `Venu`

Original post:

> `Strategy Overview:`
>
> `Identify PEG Stocks: Use strong earnings reports to find stocks displaying "Power Earnings Gap" candles and add them to the PEG list.`
>
> `Identify Thematic Stocks: Identify hidden gems and strong themes, particularly within the semiconductor sector, and add them to the Semi watchlist.`
>
> `Create FocusList: Perform fundamental and technical analysis on stocks from the PEG and Semi lists to select the most promising names for the FocusList.`
>
> `Inside the FocusList:`
>
> `Watchlist A: Contains strong names based on robust technicals (significant accumulation, large bases) and fundamentally growing companies (good fundamentals and institutional backing).`
>
> `Watchlist B: Consists of names that are currently considered extended in their price action.`

Observed context:

- This is a watchlist-construction workflow rather than a single chart setup or stock screen
- The process starts with two discovery funnels: earnings-gap leaders and thematic semiconductor names
- The FocusList acts as a higher-conviction ranking layer built from both fundamental and technical review
- The final split between `Watchlist A` and `Watchlist B` is based on actionability: high-quality names versus interesting but currently extended names

Normalized strategy:

- `focuslist-watchlist-pipeline-framework`

Suggested strategy record:

```yaml
trade_master: Venu
strategy_name: focuslist-watchlist-pipeline-framework
ticker_example: framework
setup_type: watchlist funnel and ranking workflow
market_bias: bullish workflow framework
timeframe: ongoing candidate pipeline

pattern_sequence:
  - source candidates from Power Earnings Gap names after strong earnings
  - source additional candidates from strong themes and hidden gems, especially semiconductors
  - review both discovery pools through combined fundamental and technical analysis
  - promote the strongest candidates into a FocusList
  - split the FocusList into actionable strength names and extended-but-interesting names

trigger_conditions:
  - stock qualifies for PEG list because it printed a valid Power Earnings Gap
  - or stock qualifies for the thematic list because it fits a strong theme such as semiconductors
  - combined technical and fundamental review supports promotion into the FocusList

confirmation_conditions:
  - Watchlist A names show significant accumulation, large constructive bases, and strong fundamentals or institutional backing
  - Watchlist B names remain attractive overall but are too extended for immediate action
  - the funnel continues surfacing leadership candidates rather than random isolated names

invalidation_conditions:
  - candidate fails later technical or fundamental review and no longer deserves FocusList status
  - apparent leadership name loses accumulation support or thematic relevance
  - extended name in Watchlist B deteriorates instead of resetting into a healthier opportunity

trade_master_terms:
  - PEG list
  - Semi watchlist
  - FocusList
  - Watchlist A
  - Watchlist B
  - hidden gems
  - strong themes
  - significant accumulation
  - large bases
  - fundamentally growing companies
  - institutional backing
  - extended in price action

scan_translation:
  scanner_features_needed:
    - PEG or earnings-gap candidate tagging
    - thematic or sector tagging, especially semiconductors
    - fundamental ranking inputs
    - technical ranking inputs
    - watchlist bucket assignment
  candidate_rules:
    - collect valid PEG names into one discovery bucket
    - collect thematic semiconductor or hidden-gem names into another discovery bucket
    - rank combined candidates on both technical quality and fundamental strength before promotion to FocusList
    - separate actionable strength from extended names at the final stage
  open_questions:
    - how the user's workflow wants to define a `hidden gem`
    - which exact technical and fundamental fields should determine FocusList promotion
    - whether Watchlist B names should be revisited on pullbacks automatically or manually

example_posts:
  - Venu / strategy overview / PEG list, Semi watchlist, FocusList, Watchlist A, Watchlist B

confidence: high
risk_notes: structured watchlist funnels can improve focus and consistency, but they still depend on disciplined promotion criteria, so loose standards can turn the pipeline into clutter instead of edge
notes: this workflow should sit above Venu's individual setups and management rules, because it describes how candidates are sourced, ranked, and staged before actual trade execution
```
