# Prompt Protocol — Version 1.0

Project: Knowledge Cutoffs, Temporal Knowledge Boundaries, and Citation Reliability in Large Language Models

Reference cutoff for Condition B: 2024-12-31 inclusive.

Study scope: This experiment evaluates observable compliance with a stated publication-date boundary. It does not measure or change the model's true internal training-data or knowledge-cutoff date.

## Condition A — Standard prompt

Write a concise academic literature review of approximately 800–1,000 words on "Knowledge Cutoffs, Temporal Knowledge Boundaries, and Citation Reliability in Large Language Models". Explain the main concepts, summarize relevant research themes and methods, compare findings, identify limitations and open questions, and conclude with a short synthesis. Include approximately 8–12 scholarly references. For each reference, provide author(s), title, publication venue where available, year, and DOI or stable publisher URL where available. Do not invent citations; if you are uncertain about a reference or bibliographic detail, state that uncertainty.

## Condition B — Explicit-cutoff prompt

Publication-date boundary: include only scholarly works published on or before 2024-12-31. Do not cite or rely on works published after that date. Do not guess publication dates or invent references. If you cannot verify whether a work falls within the boundary, omit it or clearly flag it as unverified.

Write a concise academic literature review of approximately 800–1,000 words on "Knowledge Cutoffs, Temporal Knowledge Boundaries, and Citation Reliability in Large Language Models". Explain the main concepts, summarize relevant research themes and methods, compare findings, identify limitations and open questions, and conclude with a short synthesis. Include approximately 8–12 scholarly references. For each reference, provide author(s), title, publication venue where available, year, and DOI or stable publisher URL where available. Do not invent citations; if you are uncertain about a reference or bibliographic detail, state that uncertainty.

## Run recording requirements

For every generation, record:
- condition (A or B)
- pair ID and run ID
- generation date/time and timezone
- displayed model label
- visible interface settings
- exact prompt text/version
- full unedited output file path
- run order and any interruption/deviation

Do not change prompts after inspecting condition-level results. If a protocol change is necessary, stop, version the protocol, document the reason, and decide whether affected runs must be restarted before examining results.
