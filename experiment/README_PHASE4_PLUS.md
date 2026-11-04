# Phase IV–VI Completion Addendum

This addendum extends the existing experiment release without changing its existing folder layout or replacing the original study files.

## What was added

- `scripts/reproduce_analysis.py` — reproducible analysis of the archived CSV tables.
- `requirements.txt` and `configs/analysis_config.json` — minimal dependencies and frozen analysis settings.
- `results/reproduced/` — generated CSV outputs, figures, and an execution report from a successful run in the preparation environment.
- `docs/phase4_contribution_and_evidence.md` — selected pathway, contribution, results, deeper analysis, and threats to validity.
- `docs/baseline_validation.md` — honest comparator/baseline validation status.
- `docs/peer_review_and_revision_log.md` — internal technical review and remaining revisions.
- `docs/ai_assistance_log.md` — evidence-based AI assistance record with researcher completion fields.
- `docs/five_minute_demo_script.md` — Gate G4 demonstration script.
- `paper/experimental_study.tex` and compiled `paper/experimental_study.pdf` — a LaTeX manuscript source draft and its successful compilation.
- `paper/references_review_background.bib` — bibliography file retained from the earlier literature-review project; it is not yet fully reconciled to citations in the experimental manuscript.

## Reproduce the analysis

From this directory:

```bash
python -m pip install -r requirements.txt
python scripts/reproduce_analysis.py
```

The script reads the CSV files under `data/`, validates key counts, recomputes the descriptive summary and paired sign-test result, and writes generated outputs to `results/reproduced/`.

**Scope warning:** this command re-analyses archived CSVs. It does not regenerate the original ten ChatGPT UI reviews, reproduce their generation timestamps/settings, or independently re-audit each bibliographic record.

## Current results (from archived data)

- A: 15/51 post-cutoff citation instances = 29.41%.
- B: 0/48 = 0.00%.
- Mean paired reduction: 29.64 percentage points.
- Exact two-sided sign test: p=0.0625 (not significant at alpha=0.05).
- MATCH-only sensitivity mean paired reduction: 27.14 percentage points.

The study evaluates observable compliance with a publication-date instruction, not the model's internal training-data cutoff.

## Researcher actions still required before submission

1. Verify the original UI generation log, model label, visible settings, timestamps, and randomized order from authentic records.
2. Personally spot-check the source records and publication versions for the bibliography, especially partial matches and preprint/proceedings cases.
3. Re-run the script in the target Colab or local environment and retain that environment's real output.
4. Compile the LaTeX source after reconciling every manuscript claim, citation, bibliography entry, and figure against the final paper. The included source is a 5-page draft, not yet the assignment's recommended 6–10-page target.
5. Add actual commit hashes and the full prompt/code history to the AI log. Do not invent debugging examples if none were recorded.
6. Upload the new files into the existing GitHub `experiment/` folder and test every link from GitHub.

No claim is made that these remaining human checks have already been completed.
