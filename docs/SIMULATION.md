# Simulation Guide

## Clearance & fit (always)
Use `trimesh` or CadQuery boolean checks:
- Shaft in bore: designed clearance vs measured printer shrinkage.
- Bearing press fit: coupon-derived interference.
- Magnet pocket: XY + depth oversize.
- Fastener clearance: M3 3.4, M4 4.3 (tune per printer).

## FEA (when loads matter)
- Rotors under magnet attraction (pinch force).
- Crank arms under torque.
- Base posts under bearing load.
- Tooling: CalculiX via CadQuery, or export mesh → external solver.
- Report: max stress, max deflection, safety factor, mesh info.

## Multi-part assemblies (generators etc.)
- One master `parameters.py` for the whole build.
- Simulate the full stack: air gaps, coil-to-magnet alignment, total height.
- Verify no part can bind or collide in any assembly state.

## Output format
`SIM_REPORT.md` in the project folder:
```
# SIM REPORT — <project> <date>
| Check | Expected | Actual | Status |
| Fit coupon shaft | 0.35 mm slip | 0.34 mm | PASS |
| ... | ... | ... | ... |
Safety factor: 3.1 (rotor) — PASS
```
