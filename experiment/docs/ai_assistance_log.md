# Human–AI Assistance and Verification Log (Prompt 18)

This log records only activities evidenced by the project artifacts and current work. It is not a substitute for the complete original prompt history. Add dates, screenshots, exact prompts, commits, and actual outputs where available.

| Activity | AI assistance evidenced | Human verification / decision | Status |
|---|---|---|---|
| Research question and design | Assistance used to refine the cutoff-compliance question and matched A/B comparison | Research scope narrowed to explicit publication-date boundary compliance; cutoff fixed at 2024-12-31 | Documented in protocol and report |
| Prompt protocol | Prompt definitions and protocol documentation prepared with AI assistance | Two conditions retained; same base prompt with date instruction added in B | Verify exact prompts against original saved protocol |
| Citation audit | AI assistance used to organize candidate extraction and metadata checks | Manual decisions include MATCH, PARTIAL_MATCH, DOI_MISMATCH and NOT_APPLICABLE; DOI 404 not treated as proof of fabrication | Audit CSV supplied; primary-source spot checks remain advisable |
| Statistical analysis | AI assistance used to prepare analysis logic and interpretation | Reproduction script assertions and recomputed totals were executed in this runtime | PASS for archived CSV re-analysis only |
| DOI correction | AI-assisted identification of DOI discrepancy | The 2025 ACM survey DOI in one citation was corrected to 10.1145/3703155 in audit notes | Confirm against publisher record before final publication |
| Repository documentation | AI assistance used to draft README and supporting documentation | File paths were aligned to the actual `experiment/` structure | Researcher must verify GitHub links after upload |

## Known limitations / manual corrections to disclose
1. A DOI 404 response is not sufficient evidence that a paper is fabricated; records can be missing or malformed.
2. A cited preprint and its later proceedings version can have different publication dates; version identity matters for cutoff classification.
3. The analysis script checks and recomputes supplied tables; it does not independently prove the source CSV labels or regenerate the original ChatGPT responses.

## Reflection
AI assistance was useful for structuring the study, preparing analysis/documentation, and checking arithmetic and consistency. Human responsibility remains with the researcher for verifying source records, understanding the protocol, checking the code, deciding how versions are classified, and defending the limits of inference.

## Researcher completion fields
- [TO COMPLETE] Exact AI tools and displayed model labels used at each stage.
- [TO COMPLETE] Dates and exact prompts for all ten manual generations.
- [TO COMPLETE] Relevant Git commits/diffs and human edits.
- [TO COMPLETE] Actual debugging cases and tracebacks, if any. If none occurred, state that no debugging case was recorded; do not invent one.
- [TO COMPLETE] Researcher's own reflection and confirmation that they understand the analysis script.
