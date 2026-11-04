# ACM Single-Column Paper — Expanded Reference Version

This revision expands the related-work discussion and includes 23 BibTeX entries from the project's existing research bibliography, plus the temporal reasoning paper already present in the extracted-reference appendix. The added works are cited in the manuscript so the bibliography is not simply an uncited dump.

## Files
- `ACM_Single_Column.pdf` — compiled 8-page single-column ACM manuscript
- `ACM_Single_Column.tex` — editable source
- `references.bib` — BibTeX database (23 entries)
- `ACM_Single_Column.bbl` — generated ACM-formatted bibliography
- `figures/` — the three study figures

## Compile
Use a TeX installation containing `acmart`, `ACM-Reference-Format.bst`, and BibTeX:

```bash
pdflatex ACM_Single_Column.tex
bibtex ACM_Single_Column
pdflatex ACM_Single_Column.tex
pdflatex ACM_Single_Column.tex
```

## Reference verification note
The BibTeX records were carried forward from the project's existing `references_review_background.bib`, with the Tan et al. temporal-reasoning record added from the extracted-reference appendix. This is an expanded cited bibliography, not a claim that every metadata field has been independently rechecked against the publisher. BibTeX reports missing optional metadata for some preprints and proceedings records; verify author lists, publication status, venue, pages, and DOI against publisher/ACL/arXiv records before formal submission. In particular, do not treat an arXiv posting year and a later proceedings publication year as interchangeable.

This is a generic ACM `acmart` manuscript-mode student paper, not a camera-ready submission to a named ACM venue.
