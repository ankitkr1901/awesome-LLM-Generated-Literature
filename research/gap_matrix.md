# Gap Matrix: Knowledge Cutoff Effects on LLM-Generated Literature Reviews in Rapidly Evolving Fields

**Scope note:** This matrix is based on the supplied review text and the Prompt 02 analysis. Nothing below is verified against an original paper unless explicitly stated. Numerical findings are described as “as reported in the review.” No G2 experiment has been run and no code results are claimed.

**Evidence labels:** **VERIFIED** = checked in an original source or by real execution; **INFERRED** = plausible and needs testing; **UNKNOWN** = missing evidence.

## 1. What the review contains

The supplied review is a narrative synthesis. It reports no experiment of its own and does not state a search protocol. The methods, datasets and findings below are those the review discusses, not independently verified findings.

### Central methods discussed

- **Cutoff measurement:** effective-cutoff tracing [3] and LLMLagBench [10] (Section 2.2).
- **Temporal knowledge probing:** time-aware language models [4] and WikiRecentChanges-style conflict tests (Section 2.3; source details need verification).
- **Contamination analysis:** post-cutoff performance decay [18] (Sections 2.3 and 3.4).
- **Mitigations:** RAG, active retrieval and Self-RAG [1, 5, 6, 9]; grounded pipelines [16]; knowledge editing (ROME, MEMIT, GRACE, WISE) [15]; continual learning [17]; explicit-cutoff prompting (source missing from reference list); TEMPO reward training [19]; and temporally filtered legal RAG [11].

### Datasets and benchmarks named in the review

- SciReviewGen [8] (Section 2.5).
- LLMLagBench [10].
- WikiRecentChanges (no reference-list entry identified in the review).
- Orthopedic systematic-review reference lists [2].
- A mental-health citation study (no reference-list entry identified).
- Statutory QA data [11] (dataset name not specified in the review).

### Measured findings as reported in the review

| Finding as reported | Source in review | Status |
|---|---|---|
| Fabrication rates of 39.6% (GPT-3.5), 28.6% (GPT-4), and 91.4% (Bard); precision below 15%. | [2], Section 2.4 | UNKNOWN — verify original |
| Extraction precision 83.0%, recall 86.0% across 172 studies; publication search weakest. | [13], Section 2.5 | UNKNOWN — verify original |
| Hallucination risk below 0.5% at 95% confidence. | [16], Sections 2.5 and 4.1 | UNKNOWN — verify original |
| Leakage 2–13% reduced to 0.6–3.7%. | [19], Section 4.3 | UNKNOWN — verify original |
| One open model's self-reported cutoff was nearly two years earlier than its benchmark-estimated cutoff. | [10], Section 2.2 | UNKNOWN — verify original |
| Corpus of over 10,000 reviews and 690,000 cited papers. | [8], Section 2.5 | UNKNOWN — verify original |

### Limitations described by the review

- Reported cutoffs may be unreliable (Section 5).
- Temporal benchmarks may be fragile ([18], Section 5).
- Mitigations have trade-offs: RAG inherits corpus lag; editing targets discrete facts; continual learning can risk forgetting; prompt/reward methods were reportedly evaluated mostly on narrow tasks (Sections 4–5).
- Naive web search showed recency bias in a legal QA setting [11] (Section 4.4); applying this to literature reviews is an extrapolation.

### Unresolved questions raised by the review

- How much citation fabrication is due to cutoff pressure rather than baseline hallucination? (Section 5, fourth point.)
- Do prompt and reward gains transfer to narrative synthesis? (Section 5.)
- Can recency weighting be adapted to the field? (Section 6.)
- How quickly does a generated review become stale? (Section 6.)
- Can user-facing confidence indicators communicate review currency? (Section 6.)

## 2. Five-gap matrix

| ID | Candidate research gap | Supporting passage or reference | Reported limitation or inferred gap | Testable research question | Evidence and experiment required | Feasibility | Verification still needed |
|---|---|---|---|---|---|---|---|
| G1 | Citation fabrication versus cutoff proximity is unmeasured. | Section 5 (fourth point), Section 6 (third direction), Section 3.3; [2], [14]. | Gap stated in the supplied review, not verified as a limitation reported by an original paper. The mechanism in Section 3.3 is INFERRED. | Does the rate of non-existent citations rise as the requested publication window approaches or passes a model's effective cutoff? | Use fixed prompts across date windows relative to an estimated cutoff. Verify each citation against a scholarly metadata index. Report fabrication rate per window and repeat runs where feasible. | **High, provisionally.** Requires LLM access and metadata lookup. Citation matching and cutoff estimation are hard parts. | Check [2] and [14] for date-stratified fabrication results; check [3] and [10] for cutoff estimation. Verify metadata-index access. Novelty requires a separate search. |
| G2 | Prompt-based temporal grounding is untested on open-ended review writing. | Section 4.3, Section 5 (third point); [19]. | The review reports that related methods were validated on narrow tasks. The specific prefix-versus-suffix claim cites an unlisted source. | Does an explicit-cutoff instruction at the start or end of the prompt reduce post-cutoff and fabricated claims versus no instruction? | Compare prompt variants on a fixed topic set; use a rubric for temporal claims and citation fabrication; repeat runs. | **High, provisionally.** No training required; scoring and source verification are the main work. | Identify the missing “temporal-critique” source; verify [19]'s numbers and task; check comparability to narrative review generation. |
| G3 | Omission of post-cutoff work (“silent staleness”) is not quantified. | Section 3.1, Section 6 (fourth direction); [3], [10]. | INFERRED from [3] and [10]; the review does not measure omission in generated reviews. | How many landmark papers published after a model's cutoff are missing from generated reviews, and how does omission vary across topics or dates? | Create a dated, justified reference list of landmark papers for one or two fast-moving topics and compare it with generated reviews. | **Medium.** Ground-truth selection is the main methodological risk. | Verify whether [10] studies event knowledge rather than review writing; justify how reference papers are selected. |
| G4 | Recency weighting in retrieval may distort historical coverage. | Section 4.4, Section 6 (second direction); [11]. | INFERRED; the recency-bias finding is from legal QA and is extrapolated to literature review. | Do unweighted, date-filtered and recency-weighted retrieval yield different historical coverage and citation fabrication in generated reviews? | Use a fixed corpus and RAG pipeline with three retrieval variants; evaluate against a reference review or predefined paper set. | **Low to medium.** Requires a corpus and retrieval stack; more engineering. | Read [11] to establish what was tested; verify corpus access/licence and SciReviewGen usability [8]. |
| G5 | No benchmark jointly measures staleness, temporal blending and fabrication. | Section 6 (first direction), Section 3.2; [10], [3], [8]. | Gap stated in the supplied review. The proposed “blending” mechanism is INFERRED from Section 3.2. | Can a small dated review benchmark measure staleness, blending and citation fabrication together? | Construct dated review cases and define separate metrics for each failure mode. | **Low for a full project.** A small pilot may be possible. | Check what SciReviewGen [8] already provides; verify what [10] measures; perform a separate novelty search. |

## 3. Three strongest candidates (provisional)

The ranking is **INFERRED**, based on expected significance, resources and feasibility; it is not an empirical result.

1. **G1 — Citation fabrication versus cutoff proximity.** The supplied review raises this as unmeasured. It has a clear outcome metric, but effective-cutoff estimation and citation matching are risks.
2. **G2 — Explicit-cutoff prompting.** This is relatively inexpensive and controllable because it does not require model training. The missing source for the prompting claim must be resolved.
3. **G3 — Silent staleness.** This targets omitted recent work, but requires a defensible ground-truth list.

G4 and G5 remain interesting but require more infrastructure or dataset construction.

## 4. Before implementation

- Do not call any gap novel until a separate literature search has been completed.
- Verify the original papers [2], [3], [10], [14], [18] and [19], as well as sources behind placeholder citations.
- Confirm LLM access, metadata-source access, available time and any compute constraints.
- Choose and freeze a scoring rubric before evaluating generated outputs.
- The existing repository's metadata-audit experiment is a separate earlier study; it does not test G2.
- No G2 code has been written or run, and no experimental result is claimed in this matrix.
