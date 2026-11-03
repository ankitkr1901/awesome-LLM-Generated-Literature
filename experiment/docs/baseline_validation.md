# Baseline / Comparator Validation Report

## Study type
This is a controlled prompt-comparison study, not a model-training or algorithm-reproduction project. Therefore, the relevant baseline is Condition A (standard prompt), and the intervention is Condition B (same prompt plus explicit date-boundary instruction). No external trained model or benchmark dataset is claimed.

## VERIFIED from supplied artifacts
- Ten generated review text files are retained under `outputs/` (five A/B pairs).
- The release contains frozen prompt protocol documentation and the extracted citation/audit CSVs.
- The final condition summary records 51 citations for A and 48 for B.
- The paired comparison file contains five pairs.
- A local analysis script was run against the archived CSVs and passed its data assertions; see `results/reproduced/REPRODUCTION_RUN_REPORT.md`.

## NOT VERIFIED / still required from the researcher
- The exact model version, UI settings, timestamps, and generation order must be cross-checked against the original generation log/screenshots if these records exist. Do not infer them from the output text.
- The original generation process cannot be deterministically rerun from the supplied CSVs. A fresh rerun would be a new experiment and should be logged separately.
- No baseline software implementation of the ChatGPT model is available or expected. The prompt condition is the comparator.
- The archived bibliography classifications are not independently re-audited by the reproduction script.

## Validation decision
**Comparator validation: PARTIAL / appropriate for the selected study design.** The A/B prompt conditions and analysis tables are inspectable. Full provenance validation of the manual UI generations and independent bibliographic audit remains a human verification task.
