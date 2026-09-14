"""Shared parameters for <project>. All dimensions in mm."""

# --- Printer / FDM assumptions ---
NOZZLE = 0.4
LAYER = 0.2
WALL = 1.6                 # load-bearing ~4 perimeters
CLEARANCE_SLIP = 0.35      # shaft slip fit
CLEARANCE_LOOSE = 0.55
PRESS_INTERFERENCE = 0.15   # bearing pocket undersize (coupon-test)
ELEPHANT_FOOT = 0.5

# --- Purchased parts ---
# e.g. MAGNET_D = 20; MAGNET_H = 3; BEARING_OD = 22; SHAFT_D = 8

# --- Geometry ---
# every dimension a named constant; no magic numbers in part scripts

# --- Fasteners ---
M3_CLEAR = 3.4
M4_CLEAR = 4.3
