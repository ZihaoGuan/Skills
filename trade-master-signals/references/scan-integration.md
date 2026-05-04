# Scan Integration

Use this file to map normalized strategies into the user's existing market-scanning project.

## Goal

Keep strategy logic independent from implementation details, then translate only the parts the scanner can actually express.

## Integration workflow

1. Inspect the scanner project and find:
- the entrypoint command
- supported indicators and price-pattern primitives
- how the project defines universes, filters, and outputs
- any existing naming or schema conventions

2. For each strategy, create a translation table:

```yaml
strategy_name:
scanner_component:
supported_fields:
unsupported_fields:
approximation_notes:
```

3. Prefer direct mappings:
- moving averages -> existing MA fields
- breakout above range high -> existing breakout or pivot logic
- volume confirmation -> existing relative-volume or average-volume logic

4. Record gaps explicitly.
If the scanner cannot represent a concept such as "constructive squat," write down the approximation or missing capability.

## Current status

The user's scanner project has not yet been attached to this skill. Until it is available:

- avoid hardcoding thresholds
- avoid inventing a query language
- keep `scan_translation` at the concept level
