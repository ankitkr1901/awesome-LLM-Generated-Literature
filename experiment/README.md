# Knowledge Cutoffs, Temporal Knowledge Boundaries, and Citation Reliability in Large Language Models

## Project overview

This project investigates whether explicitly instructing a large language model
to respect a publication-date boundary changes the temporal compliance and
bibliographic reliability of generated literature reviews.

## Research design

- Controlled comparative prompt study
- Condition A: standard literature-review prompt
- Condition B: same prompt with an explicit publication-date boundary
- Cutoff date: 31 December 2024 (inclusive)
- Five matched prompt pairs
- Ten generated literature reviews

## Main preliminary findings

- 99 citation instances were identified.
- Condition A: 15 post-cutoff citations among 51 references.
- Condition B: 0 post-cutoff citations among 48 references.
- Mean paired reduction in post-cutoff citation rate: 29.64 percentage points.
- Bibliographic audit: 93 MATCH, 5 PARTIAL_MATCH, 1 DOI_MISMATCH,
  and 1 NOT_APPLICABLE.

These findings are descriptive and should be interpreted cautiously.
Publication-year candidates and unresolved bibliographic cases require
appropriate qualification in the final report.

## Repository structure

- `data/`: citation extraction, audit, and analysis datasets
- `outputs/`: generated literature reviews
- `notebooks/`: Colab notebooks and analysis code
- `results/`: final statistical outputs and figures
- `docs/`: experiment protocol and documentation

## Reproducibility

The analysis was conducted using Python and Google Colab.
The model-generated reviews were collected manually through the ChatGPT interface.

## Limitations

The experiment contains only five matched pairs. It measures observable
compliance with an explicit publication-date instruction, not the model's
internal training-data cutoff or actual internal knowledge boundary.
