# Pipeline Specification

This is the contract every project in this repo must follow. Deviations require a note in the project's `DEBRIEF.md`.

## Stages

### 1. Idea (`IDEA.md`)
- One paragraph: what it is, why, success criteria.
- Constraints: printer, material, load, safety.
- Explicit non-claims (e.g. "not free energy").

### 2. Parameters (`parameters.py`)
- Every dimension a named constant with units in a comment.
- Grouped: printer assumptions, purchased parts, geometry, clearances, fasteners.
- No geometry code may hardcode a number that belongs here.

### 3. Geometry (`parts/*.py`)
- One module per printable part.
- Import `parameters` only; no cross-imports between parts except via params.
- Functions return CadQuery solids; `export_stl(path)` writes binary STL.
- Filenames stable: `rotor_disc_A.py` → `rotor_disc_A.stl`.

### 4. Simulation (`simulate.py`)
Mandatory checks before any STL is considered print-ready:
- **Fit coupon**: shaft, bearing, magnet, fastener clearances in the target material.
- **Clearance matrix**: every mating pair checked for interference / min gap.
- **Stack height**: axial assemblies sum to target within tolerance.
- **Stress** (where relevant): FEA or hand calc with stated assumptions; flag if safety factor < 2.
- Output: `SIM_REPORT.md` with pass/fail per check and the numbers.

### 5. Export (`export.py`)
- Regenerates all STLs from current params.
- Writes `MANIFEST.md` listing every file + sha256.
- Never commit a hand-tweaked STL.

### 6. Debrief (`DEBRIEF.md`)
- What was measured vs predicted.
- Failures and fixes (the gold that stops repetition).
- Lessons for the next build.

## Versioning
- One git commit per meaningful param or geometry change.
- Tag releases: `v1.0-afpm-desk` etc.
- Breaking param changes bump minor version and note migration in DEBRIEF.
