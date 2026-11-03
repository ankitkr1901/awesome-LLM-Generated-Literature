# Data Dictionary

| Field | Meaning |
|---|---|
| run_id | Unique generation run identifier |
| reference_number | Reference position in a generated review |
| reference_text | Extracted bibliography entry |
| manual_decision | Manual bibliographic assessment |
| manual_notes | Notes on manual verification |
| candidate_verified_year | Candidate publication year |
| cutoff_status_final | Within-cutoff, post-cutoff, or unknown |
| condition | A or B experimental condition |
| pair_id | Matched prompt pair identifier |

Manual decisions:
- MATCH: bibliographic record identified and consistent
- PARTIAL_MATCH: some metadata discrepancy remains
- DOI_MISMATCH: DOI discrepancy identified
- NOT_APPLICABLE: entry is not a complete reference
