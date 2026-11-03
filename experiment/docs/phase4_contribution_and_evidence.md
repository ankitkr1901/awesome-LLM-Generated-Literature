# Phase IV — Contribution and Evidence (Prompt 12–14)

## 1. Selected contribution pathway

**Selected pathway: B — controlled comparative study.** This matches the assignment's approved pathway on page 2: compare relevant methods under a common protocol with fair controls, consistent metrics, and failure/trade-off analysis.

The study compares two prompt conditions rather than two trained ML architectures:
- **A:** standard literature-review prompt.
- **B:** same base task with an explicit instruction to include only scholarly works published on or before 2024-12-31 (inclusive), and to omit or flag uncertain dates rather than guess.

This is a valid domain-appropriate comparison for an LLM/HCI-style study. A conventional algorithmic baseline is not applicable because the intervention itself is a prompt-level control. Condition A is the control comparator; Condition B is the treatment condition.

## 2. Evidence and observed outcomes

| Outcome | A | B |
|---|---:|---:|
| Citation instances | 51 | 48 |
| Within cutoff | 36 | 48 |
| Post cutoff | 15 | 0 |
| Post-cutoff rate | 29.41% | 0.00% |
| MATCH entries | 45 | 48 |
| Bibliographic match rate | 88.24% | 100.00% |

Five matched pairs were used. The mean paired reduction was 29.64 percentage points; all five pairs favoured B. The exact two-sided sign test gives p=0.0625, so the result does not cross the conventional 0.05 threshold. Interpret as a consistent descriptive pattern in a small sample, not a definitive general effect.

## 3. Deeper analysis

The study includes a sensitivity analysis restricted to references classified as `MATCH`. The mean paired reduction remained 27.14 percentage points. This is the required deeper analysis (sensitivity/error robustness check). It does not establish that the bibliographic audit is error-free.

Other audit findings: 100 candidate entries were initially extracted; one was commentary rather than a complete reference, leaving 99 analyzed references. The audit classified 93 as MATCH, five as PARTIAL_MATCH, one as DOI_MISMATCH, and one as NOT_APPLICABLE (the latter excluded from the 99-reference analysis). A DOI 404 is not treated as proof of fabrication. The 2025 ACM hallucination survey entry had an incorrect DOI in the generated citation; the matching publication record uses DOI 10.1145/3703155. The arXiv preprint 2412.12472 has a 2024 first-submission date and a later 2025 proceedings version; cutoff classification depends on which version is cited.

## 4. Deviations and threats to validity

- The generated reviews exceeded the planned 800–1,000 word range. Original outputs were retained; no post-hoc editing is claimed.
- Five matched pairs and one ChatGPT interface/model configuration limit statistical power and generalizability.
- Manual generation through the ChatGPT UI is not an API-level deterministic reproduction.
- Bibliographic classification depends on the cited version and date-source quality; candidate years and verified publication dates must not be conflated.
- Unequal citation counts across some paired reviews may influence rate stability.
- The study measures compliance with an explicit publication-date instruction. It does **not** measure the model's internal training-data cutoff.

## 5. Reproduction script scope

`scripts/reproduce_analysis.py` reads the archived CSVs, checks expected row/column counts and key totals, recomputes descriptive paired statistics, and regenerates two figures. It was executed successfully in the current working environment. It re-analyses the archived tables; it does not recreate the ten original LLM generations or independently validate every reference.

## 6. Prompt 13–14 completion

The script exports reproducible CSV tables and PNG figures to `results/reproduced/`. Interpretation is documented in `results/RESULTS_AND_FINDINGS.md` and `docs/DISCUSSION_LIMITATIONS_CONCLUSION.md`. Do not report the script run as an original generation run.
