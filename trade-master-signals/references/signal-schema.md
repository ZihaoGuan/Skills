# Signal Schema

Use this schema for any strategy or signal record derived from a trade master's post. Keep it structured enough for later scanner integration, but avoid inventing precision the source material does not support.

## Required fields

```yaml
trade_master:
strategy_name:
setup_type:
market_bias:
timeframe:
confidence:
```

## Recommended fields

```yaml
trade_master:
strategy_name:
ticker_example:
setup_type:
market_bias:
timeframe:

pattern_sequence:
  - ordered event
  - ordered event

trigger_conditions:
  - condition

confirmation_conditions:
  - condition

invalidation_conditions:
  - condition

catalyst_context:
  catalyst:
  timing:
  edge_logic:

position_sizing:
  single_name_limit:
  typical_size:
  basket_limit:
  conviction_overweights:
    - rule

management_framework:
  entry_tactics:
    - tactic
  exit_scenarios:
    - scenario
  event_day_rules:
    - rule
  reassessment_timing:
    - rule

trade_master_terms:
  - original phrase

scan_translation:
  scanner_features_needed:
    - feature
  candidate_rules:
    - rule
  open_questions:
    - question

example_posts:
  - short label or link

confidence:
risk_notes:
notes:
```

## Field guidance

- `strategy_name`
Use lowercase hyphenated names that describe the pattern, not the ticker.

- `pattern_sequence`
Capture the order of events. This is often the most portable part of the setup.

- `trigger_conditions`
Record the minimum conditions needed to consider the setup active.

- `confirmation_conditions`
Record optional evidence that strengthens conviction but may not be mandatory.

- `invalidation_conditions`
Record what would make the setup fail or no longer qualify.

- `catalyst_context`
Use this when the post is organized around a catalyst such as earnings, not just around chart structure. Preserve the event, the timing window, and why the master believes the asymmetric edge exists.

- `position_sizing`
Use this when the master gives capital-allocation rules. Keep exact single-name caps, typical sizing bands, basket limits, and any conviction-overweight guidance.

- `management_framework`
Use this when the post teaches execution after entry rather than only the trigger. Preserve entry tactics, scenario-based exits, event-day behavior, and when thesis re-evaluation is allowed.

- `trade_master_terms`
Preserve the author's words so the skill can learn each master's vocabulary over time.

- `scan_translation`
Keep this implementation-aware but scanner-agnostic until the user's project is known.

- `confidence`
Use `low`, `medium`, or `high`.
`high` should be rare unless the source is explicit and repeated across examples.
