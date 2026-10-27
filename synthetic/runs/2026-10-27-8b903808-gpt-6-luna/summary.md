SYNTHETIC: built from synthetic grades or the shim backend; no number here is a finding about paperweight.
# Calibration run: 2026-10-27-8b903808-gpt-6-luna

Mode full · model gpt-6-luna · repeats 3 · prompt 8b903808b5c5

## Calibration (8 papers)

| Metric | Value (95% interval) |
| --- | --- |
| Bias | +1.58 (-0.72 to +4.08) |
| MAE | 3.05 (1.65 to 4.71) |
| Correlation | -0.75 (-0.99 to -0.12) |
| Reviewer ceiling | 0.83 (0.42 to 0.98) |
| Band agreement | 2 of 8 |

| Criterion | Bias (95% interval) | Grade 2, paperweight | Grade 2, reviewers |
| --- | --- | --- | --- |
| motivation | +0.55 (+0.19 to +0.88) | 22 of 24 | 10 of 24 |
| audience | +0.47 (-0.04 to +0.99) | 4 of 24 | 3 of 24 |
| prior_art | +0.56 (+0.18 to +0.94) | 17 of 24 | 11 of 24 |
| vehicle | +0.24 (-0.40 to +0.90) | 0 of 24 | 1 of 24 |
| coordination | -0.08 (-0.61 to +0.44) | 0 of 24 | 2 of 24 |
| insufficiency | -0.01 (-0.61 to +0.56) | 0 of 24 | 2 of 24 |
| implementation | -0.15 (-0.90 to +0.54) | 16 of 24 | 17 of 24 |

Stability: sigma 0.49, same exact 2 of 24, same integer 11 of 24, same band 20 of 24, spans nested 22 of 24

| Paper | Total | Band | Reviewers | Reviewers' band |
| --- | --- | --- | --- | --- |
| P0533R9 | 8.11 | Heavy | 6.33 | Medium |
| P0957R8 | 8.55 | Heavy | 6.33 | Medium |
| P1068R11 | 10.17 | Heavy | 4.33 | Medium |
| P1122R3 | 6.61 | Medium | 9.33 | Heavy |
| P2040R0 | 7.00 | Medium | 8.00 | Heavy |
| P3290R4 | 11.28 | Heavy | 3.67 | Medium |
| P3953R0 | 4.50 | Medium | 6.67 | Medium |
| P3978R0 | 7.39 | Medium | 6.33 | Medium |

## Holdout (1 papers)

| Metric | Value (95% interval) |
| --- | --- |
| Bias | +0.50 (+0.50 to +0.50) |
| MAE | 0.50 (0.50 to 0.50) |
| Correlation | n/a (n/a to n/a) |
| Reviewer ceiling | n/a (n/a to n/a) |
| Band agreement | 1 of 1 |

| Criterion | Bias (95% interval) | Grade 2, paperweight | Grade 2, reviewers |
| --- | --- | --- | --- |
| motivation | +0.61 (+0.61 to +0.61) | 0 of 3 | 0 of 3 |
| audience | +0.22 (+0.22 to +0.22) | 0 of 3 | 0 of 3 |
| prior_art | +1.00 (+1.00 to +1.00) | 1 of 3 | 0 of 3 |
| vehicle | -0.44 (-0.44 to -0.44) | 0 of 3 | 1 of 3 |
| coordination | -0.67 (-0.67 to -0.67) | 0 of 3 | 0 of 3 |
| insufficiency | +0.00 (+0.00 to +0.00) | 0 of 3 | 0 of 3 |
| implementation | -0.22 (-0.22 to -0.22) | 0 of 3 | 0 of 3 |

Stability: sigma 0.60, same exact 0 of 3, same integer 1 of 3, same band 3 of 3, spans nested 3 of 3

| Paper | Total | Band | Reviewers | Reviewers' band |
| --- | --- | --- | --- | --- |
| P4228R0 | 4.17 | Medium | 3.67 | Medium |

## Health

Runs 36, failed 0, incomplete 0, replies missing 0, quotes rejected 315, NOT_PROPOSAL 6, model calls 6351, wall time 438.3s, sample agreement 92%.

Left out: P3411R5 (triaged NOT_PROPOSAL), P3556R0 (triaged NOT_PROPOSAL), P4020R0 (triaged NOT_PROPOSAL)
