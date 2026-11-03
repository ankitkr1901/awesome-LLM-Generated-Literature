
# 5. Discussion

## 5.1 Interpretation of the Findings

The findings indicate that adding an explicit publication-date
boundary instruction was associated with improved temporal compliance
in the generated literature reviews.

Condition A produced 15 post-cutoff citation instances among 51
references, whereas Condition B produced none among 48 references.
The observed difference was 29.41 percentage points.

Importantly, this pattern was consistent across all five matched
pairs. The sensitivity analysis, which retained only references
classified as bibliographic matches, also showed a reduction.
Its mean paired reduction was 27.14 percentage points.

These results suggest that a clearly stated temporal constraint
can influence the publication dates of references selected or
generated during literature-review generation.

## 5.2 Implications for Literature Review Generation

The findings have practical implications for researchers using
large language models to support literature reviews.

A model may produce a plausible-looking bibliography without
necessarily respecting a researcher's intended temporal scope.
An explicit cutoff instruction may help reduce this problem.

However, a date instruction should not replace independent
bibliographic verification. Researchers should still check titles,
authors, publication venues, DOIs, and the distinction between
preprint and formally published versions.

A useful research workflow should therefore combine explicit
prompt constraints with external reference verification.

## 5.3 Bibliographic Reliability

Condition B also showed a higher bibliographic match rate in this
sample. However, this result should be interpreted cautiously.

The experiment was not designed with a sufficiently large sample
to establish that explicit temporal instructions generally improve
bibliographic accuracy. The observed difference may be influenced
by the small number of generated reviews, the topics selected,
and the unresolved partial-match cases.

Temporal compliance and bibliographic correctness should therefore
be treated as separate dimensions of citation reliability.

## 5.4 Relationship to Knowledge Boundaries

The experiment evaluates whether a model follows an explicitly
provided publication-date boundary. It does not directly reveal
the model's internal training-data cutoff or establish when the
model acquired particular information.

A model can cite a post-cutoff work because of information available
through its context, retrieval, updates, or other mechanisms.
Likewise, a model can omit a recent work even if it has information
about that work.

Consequently, the results concern observable temporal instruction
compliance rather than the model's internal knowledge boundary.

# 6. Limitations

## 6.1 Small Sample Size

The experiment included five matched pairs and ten literature
reviews. This limited sample restricts statistical power and
generalizability.

The descriptive consistency across pairs is encouraging, but
larger studies are needed to determine whether the observed
pattern holds across different models, domains, and prompts.

## 6.2 Single Model Interface

The reviews were generated manually through the ChatGPT interface.
The findings should not automatically be generalized to other
models, model versions, APIs, or generation settings.

## 6.3 Review Length Deviation

The generated reviews exceeded the originally intended target
of 800–1,000 words. This deviation was documented, and the
original outputs were retained rather than edited after generation.

Differences in review length may have influenced the number of
references produced.

## 6.4 Bibliographic Uncertainty

Although 93 entries were classified as MATCH, five were classified
as PARTIAL_MATCH and one as DOI_MISMATCH.

Automated metadata services may return incomplete records, and
preprint and publication versions can have different dates or
identifiers. These cases require careful interpretation.

## 6.5 Publication Date Versus Internal Knowledge

The experiment measured compliance with an explicit publication-date
constraint. It did not measure the model's internal knowledge
cutoff, training-data composition, or exact knowledge acquisition
dates.

## 6.6 Limited Statistical Generalizability

Only five paired comparisons were available. The two-sided exact
sign test yielded p = 0.0625, which does not meet the conventional
0.05 threshold.

The results should therefore be presented as preliminary,
descriptive evidence rather than definitive statistical proof.

# 7. Conclusion

This study investigated whether an explicit publication-date
boundary instruction influences the temporal compliance of
large language models when generating literature reviews.

Across five matched prompt pairs, the standard prompting condition
produced a post-cutoff citation rate of 29.41%, while the condition
containing an explicit publication-date boundary produced a rate
of 0%.

The mean paired reduction was 29.64 percentage points. A sensitivity
analysis restricted to bibliographically matched references
also showed a reduction, with a mean paired difference of
27.14 percentage points.

The findings suggest that explicitly stating a publication-date
boundary may be a useful practical measure for reducing
post-cutoff citations in generated literature reviews.

Nevertheless, temporal instruction compliance does not guarantee
bibliographic accuracy. Independent verification remains necessary,
particularly when references involve preprints, later proceedings,
or uncertain publication metadata.

Future research should examine larger samples, multiple language
models, different academic domains, and repeated generations under
controlled settings. Such work could provide stronger evidence
about the reliability of temporal constraints in AI-assisted
academic research.

Overall, this study provides preliminary evidence that explicit
temporal instructions can improve observable date-boundary
compliance, while highlighting the continuing need for
independent citation verification.
