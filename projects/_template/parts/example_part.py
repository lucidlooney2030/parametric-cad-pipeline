"""Example part module. Import parameters; return a CadQuery solid."""
import cadquery as cq
from .. import parameters as P

def build():
    # TODO: replace with real geometry using P.* only
    return (cq.Workplane("XY")
            .box(10, 10, 5)
            .edges(">Z")
            .fillet(1))

def export_stl(path="example_part.stl"):
    cq.exporters.export(build(), path)
    return path
