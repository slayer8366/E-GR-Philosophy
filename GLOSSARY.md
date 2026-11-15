# E-GR Glossary

Machine-facing. `check_transfer.py` verifies it against E-GD's PHILOSOPHY.md: every E-GD headword appears here exactly once with a bucket, and once in E-GR's PHILOSOPHY.md. Agents use it as a headword lookup.

Columns: the headword, kept exactly as E-GD wrote it; its E-GD source line in PHILOSOPHY.md at commit 7e227d0; its bucket (Carried, Translated, Code-only, New); and its status here.

Status values: **Active** governs E-GR work. **Moved to skill** governs analysis code only, through skills/egd-analysis-code, and is enforced by E-GD. **Probation** is a research-layer candidate that has not yet earned standing.

Headwords are stable identifiers. To retire one, supersede it in RECORD.md and mark it here, leaving the row in place.

| Headword | E-GD source | Bucket | Status |
|---|---|---|---|
| Traceability of Reported Results | E-GD:7 | Carried | Active |
| Inseparability of Result and Conditions | E-GD:9 | Carried | Active |
| Role Partition | E-GD:13 | Translated | Active |
| Operator Authority | E-GD:15 | Carried | Active |
| Operator Observation | E-GD:17 | Carried | Active |
| Content-Addressed Identification | E-GD:21 | Carried | Active |
| Immutable Append-Only History | E-GD:23 | Carried | Active |
| Archival Without Loss | E-GD:25 | Carried | Active |
| Durability Is Location | E-GD:27 | Carried | Active |
| Atomic State Mutations | E-GD:29 | Code-only | Moved to skill |
| Capture Environmental Context | E-GD:31 | Carried | Active |
| Reconstructable Environments | E-GD:33 | Translated | Active |
| Pipeline Substrate Discipline | E-GD:35 | Carried | Active |
| Explicit Canonicalization | E-GD:37 | Translated | Active |
| Isolated Hardware and Integration Layers | E-GD:41 | Code-only | Moved to skill |
| Decouple Business Logic from Presentation | E-GD:43 | Code-only | Moved to skill |
| Presentation Is Not Acquisition | E-GD:45 | Translated | Active |
| Truthful Interface Contracts | E-GD:47 | Translated | Active |
| Capability Ranges Are Not Operating Envelopes | E-GD:49 | Translated | Active |
| Observable Configuration References | E-GD:51 | Code-only | Moved to skill |
| Concurrency Awareness | E-GD:53 | Translated | Active |
| Automated Boundary Enforcement | E-GD:55 | Code-only | Moved to skill |
| Explicit Failure Reporting | E-GD:59 | Carried | Active |
| Unattended Execution Discipline | E-GD:61 | Code-only | Moved to skill |
| Surface Anomaly Evidence | E-GD:63 | Carried | Active |
| Uniform Code Paths | E-GD:65 | Code-only | Moved to skill |
| Additive Enhancements | E-GD:67 | Code-only | Moved to skill |
| Evidence-Based Feature Addition | E-GD:69 | Translated | Active |
| Separate Execution Contexts | E-GD:73 | Translated | Active |
| Confirm Failure Before Applying Fixes | E-GD:75 | Translated | Active |
| Data-Driven Debugging | E-GD:77 | Translated | Active |
| Validate Real Event Paths | E-GD:79 | Translated | Active |
| Assert Structural and Semantic Truths | E-GD:81 | Translated | Active |
| Checks Decay | E-GD:83 | Translated | Active |
| Severity of Checks | E-GD:85 | Carried | Active |
| Sourced Claims | E-GD:87 | Carried | Active |
| Intent-Driven Engineering | E-GD:91 | Translated | Active |
| Complete Task Prompts | E-GD:93 | Translated | Active |
| Decisions Have Standing Conditions | E-GD:95 | Carried | Active |
| Terminal Intent Entries | E-GD:97 | Carried | Active |
| Complete Execution Reports | E-GD:99 | Carried | Active |
| Knowledge Harvest Before Rewrite | E-GD:101 | Carried | Active |
| Document the Reasoning | E-GD:103 | Carried | Active |
| Early Flagging of Ambiguities | E-GD:105 | Carried | Active |
| Evidentiary Standing of This Document | E-GD:109 | Carried | Active |
| Source Strength | none | New | Probation |
| Claim Strength Matches Evidence | none | New | Probation |
| Conflicting Sources Are Laid Out | none | New | Probation |
| Practitioner Observation Is Evidence | none | New | Probation |
| Gaps Become Research Questions | none | New | Probation |
| No Stretching Sources | none | New | Probation |

## Enforcement

E-GR's ENFORCEMENT.md holds an entry for each Translated headword, added under RECORD.md 2026-11-14-07, and `check_transfer.py` verifies that. Carried headwords have no E-GR entry yet: for those, an agent follows the E-GD enforcement entry of the same name, read in the research terms of E-GR's PHILOSOPHY.md, and flags any place the two do not fit. Code-only headwords are enforced by E-GD through skills/egd-analysis-code.

## Marker vocabulary

As E-GD's GLOSSARY.md at 7e227d0: `LESSON:`, `OPEN:`, `CLOSED:`, `DEFER:`. Additions are recorded in RECORD.md and added here.
