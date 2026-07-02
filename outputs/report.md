# NimbusAI — GPU Cost Optimization Report

**Period:** monthly  
**Baseline spend:** $27,133  
**Optimized spend:** $14,626  
**Projected savings:** $12,507  (**46%**)

## Savings by lever

| Lever | Savings (USD) |
|---|---|
| Inference (cascade/cache/batch) | $1,212 |
| Purchasing (spot/reserved) | $10,040 |
| Right-size util-lies | $655 |
| Kill idle GPUs | $600 |

## Sustainability

- Energy per query: 0.24 Wh
- Carbon per query: 0.091 gCO2e
- Cheapest+cleanest region: europe-north1

_Figures are June-2026 as-of snapshots; re-baseline before acting._

## Extension Results

### Cache economics
- Assumed reads per cached prefix: 3.0
- Assumed write cost per million units: 1.0
- Read discount: 0.1
- Cache worth it? True
- Effective cache savings: $2.44

### Reasoning budget
- Reasoning traffic share: 16.5%
- Reasoning cost share: 16.5%
- Estimated reasoning energy: 29787.74 Wh
- 10% cap avoidable spend: $1.26
- 10% cap avoidable energy: 26808.97 Wh