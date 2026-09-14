# Generators (parametric port)

Migrating the OpenSCAD builds from the sibling `generators` repo into CadQuery + simulation.

Current OpenSCAD sources & STLs remain in `lucidlooney2030/generators`.
This folder will host:
- `parameters.py` (ported from `scad/parameters.scad`)
- CadQuery part scripts
- `simulate.py` with FEA for rotor pinch, crank torque, stack verification
- Fit-coupon workflow

Start here: copy `projects/_template` and port v2 parameters first.
