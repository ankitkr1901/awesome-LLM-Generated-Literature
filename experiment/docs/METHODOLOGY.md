
# 3. Research Methodology

## 3.1 Research Design

This study employed a controlled comparative design to investigate
whether explicit publication-date boundary instructions influence
the temporal compliance of large language models when generating
literature reviews.

Two prompting conditions were compared. Condition A used a standard
literature-review prompt. Condition B used the same underlying prompt
with an additional instruction requiring the model to include only
scholarly works published on or before 31 December 2024, inclusive.
The instruction also required uncertain publication dates to be
omitted or flagged rather than guessed.

The experiment consisted of five matched prompt pairs, producing
ten literature reviews in total.

## 3.2 Experimental Conditions

### Condition A: Standard Prompt

The model received the standard literature-review prompt without
an explicit publication-date restriction.

### Condition B: Explicit Temporal Boundary

The model received the same underlying literature-review prompt,
preceded by an explicit instruction to respect the publication-date
boundary of 31 December 2024. The instruction specified that
unverified publication dates should not be guessed.

The comparison was designed to isolate the effect associated with
adding an explicit temporal boundary instruction.

## 3.3 Data Collection

Ten literature reviews were generated manually through the
ChatGPT user interface. The five matched pairs were identified
using pair IDs P01 through P05.

The generation order was randomized using seed 2026. The generated
reviews were saved as Word documents and subsequently converted
into text files for analysis.

The model selector label and visible generation settings were
recorded in the generation log.

The generated reviews were retained for analysis. Their observed
lengths exceeded the originally intended target of 800–1,000 words.
This deviation was documented rather than modifying the generated
outputs after collection.

## 3.4 Citation Extraction

References were extracted from the bibliography sections of the
generated literature reviews. The extraction process identified
candidate bibliography entries and assigned run IDs and reference
numbers to support traceability.

The initial extraction identified 100 candidate entries. One entry
was determined to be commentary rather than a complete bibliographic
reference. The final analysis therefore considered 99 reference
instances.

## 3.5 Bibliographic Verification

Candidate references were assessed using bibliographic metadata
services, including Crossref and OpenAlex, together with additional
record checks where appropriate.

Manual decisions were recorded using four categories:

- MATCH: the bibliographic record was identified and considered
  consistent with the cited reference.
- PARTIAL_MATCH: a record was identified, but one or more
  bibliographic details remained inconsistent or unresolved.
- DOI_MISMATCH: a discrepancy involving the cited DOI was identified.
- NOT_APPLICABLE: the entry was not a complete bibliographic reference.

A failed DOI lookup was not treated as sufficient evidence that
a reference was fabricated. Preprint and published versions were
also distinguished where relevant.

## 3.6 Temporal Classification

The temporal boundary was set to 31 December 2024, inclusive.

References were classified according to their candidate publication
year:

- WITHIN_CUTOFF: publication year on or before 2024.
- POST_CUTOFF: publication year after 2024.
- UNKNOWN_DATE: publication year could not be established.

Publication-year candidates and independently verified dates
were distinguished in the audit records. Where a preprint and a
later proceedings or journal version differed, the cited version
was relevant to the cutoff assessment.

## 3.7 Evaluation Measures

The primary outcome was the proportion of dated citation instances
published after the cutoff:

Post-cutoff rate = Post-cutoff citation instances /
                   All dated citation instances

The secondary outcome was bibliographic match rate:

Bibliographic match rate = MATCH instances /
                           All analyzed citation instances

A sensitivity analysis was also conducted using only references
classified as MATCH.

## 3.8 Paired Analysis

Results were compared within each of the five matched prompt pairs.
For each pair, the post-cutoff citation rate under Condition A
was compared with the corresponding rate under Condition B.

The mean paired reduction was calculated as the average of the
five pair-specific differences.

Given the small number of matched pairs, the analysis emphasized
descriptive comparisons and cautious interpretation rather than
strong claims of statistical generalizability.

## 3.9 Research Limitations

The experiment involved five matched pairs and ten generated
literature reviews. Consequently, the findings should not be
assumed to generalize to all language models, prompts, or subject
areas.

The study measured observable compliance with an explicit
publication-date instruction. It did not directly measure the
model's internal training-data cutoff or establish the exact
boundary of its internal knowledge.

Manual bibliographic assessment and publication-version
distinctions also introduce potential uncertainty. These
limitations were retained when interpreting the results.
