"""Regenerate all STLs from current parameters."""
from .parts.example_part import export_stl
import os

os.makedirs("stl", exist_ok=True)
export_stl("stl/example_part.stl")
print("Exported stl/example_part.stl")
