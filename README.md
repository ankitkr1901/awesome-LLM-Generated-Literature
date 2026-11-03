# Awesome Knowledge Cutoff Effects on LLM-Generated Literature Reviews

A curated academic research repository focused on **knowledge cutoff
effects, temporal knowledge boundaries, and citation reliability in
LLM-generated literature reviews**, particularly in rapidly evolving
research fields.

This repository connects the original literature review and
citation-integrity audit with a controlled comparative experiment on
explicit publication-date instructions. It also curates relevant
scholarly literature, datasets, tools, implementations, and learning
resources.

**Research topic:** Knowledge Cutoff Effects on LLM-Generated Literature
Reviews in Rapidly Evolving Fields

------------------------------------------------------------------------

## Contents

-   [Overview](#overview)
-   [Research Journey](#research-journey)
-   [Original AI-Assisted Research
    Paper](#original-ai-assisted-research-paper)
-   [Citation Integrity Audit](#citation-integrity-audit)
-   [Experimental Study](#experimental-study)
    -   [Research Question](#research-question)
    -   [Experimental Design](#experimental-design)
    -   [Main Findings](#main-findings)
    -   [Experiment Files](#experiment-files)
    -   [Interpretation and
        Limitations](#interpretation-and-limitations)
-   [Repository Structure](#repository-structure)
-   [Survey and Review Papers](#survey-and-review-papers)
-   [Foundational Papers](#foundational-papers)
-   [Recent Research](#recent-research)
-   [Methods and Mitigation
    Approaches](#methods-and-mitigation-approaches)
-   [Datasets and Benchmarks](#datasets-and-benchmarks)
-   [Tools and Libraries](#tools-and-libraries)
-   [GitHub Implementations](#github-implementations)
-   [Tutorials and Learning
    Resources](#tutorials-and-learning-resources)
-   [Verification and Research
    Integrity](#verification-and-research-integrity)
-   [License](#license)

------------------------------------------------------------------------

## Overview

Large language models (LLMs) are increasingly used to support academic
literature-review tasks such as scholarly search, screening, reference
extraction, summarization, and synthesis.

However, LLM-generated literature reviews face an important temporal
challenge. A model's available knowledge may reflect a particular
training snapshot or other information-access boundary. As a result,
research published after that boundary may be missing, incompletely
represented, or inaccurately incorporated into generated reviews.

This problem is particularly relevant in rapidly evolving areas such as
artificial intelligence, biomedicine, computer science, and law, where
new research can quickly change the state of the literature.

Temporal limitations are not the only concern. AI-generated references
may also contain incorrect author names or publication details,
mismatched identifiers, incomplete metadata, or sources that cannot be
independently verified.

This repository studies these issues through three connected components:

1.  An original literature review of temporal knowledge boundaries and
    LLM-generated literature reviews.
2.  A citation-integrity audit of AI-generated scholarly references.
3.  A controlled comparative experiment investigating explicit
    publication-date instructions.

The repository distinguishes between **temporal compliance**,
**bibliographic correctness**, and a model's actual internal knowledge
boundary. These are related concerns, but they are not interchangeable
measurements.

## Research Journey

The project follows this progression:

**Literature Review → Research Gap → Research Question → Experimental
Design → Data Collection → Citation Verification → Evaluation → Research
Report**

  -----------------------------------------------------------------------
  Component                           Purpose
  ----------------------------------- -----------------------------------
  Original literature review          Examine knowledge cutoff effects,
                                      temporal knowledge, citation
                                      reliability, and mitigation
                                      methods.

  Citation-integrity audit            Examine the existence and
                                      bibliographic accuracy of
                                      AI-generated references.

  Controlled experimental study       Investigate whether explicit
                                      publication-date instructions
                                      reduce post-cutoff citations in
                                      generated literature reviews.
  -----------------------------------------------------------------------

The experimental work uses a controlled comparative study design
(Pathway B).

------------------------------------------------------------------------

## Original AI-Assisted Research Paper

**Title:** Knowledge Cutoff Effects on LLM-Generated Literature Reviews
in Rapidly Evolving Fields

The original literature review examines:

-   Effective versus reported knowledge cutoffs.
-   Temporal misalignment in generated literature reviews.
-   Silent staleness and incomplete literature coverage.
-   Citation fabrication and bibliographic errors.
-   Temporal knowledge evaluation and benchmark contamination.
-   Retrieval-augmented generation.
-   Knowledge editing and continual learning.
-   Prompt-based and reward-based temporal grounding.

**Original research paper:**

-   [Original literature review PDF](paper/MSE_03_ANKIT_KUMAR.pdf)
-   [Original literature review Word
    document](paper/Knowledge_Cutoff_Effects_LLM_Literature_Reviews.docx)

This paper provides the literature foundation for the subsequent
experimental investigation.

------------------------------------------------------------------------

## Citation Integrity Audit

The repository also contains an earlier AI-assisted citation-integrity
audit. It investigated whether references generated by an AI system
corresponded to genuine scholarly publications and whether their
bibliographic metadata were accurate.

### Reported audit findings

  Audit measure                            Reported result
  -------------------------------------- -----------------
  References in the AI-generated paper                  23
  References deeply audited                             10
  References verified                                    9
  References with incorrect metadata                     1
  Frankenstein references                                0
  Fabricated references                                  0
  Identifier mismatches                                  0
  Authenticity score                                90/100
  Prediction accuracy                                  90%

These figures belong to the **original citation-integrity audit**. They
are separate from the later experimental study.

-   [Citation-integrity audit working
    document](citatition-audit/Lab%2001%20AI-ASSISTED%20CITATION%20INTEGRITY%20AUDIT.docx)

------------------------------------------------------------------------

## Experimental Study

### Title

**Knowledge Cutoffs, Temporal Knowledge Boundaries, and Citation
Reliability in Large Language Models: A Controlled Comparative Study of
Explicit Publication-Date Instructions**

The experimental study investigates whether adding an explicit
publication-date boundary instruction changes the temporal compliance of
LLM-generated literature reviews.

### Research Question

Does adding an explicit publication-date boundary instruction reduce
post-cutoff citations in literature reviews generated by a large
language model, and how does this affect bibliographic reliability?

### Experimental Design

The study uses two matched prompting conditions.

**Condition A --- Standard prompt**

The model receives a standard literature-review prompt without an
explicit publication-date restriction.

**Condition B --- Explicit temporal boundary**

The same underlying prompt is preceded by an instruction requiring the
model to include only scholarly works published on or before **31
December 2024**, inclusive, and not to guess uncertain publication
dates.

### Experiment overview

  -----------------------------------------------------------------------
  Component                           Design
  ----------------------------------- -----------------------------------
  Study design                        Controlled comparative study

  Experimental conditions             Standard prompt (A) and explicit
                                      temporal instruction (B)

  Matched prompt pairs                5

  Generated literature reviews        10

  Pair identifiers                    P01--P05

  Publication-date cutoff             31 December 2024, inclusive

  Citation instances analyzed         99

  Generation order                    Randomized using seed 2026

  Generation method                   Manual generation through the
                                      ChatGPT interface

  Bibliographic verification          Crossref, OpenAlex, and additional
                                      scholarly record checks
  -----------------------------------------------------------------------

### Main Findings

  Measure                         Condition A   Condition B
  ----------------------------- ------------- -------------
  Citation instances                       51            48
  Within-cutoff citations                  36            48
  Post-cutoff citations                    15             0
  Unknown publication years                 0             0
  Post-cutoff citation rate            29.41%         0.00%
  Bibliographic MATCH entries              45            48
  Bibliographic match rate             88.24%       100.00%

Condition A produced 15 post-cutoff citation instances among 51
references, while Condition B produced none among 48 references. The
observed difference in aggregate post-cutoff rates was **29.41
percentage points**.

### Matched-Pair Comparison

  -----------------------------------------------------------------------
  Pair                  Condition A        Condition B          Reduction
                   post-cutoff rate   post-cutoff rate 
  -------------- ------------------ ------------------ ------------------
  P01                        30.00%              0.00%           30.00 pp

  P02                        30.00%              0.00%           30.00 pp

  P03                        30.00%              0.00%           30.00 pp

  P04                        18.18%              0.00%           18.18 pp

  P05                        40.00%              0.00%           40.00 pp

  **Mean**               **29.64%**          **0.00%**       **29.64 pp**
  -----------------------------------------------------------------------

All five matched pairs showed a lower post-cutoff citation rate under
Condition B.

### Bibliographic Verification

The manual bibliographic audit classified 100 extracted candidate
entries as follows:

  Audit decision                  Entries
  ----------------------------- ---------
  MATCH                                93
  PARTIAL_MATCH                         5
  DOI_MISMATCH                          1
  NOT_APPLICABLE                        1
  **Total candidate entries**     **100**

One candidate was commentary rather than a complete bibliographic
reference. Therefore, the experimental analysis used 99 actual reference
instances.

A sensitivity analysis restricted to bibliographically matched
references produced:

  Measure                      Condition A   Condition B
  -------------------------- ------------- -------------
  Confirmed references                  45            48
  Within-cutoff references              33            48
  Post-cutoff references                12             0
  Post-cutoff rate                  26.67%         0.00%

The mean paired reduction in this sensitivity analysis was **27.14
percentage points**.

### Statistical Interpretation

All five matched pairs favored Condition B. A two-sided exact sign test
based on the five pairwise directions yielded **p = 0.0625**.

This does not meet the conventional 0.05 significance threshold. The
findings are therefore interpreted primarily as descriptive evidence
rather than conclusive statistical proof.

### Experiment Files

The complete release package was uploaded into `experiment/` **without
changing its internal folder structure**. Its files are therefore linked
using the paths below.

**Main documents**

-   [Experiment README](experiment/README.md)
-   [Research report](experiment/RESEARCH_REPORT.md)
-   [Final research paper
    PDF](experiment/LLM_Cutoff_Temporal_Knowledge_Study.pdf)

**Documentation**

-   [Methodology](experiment/docs/METHODOLOGY.md)
-   [Discussion, limitations, and
    conclusion](experiment/docs/DISCUSSION_LIMITATIONS_CONCLUSION.md)
-   [Extracted references
    appendix](experiment/docs/APPENDIX_A_EXTRACTED_REFERENCES.md)
-   [Data dictionary](experiment/docs/DATA_DICTIONARY.md)
-   [Experimental prompt
    protocol](experiment/docs/prompt_protocol_v1.md)

**Results and figures**

-   [Results and findings](experiment/results/RESULTS_AND_FINDINGS.md)
-   [Figure index](experiment/results/FIGURE_INDEX.md)
-   [Preliminary results](experiment/results/preliminary_results.md)
-   [Overall cutoff-rate
    figure](experiment/results/figure1_overall_cutoff_rate.png)
-   [Matched-pair comparison
    figure](experiment/results/figure2_paired_comparison.png)
-   [Sensitivity-analysis
    figure](experiment/results/figure3_sensitivity_analysis.png)

**Supporting files**

-   `experiment/data/` --- citation extraction, bibliographic
    verification, and evaluation CSV files.
-   `experiment/outputs/` --- ten generated literature-review text
    files.
-   `experiment/results/` --- results documentation,
    sensitivity-analysis CSV, and figures.

### Interpretation and Limitations

The experiment measures **observable compliance with an explicitly
stated publication-date instruction**. It does not directly measure the
model's internal training-data cutoff or the exact date when the model
acquired particular information.

Other limitations include:

-   Only five matched prompt pairs were evaluated.
-   Reviews were generated through one model interface.
-   Generated reviews exceeded the originally intended 800--1,000-word
    target.
-   Some bibliographic entries had partial matches or DOI discrepancies.
-   Publication-version distinctions, including preprint versus
    proceedings dates, require careful interpretation.
-   The results should not be generalized automatically to all LLMs,
    topics, or prompting conditions.

The observed improvement in temporal compliance does not guarantee that
all references are bibliographically correct. Independent verification
remains necessary.

------------------------------------------------------------------------

## Repository Structure

The existing repository structure has been retained. The experimental
release has been added as a separate `experiment/` folder, preserving
the release's own internal structure.

``` text
awesome-LLM-Generated-Literature/
│
├── README.md
├── LICENSE
├── tutorials.md
│
├── paper/
│   ├── Knowledge_Cutoff_Effects_LLM_Literature_Reviews.docx
│   └── MSE_03_ANKIT_KUMAR.pdf
│
├── research/
│   ├── gap_matrix.md
│   └── research_decisions.md
│
├── citatition-audit/
│   └── Lab 01 AI-ASSISTED CITATION INTEGRITY AUDIT.docx
│
├── references/
│   └── references.md
│
├── datasets/
│   └── datasets.md
│
├── tools/
│   └── tools.md
│
├── implementations/
│   └── github-repositories.md
│
└── experiment/
    ├── README.md
    ├── RESEARCH_REPORT.md
    ├── LLM_Cutoff_Temporal_Knowledge_Study.pdf
    │
    ├── docs/
    │   ├── APPENDIX_A_EXTRACTED_REFERENCES.md
    │   ├── DATA_DICTIONARY.md
    │   ├── prompt_protocol_v1.md
    │   ├── DISCUSSION_LIMITATIONS_CONCLUSION.md
    │   └── METHODOLOGY.md
    │
    ├── data/
    │   └── [CSV audit and analysis files]
    │
    ├── outputs/
    │   └── [10 generated review text files]
    │
    └── results/
        ├── RESULTS_AND_FINDINGS.md
        ├── sensitivity_analysis.csv
        ├── FIGURE_INDEX.md
        ├── preliminary_results.md
        └── [three PNG figures]
```

The original `paper/`, `research/`, `citatition-audit/`, `references/`,
`datasets/`, `tools/`, and `implementations/` folders remain at the
repository root. The new experimental files are kept inside
`experiment/`.

------------------------------------------------------------------------

## Survey and Review Papers

-   [Retrieval-Augmented Generation for Large Language Models: A
    Survey](https://doi.org/10.48550/arXiv.2312.10997) --- Survey of
    retrieval-augmented generation and its role in grounding LLMs with
    external information.
-   [A Survey on Hallucination in Large Language
    Models](https://doi.org/10.2196/53164) --- Broad taxonomy and
    discussion of hallucination challenges in LLMs.
-   [Knowledge Editing for Large Language Models: A
    Survey](https://doi.org/10.1145/3698590) --- Reviews techniques for
    modifying or updating parametric knowledge.
-   [Continual Learning for Large Language Models: A
    Survey](https://doi.org/10.48550/arXiv.2402.01364) --- Reviews
    methods for maintaining and updating LLM knowledge.
-   [The Emergence of Large Language Models as Tools in Literature
    Reviews](https://doi.org/10.1093/jamia/ocaf063) --- Systematic
    review of LLM use across literature-review workflows.

------------------------------------------------------------------------

## Foundational Papers

-   [Retrieval-Augmented Generation for Knowledge-Intensive NLP
    Tasks](https://arxiv.org/abs/2005.11401) --- Foundational RAG work
    combining parametric generation with retrieved evidence.
-   [Time-Aware Language Models as Temporal Knowledge
    Bases](https://doi.org/10.1162/tacl_a_00459) --- Research on
    representing and probing temporally situated knowledge.
-   [Self-RAG: Learning to Retrieve, Generate, and Critique through
    Self-Reflection](https://arxiv.org/abs/2310.11511) --- Retrieval and
    self-reflection framework for improving grounded generation.
-   [Active Retrieval Augmented
    Generation](https://aclanthology.org/2023.emnlp-main.495/) ---
    Studies adaptive retrieval decisions during generation.

------------------------------------------------------------------------

## Recent Research

-   [Dated Data: Tracing Knowledge Cutoffs in Large Language
    Models](https://arxiv.org/abs/2403.12958) --- Investigates model
    knowledge boundaries and effective cutoffs.
-   [LLMLagBench: Identifying Temporal Training Boundaries in Large
    Language Models](https://arxiv.org/abs/2511.12116) ---
    Benchmark-oriented work for estimating temporal training boundaries.
-   [Test of Time: Rethinking Temporal Signal of Benchmark
    Contamination](https://arxiv.org/abs/2509.00072) --- Examines
    temporal signals used to identify benchmark contamination.
-   [TEMPO: Temporal Enforcement via Mode-Separated Policy Optimization
    for Trustworthy LLM Backtesting](https://arxiv.org/abs/2605.18843)
    --- Explores reward-based temporal enforcement.
-   [All Leaks Count, Some Count More](https://arxiv.org/abs/2602.17234)
    --- Studies interpretable temporal contamination detection and
    mitigation.
-   [Large Language Models for Automated Literature
    Review](https://doi.org/10.48550/arXiv.2412.13612) --- Evaluates
    reference generation, abstract writing, and review composition.
-   [Automated Literature Research and Review-Generation Method Based on
    Large Language Models](https://doi.org/10.1093/nsr/nwaf169) ---
    Describes a literature-research and review-generation pipeline.
-   [Large Language Models Streamline Automated Systematic
    Review](https://doi.org/10.48550/arXiv.2502.15702) --- Preliminary
    study of LLM-assisted systematic-review automation.

------------------------------------------------------------------------

## Methods and Mitigation Approaches

### Retrieval-Augmented Generation

RAG combines a language model with an external retrieval system. It can
reduce knowledge staleness by accessing an updateable corpus. Its
effectiveness depends on retrieval-corpus currency, completeness,
ranking quality, source reliability, and integration of retrieved
evidence.

### Knowledge Editing

Knowledge-editing methods such as ROME and MEMIT attempt to update
specific factual information within model parameters. These methods are
more naturally suited to discrete factual corrections than to
continuously incorporating the large volume of new research
publications.

### Continual Pretraining

Continual learning and model updating can incorporate newer information
into model parameters. However, updating models introduces computational
costs, update-cadence decisions, and risks such as catastrophic
forgetting.

### Prompt- and Reward-Based Temporal Grounding

Explicit temporal constraints can instruct a model to respect a
specified date boundary without changing its parameters. Reward-based
approaches investigate whether model behavior can be encouraged to
comply with temporal constraints. The experiment in this repository
focuses on explicit publication-date prompting.

------------------------------------------------------------------------

## Datasets and Benchmarks

See [datasets/datasets.md](datasets/datasets.md).

Potentially relevant resources include:

-   SciReviewGen.
-   LLMLagBench.
-   Temporal-knowledge benchmarks.
-   Dated-data resources.

Dataset access, licensing, structure, and evaluation suitability should
be checked against the official source before use.

## Tools and Libraries

See [tools/tools.md](tools/tools.md).

Relevant categories include scholarly search and metadata systems, DOI
and bibliographic verification services, retrieval frameworks, LLM
evaluation frameworks, literature-review automation tools, and data
processing and visualization libraries.

## GitHub Implementations

See
[implementations/github-repositories.md](implementations/github-repositories.md).

Implementations should be evaluated according to source-code
availability, documentation quality, maintenance status,
reproducibility, licensing, connection to recognized research, and
availability of datasets, weights, and benchmark protocols.

## Tutorials and Learning Resources

See [tutorials.md](tutorials.md).

Recommended learning areas:

-   Retrieval-Augmented Generation.
-   LLM hallucination evaluation.
-   Temporal knowledge and model knowledge cutoffs.
-   Systematic literature-review methodology.
-   Scholarly citation verification.
-   Reproducible experimental research.
-   AI-assisted coding and debugging.

------------------------------------------------------------------------

## Verification and Research Integrity

References and research resources should not be accepted solely because
an AI system generated them.

For scholarly papers, verify:

1.  Title.
2.  Author names.
3.  Publication year.
4.  Publication venue.
5.  DOI, arXiv identifier, PMID, or other persistent identifier where
    applicable.
6.  Whether the identifier resolves to the same work.
7.  Whether the publication version and date are appropriate.
8.  Whether the cited source actually supports the associated claim.

A failed DOI lookup alone does not prove that a paper is fabricated.
Preprint and formally published versions may also have different
publication dates and identifiers.

AI tools are used as supervised research assistants rather than
authorities. The project aims to preserve the distinction between
AI-generated suggestions and human-verified decisions, report actual
results, document limitations, and respect third-party copyright,
dataset licensing, privacy, and usage restrictions.

------------------------------------------------------------------------

## License

The repository's original documentation and curation material is
released under the [MIT License](LICENSE).

Research papers, datasets, code, figures, and third-party resources
remain subject to their respective copyright and licensing terms.

Do not redistribute copyrighted papers or restricted datasets unless
redistribution is explicitly permitted. Link to official publisher, DOI,
arXiv, PubMed, or other authorized sources where appropriate.

------------------------------------------------------------------------

**Repository purpose:** To investigate how temporal knowledge boundaries
affect LLM-generated literature reviews, evaluate citation reliability,
and document practical methods for more temporally consistent and
verifiable AI-assisted academic research.
