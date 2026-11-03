# Five-Minute Code-and-Results Demonstration (Gate G4)

**0:00–0:40 — Research question**  
Explain the question: whether an explicit publication-date boundary instruction reduces post-cutoff citations in LLM-generated literature reviews. State the inclusive cutoff: 2024-12-31.

**0:40–1:30 — Design**  
Show the prompt protocol and ten retained outputs. Explain A (standard prompt), B (same prompt plus cutoff instruction), five matched pairs, and manual ChatGPT UI generation. Mention the documented review-length deviation.

**1:30–2:30 — Data and audit**  
Open `data/citation_extraction_v3.csv` and `data/final_consolidated_reference_audit.csv`. Explain the 100 candidates / 99 analyzed references distinction and the manual audit categories. Emphasize that a DOI 404 is not proof of fabrication.

**2:30–3:40 — Reproduce the analysis live**  
From the `experiment/` directory run:

```bash
python -m pip install -r requirements.txt
python scripts/reproduce_analysis.py
```

Show the generated `results/reproduced/REPRODUCTION_RUN_REPORT.md`, CSV outputs, and figures. State clearly that this re-runs analysis of archived CSVs, not the original LLM generations.

**3:40–4:30 — Findings and limitations**  
A: 15/51 post-cutoff (29.41%); B: 0/48 (0%). Mean paired reduction: 29.64 percentage points. Exact two-sided sign test p=0.0625; not significant at 0.05. MATCH-only sensitivity mean reduction: 27.14 percentage points. Discuss small sample, one interface/model configuration, and bibliographic uncertainty.

**4:30–5:00 — Contribution and accountability**  
State that the contribution is a controlled prompt comparison, not a new model architecture. Explain the AI assistance log, what was checked by code, what still needs human verification, and why the experiment does not measure the model's internal training cutoff.
