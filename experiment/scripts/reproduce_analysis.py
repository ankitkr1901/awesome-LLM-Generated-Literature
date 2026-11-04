#!/usr/bin/env python3
"""Reproduce descriptive tables and figures from the archived study CSVs.
Run from the experiment directory: python scripts/reproduce_analysis.py
This script re-analyses supplied CSV data; it does not regenerate LLM outputs.
"""
from pathlib import Path
import math
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "results" / "reproduced"
OUT.mkdir(parents=True, exist_ok=True)

summary = pd.read_csv(DATA / "final_condition_summary.csv")
pairs = pd.read_csv(DATA / "paired_condition_comparison.csv")
sens = pd.read_csv(DATA / "sensitivity_analysis.csv")
audit = pd.read_csv(DATA / "final_consolidated_reference_audit.csv")

required = {"condition", "citation_instances", "within_cutoff", "post_cutoff", "unknown_date", "matched", "post_cutoff_rate", "bibliographic_match_rate"}
assert required.issubset(summary.columns), f"Missing summary columns: {required-set(summary.columns)}"
assert set(summary.condition) == {"A", "B"}
assert len(pairs) == 5 and pairs.pair_id.nunique() == 5
assert len(audit) == 99, f"Expected 99 analyzed reference instances; found {len(audit)}"

A = summary.set_index("condition").loc["A"]
B = summary.set_index("condition").loc["B"]
assert int(A.citation_instances) == 51 and int(A.post_cutoff) == 15
assert int(B.citation_instances) == 48 and int(B.post_cutoff) == 0
assert math.isclose(float(A.post_cutoff_rate), 15/51, rel_tol=1e-8)
assert math.isclose(float(B.post_cutoff_rate), 0.0, abs_tol=1e-12)

# Descriptive paired estimate from the frozen paired comparison table.
mean_reduction = pairs.rate_reduction_A_minus_B.mean() * 100
# Exact two-sided sign test: all five non-tied pairs point in the same direction.
n = int((pairs.rate_reduction_A_minus_B != 0).sum())
positive = int((pairs.rate_reduction_A_minus_B > 0).sum())
p_sign = min(1.0, 2 * sum(math.comb(n, k) for k in range(positive, n+1)) / (2**n))

summary_out = summary.copy()
summary_out.to_csv(OUT / "condition_summary_reproduced.csv", index=False)
pairs.assign(rate_reduction_pp=pairs.rate_reduction_A_minus_B*100).to_csv(OUT / "paired_comparison_reproduced.csv", index=False)
sens.assign(reduction_pp=sens.reduction_A_minus_B*100).to_csv(OUT / "sensitivity_reproduced.csv", index=False)

# Recreate a compact overall figure.
fig, ax = plt.subplots(figsize=(6.4, 4.2))
ax.bar(summary.condition, summary.post_cutoff_rate*100)
ax.set_ylabel("Post-cutoff citation instances (%)")
ax.set_xlabel("Prompt condition")
ax.set_title("Post-cutoff citation rate by condition")
ax.set_ylim(0, max(35, float(summary.post_cutoff_rate.max()*100+5)))
fig.tight_layout(); fig.savefig(OUT / "overall_cutoff_rate_reproduced.png", dpi=200); plt.close(fig)

fig, ax = plt.subplots(figsize=(7, 4.5))
x = range(len(pairs))
ax.plot(x, pairs.post_cutoff_rate_A*100, marker="o", label="A: standard")
ax.plot(x, pairs.post_cutoff_rate_B*100, marker="o", label="B: explicit cutoff")
ax.set_xticks(list(x), pairs.pair_id)
ax.set_ylabel("Post-cutoff citation rate (%)")
ax.set_xlabel("Matched pair")
ax.set_title("Paired comparison")
ax.legend(); fig.tight_layout(); fig.savefig(OUT / "paired_comparison_reproduced.png", dpi=200); plt.close(fig)

report = f'''# Reproduction run report\n\n- Run status: PASS\n- Input: archived CSV files under `data/`\n- References audited: {len(audit)}\n- Condition A: {int(A.post_cutoff)}/{int(A.citation_instances)} post-cutoff ({A.post_cutoff_rate*100:.2f}%)\n- Condition B: {int(B.post_cutoff)}/{int(B.citation_instances)} post-cutoff ({B.post_cutoff_rate*100:.2f}%)\n- Mean paired reduction: {mean_reduction:.2f} percentage points\n- Exact two-sided sign test: n={n}, positive pairs={positive}, p={p_sign:.4f}\n\nThis verifies that the supplied analysis tables can be read and their principal descriptive results recomputed. It does not reproduce the original ChatGPT generations, independently re-audit every citation, or establish the correctness of the source CSV classifications.\n'''
(OUT / "REPRODUCTION_RUN_REPORT.md").write_text(report, encoding="utf-8")
print(report)
print(f"Outputs written to: {OUT}")
