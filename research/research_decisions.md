# Research Decisions Log

**Project:** Knowledge Cutoff Effects on LLM-Generated Literature Reviews in Rapidly Evolving Fields (implementation paper)

**Evidence labels:** **VERIFIED** = checked in an original source or by real execution; **INFERRED** = plausible and still needs testing; **UNKNOWN** = evidence is missing.

**Evidence rule:** The statements below are verified against the supplied literature-review text only unless explicitly stated otherwise. A claim is not verified against an original publication until the original paper has been opened and the relevant passage located.

## D-001 — Scope of the source review

- **Decision:** Treat the Overleaf/Prism PDF version of the completed review as the starting evidence base, not as text to recycle.
- **Reason:** The implementation paper must connect a new, testable question to evidence rather than copy the prior review.
- **Evidence:** Sections 1–7 of the review were read (**VERIFIED against the review text**). The `.docx` version has not been confirmed identical to the PDF (**UNKNOWN**).
- **Next action:** Compare the `.docx` and PDF, then use one canonical version.

## D-002 — Review limitations that affect its use as evidence

| ID | Issue in the review | Location | Status | Action |
|---|---|---|---|---|
| L1 | Placeholder citations have no identifiable reference-list entry: “cited PMC study on citation fabrication, 2025”; “cited work on temporal knowledge conflict resolution, 2026”; “temporal-critique literature”; “surveyed in recent RAG-hallucination literature”; “cited in recent literature-synthesis tooling work”. | Sections 2.1, 2.3, 2.4, 3.3, 4.1, 4.3, 6 | UNKNOWN source | Find and verify the original papers or remove the claims. |
| L2 | The abstract attributes “blending of pre/post-cutoff knowledge” to Zhang et al. 2025 [18], while the body associates multiple partial cutoffs with Pezik et al. [10]; [18] is described in the review as a benchmark-contamination paper. | Abstract; Sections 2.2, 3.2, 3.4 | Attribution inconsistent | Check [10] and [18], then correct the attribution. |
| L3 | Publication-growth figures (3.3M articles in 2022, 2.0M in 2010, approximately 4–5% yearly growth) are cited to [12], which may not be the primary source; the arXiv 1M→2M→3M timeline is uncited. | Section 2.1 | UNKNOWN primary source | Locate the primary statistics source or remove/qualify the figures. |
| L4 | The introduction says “hundreds of projects” use LLMs for review, while Section 2.5 says [13] covered 172 studies. | Sections 1 and 2.5 | Possible inconsistency | Check [13] and clarify the scope of each count. |
| L5 | The claim that models hedge on post-cutoff events but fabricate recent citations because narrative synthesis differs from factual recall is attributed to [7, 18]. | Section 1 | INFERRED; possibly stronger than cited evidence | Check [7] and [18]; reframe as a hypothesis if unsupported. |
| L6 | The review does not state a search protocol (databases, dates, inclusion criteria). Figure 1 (ResearchRabbit) is not discussed in the text and shows works not clearly represented in the bibliography. | Figure 1; references | UNKNOWN | Document the search method where possible and reconcile figure items with references. |
| L7 | Findings from legal recency bias [11] and an incompletely identified mental-health citation study are extrapolated to literature review generation. | Sections 3.3, 4.4, 6 | INFERRED | Treat these as hypotheses unless direct evidence is found. |

## D-003 — Numerical claims to verify against original papers

| Claim as stated in the review | Cited source | Current status |
|---|---|---|
| Hallucination rates of 39.6%, 28.6%, and 91.4% for GPT-3.5, GPT-4, and Bard; precision below 15%. | [2] Chelli et al. (2024) | UNKNOWN — verify |
| Mean extraction precision 83.0%, recall 86.0%; 172 studies; search stage weakest. | [13] Scherbakov et al. (2025) | UNKNOWN — verify |
| Hallucination risk below 0.5% at 95% confidence. | [16] Wu et al. (2025) | UNKNOWN — verify |
| Leakage 2–13% reduced to 0.6–3.7% with TEMPO. | [19] Zhang & Stadie (2026) | UNKNOWN — verify |
| A model's self-reported cutoff was about two years earlier than a benchmark-estimated cutoff. | [10] Pezik et al. (2025) | UNKNOWN — verify |
| More than 10,000 reviews and 690,000 cited papers. | [8] Kasanishi et al. (2023) | UNKNOWN — verify |

## D-004 — Candidate research gaps (before selection)

| ID | Review location | Origin | Candidate question | Possible experiment | Main needs |
|---|---|---|---|---|---|
| G1 | Section 5 (fourth point); Section 6 (third direction) | Gap stated by the review, not verified as an original-paper limitation | Does citation fabrication rise as requested publication dates approach or pass a model's effective cutoff? | Generate citations for date windows and verify them against scholarly metadata; compare fabrication rates across windows. | LLM access, metadata source, date-labelled reference set. |
| G2 | Section 4.3; Section 5 (third point) | Inference from [19] and prompting literature | Does explicit-cutoff prompting (prefix, suffix, or no instruction) reduce post-cutoff or fabricated claims in open-ended review generation? | Compare prompt variants and score temporal claims and citations. | LLM access, source verification, scoring rubric. |
| G3 | Section 3.1; Section 6 (fourth direction) | Inference | How much post-cutoff landmark work does a review omit, and how does omission vary with literature age? | Compare generated reviews with a dated list of landmark papers. | Defensible reference list and bounded topic/time window. |
| G4 | Section 4.4; Section 6 (second direction) | Extrapolation from legal-domain finding [11] | Does recency-weighted retrieval distort historical coverage? | Compare unweighted, date-filtered, and recency-weighted retrieval on a fixed corpus. | Corpus, retrieval pipeline, engineering time. |
| G5 | Section 6 (first direction) | Gap stated by the review | Can a small benchmark jointly measure staleness, temporal blending, and citation fabrication? | Build a small benchmark from dated reviews and define metrics for each failure mode. | Dataset construction effort; full benchmark likely too large for a short project. |

**Provisional ranking** by significance, resource needs, and feasibility: G1, G2, G3. This ranking is **INFERRED**. Novelty is **UNKNOWN** for all candidates until a separate literature search is performed.

## D-005 — Decisions so far

- Use explicit evidence labels in later records.
- Keep the prompt/AI-assistance log separate at `logs/ai_assistance_log.md`.
- Do not claim a novel contribution or an experiment result without independent evidence.
- Preserve the earlier metadata-audit experiment as a distinct prior artifact; it does not test G2.

## D-006 — Provisional experiment selection

- **Decision:** Select G2, explicit-cutoff prompting, as the leading candidate for a small controlled experiment.
- **Research question:** Does explicitly instructing an LLM to acknowledge its knowledge limitations improve citation reliability and temporal coverage in generated literature reviews compared with a baseline prompt?
- **Proposed comparison:** (A) baseline prompt; (B) prompt with an explicit knowledge-cutoff instruction.
- **Potential measurements:** Citation existence and metadata correctness; coverage of relevant papers in a predefined publication period; unsupported claims.
- **Status:** **INFERRED** — the experiment has not been run, and the gap's novelty has not been established.
- **Risks:** The model's effective cutoff may be uncertain; citation verification needs reliable scholarly records; prompt wording may affect the result.
- **Before implementation:** Verify key source claims, confirm access to an LLM and scholarly metadata, define topic/date windows, and specify scoring rules.
- **Next action:** Complete a feasibility check before writing code.

## Current next actions

1. Compare the review `.docx` with the canonical PDF.
2. Verify the key original papers and numerical claims listed in D-003, plus the attribution issue L2.
3. Confirm available LLM access, scholarly metadata access, time, and submission constraints.
4. Assess whether G2 can be evaluated fairly and reproducibly with those resources.
5. Update this log only when a decision changes or new evidence is obtained.

## Current status

**Prompt 01 and Prompt 02 outputs are recorded. G2 is provisional. No G2 code has been written or run, and no G2 experimental results or novelty claims are made.** The existing metadata-audit experiment in this repository is a separate prior study, not evidence for G2.
