"""Run clearance + FEA checks. Writes SIM_REPORT.md."""
# TODO: implement fit coupon, clearance matrix, stack height, stress.
# For now a stub that always passes so the pipeline is testable.

REPORT = """# SIM REPORT — template
| Check | Status |
| Fit coupon | SKIP (stub) |
| Clearance matrix | SKIP (stub) |
| Stack height | SKIP (stub) |
| Stress | SKIP (stub) |
All checks: PASS (stub)
"""

with open("SIM_REPORT.md", "w") as f:
    f.write(REPORT)
print(REPORT)
