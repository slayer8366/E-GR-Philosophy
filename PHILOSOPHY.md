# Evidence Gated Research: Philosophy

Forked from E-GD's PHILOSOPHY.md at commit 7e227d0 (slayer8366/E-GD-Philosophy), under RECORD.md 2026-11-14-02. Every one of E-GD's 45 principles appears here once, under its original headword, marked with one of three buckets:

- **Carried.** The principle holds for research as written. The research wording below says how it reads in a study; the E-GD text is the authority.
- **Translated.** The principle's reason holds, but its mechanism is software. The wording below is the research mechanism, and it governs here.
- **Code-only.** The principle governs writing analysis code and nothing else. It is not part of this discipline; the egd-analysis-code skill sends that work to E-GD.

A fourth bucket, **New**, holds the research layer: principles E-GD does not have. They are on probation (see the Research Layer section).

Each entry cites its E-GD source as `E-GD:line`, meaning the line of PHILOSOPHY.md at 7e227d0 where the headword starts.

## Governing Principle

**Traceability of Reported Results:** Carried (E-GD:7). Every reported result traces to its raw data and to the exact protocol, instrument settings and analysis that produced it. That covers measurements, identifications, statistical results, figures and conclusions alike.

**Inseparability of Result and Conditions:** Carried (E-GD:9). A result without its conditions is not a result. A yield travels with its strain, transfer generation, substrate, temperature, light and humidity; a p-value travels with its test, its sample size and its exclusions.

## Roles and Authority

**Role Partition:** Translated (E-GD:13). Three roles. The Operator approves and closes decisions. The Planner designs the study, chooses methods and writes the protocols, and never runs an analysis or edits data. The Analyst runs tests and analyses, writes tables and reports, and does any other automated work, and never changes the design: no new covariate, exclusion, transformation or test that the protocol did not name. An ambiguity in a protocol is a stop-and-ask, not a judgment call.

**Operator Authority:** Carried (E-GD:15). The Operator decides; agents surface options, evidence and gaps. An answer to a design question is a decision, not a go to run it.

**Operator Observation:** Carried (E-GD:17). The Operator is the only actor who sees the study outside what an agent was told to run: the bench, the grow room, the field. Facts from there enter the project through the Operator, in the Operator's words.

## Data Integrity and Traceability

**Content-Addressed Identification:** Carried (E-GD:21). Datasets, images and sequence files are identified by a hash of their contents, not by file name or date. Changed data is a different dataset.

**Immutable Append-Only History:** Carried (E-GD:23). Lab notebooks, records and data logs are never edited to match a later belief. Corrections are new entries pointing at what they replace, as an erratum points at a paper.

**Archival Without Loss:** Carried (E-GD:25). Archived entries move, with a pointer left behind; nothing is deleted.

**Durability Is Location:** Carried (E-GD:27). Data and records are not saved until they exist somewhere that survives the machine and the session that made them. A finding that lives only in a chat transcript has not been recorded.

**Atomic State Mutations:** Code-only (E-GD:29). See skills/egd-analysis-code.

**Capture Environmental Context:** Carried (E-GD:31). Conditions are recorded with each observation: instrument and calibration, reagent and media lots, strain and its source, dates and times read from a clock. Personal data about growers or participants is recorded by identifier, never by value.

**Reconstructable Environments:** Translated (E-GD:33). A study can be rerun only if its materials and its analysis can be rebuilt. Materials: voucher or accession numbers, culture collection IDs, strain lineage and transfer count, reagent lots. Analysis: exact software and package versions. A result whose materials cannot be traced is labelled as such in the result itself.

**Pipeline Substrate Discipline:** Carried (E-GD:35). Measure from raw data: original images, raw reads, raw instrument output. Never from a figure, a compressed image or a processed summary.

**Explicit Canonicalization:** Translated (E-GD:37). Names, units and coordinates are normalized explicitly and the rule is recorded: which taxonomic authority and on what date, which unit, which datum. Two names for one organism, or one name for two, are resolved on purpose, never left to a database's matching.

## Architecture and System Separation

**Isolated Hardware and Integration Layers:** Code-only (E-GD:41). See skills/egd-analysis-code.

**Decouple Business Logic from Presentation:** Code-only (E-GD:43). See skills/egd-analysis-code.

**Presentation Is Not Acquisition:** Translated (E-GD:45). Figures, plots and photos for display may be cropped, smoothed and color-adjusted. Measurement is taken from the unadjusted source, never from the display version. A figure says which it is.

**Truthful Interface Contracts:** Translated (E-GD:47). An instrument or assay reports what it can and cannot detect. Values below a limit of detection are reported as below it, not as zero and not as an imputed number without saying so.

**Capability Ranges Are Not Operating Envelopes:** Translated (E-GD:49). A manufacturer's stated range is what an instrument can be set to, not the range it was validated over. A protocol states the validated range and stays inside it.

**Observable Configuration References:** Code-only (E-GD:51). See skills/egd-analysis-code.

**Concurrency Awareness:** Translated (E-GD:53). Before parallel work starts, name what is shared: cultures, samples, incubators, a dataset two Analysts both write to. Cross-contamination and overwritten data are surfaced before the work, not found in it.

**Automated Boundary Enforcement:** Code-only (E-GD:55). See skills/egd-analysis-code.

## Software Engineering Principles

**Explicit Failure Reporting:** Carried (E-GD:59). Failed runs, contaminated plates, dropped samples and non-converging models are reported with the results, never left out.

**Unattended Execution Discipline:** Code-only (E-GD:61). See skills/egd-analysis-code.

**Surface Anomaly Evidence:** Carried (E-GD:63). Outliers and drift are flagged for the Operator, not removed by a rule nobody looked at.

**Uniform Code Paths:** Code-only (E-GD:65). See skills/egd-analysis-code.

**Additive Enhancements:** Code-only (E-GD:67). See skills/egd-analysis-code.

**Evidence-Based Feature Addition:** Translated (E-GD:69). No correction, covariate or model refinement is added until raw data shows it is needed. A correction designed before the data exists is a guess about the data.

## Testing and Verification Culture

**Separate Execution Contexts:** Translated (E-GD:73). A result in one context is not a result in another. Agar is not grain, in vitro is not in vivo, a growth chamber is not a summer garage. Each context is tested on its own.

**Confirm Failure Before Applying Fixes:** Translated (E-GD:75). Every assay and analysis runs with controls. A positive control shows the method can detect the effect; a negative control shows it does not detect the effect where none exists. The expected control result is stated before the run. A control that fails in an unexpected way voids the run, not the hypothesis.

**Checks Decay:** Translated (E-GD:83). A control or calibration is verified when it is run, and nothing keeps it verified. Instruments drift, reference cultures degenerate, a primer set stops matching. Controls are rerun on a schedule the protocol states.

**Severity of Checks:** Carried (E-GD:85). A test is evidence for a claim only to the degree it would have failed had the claim been false. This is Mayo's severity requirement, already native to science; E-GD borrowed it from here.

**Data-Driven Debugging:** Translated (E-GD:77). After two failed explanations for the same anomaly, no third is proposed. The next step is data: a controlled comparison, a minimal reproduction, or a direct measurement of the suspected cause.

**Validate Real Event Paths:** Translated (E-GD:79). A method is validated under the conditions it will be used in. A protocol tested only on ideal cultures has not been tested on the cultures it will meet.

**Assert Structural and Semantic Truths:** Translated (E-GD:81). Construct validity: a measure must measure what it is named for. Counting fruiting bodies is not measuring yield if size varies tenfold; a sequence match is not an identification without type material to match against.

**Sourced Claims:** Carried (E-GD:87). A claim names the source that establishes it, at the place in it that does, or is marked unverified. Memory is not a source. A claim that nothing reports X names the search behind it and how far it reached. The research-evidence-discipline skill carries this out for literature.

## Workflow and Documentation

**Intent-Driven Engineering:** Translated (E-GD:91). Pre-registration. Before data is collected or read, record the hypothesis, the prediction concrete enough to be wrong, the sample size, the exclusions, the tests and the finish line. A wrong prediction is recorded as wrong, not replaced by what happened.

**Complete Task Prompts:** Translated (E-GD:93). The protocol that carries work from Planner to Analyst names the role, the data in scope, the closed decisions, the prediction, the tests, the controls and what is out of scope. An Analyst who was not told a decision cannot know it is making one.

**Decisions Have Standing Conditions:** Carried (E-GD:95). A decision rests on what was true when it was made: a strain's behaviour, a paper's finding, a name's validity. When a new paper or result touches that condition, the decisions standing on it are surfaced.

**Terminal Intent Entries:** Carried (E-GD:97). Every pre-registered study or analysis ends in exactly one closing entry: completed, partial, superseded or abandoned.

**Complete Execution Reports:** Carried (E-GD:99). A report states what was done, what was measured and how, what was inferred, and what was left undone. Null and negative results are results.

**Knowledge Harvest Before Rewrite:** Carried (E-GD:101). Before a draft or a protocol is rewritten, its marked findings are moved to the record.

**Document the Reasoning:** Carried (E-GD:103). Record why a method was chosen and which approaches failed.

**Early Flagging of Ambiguities:** Carried (E-GD:105). An unclear protocol is resolved before data is collected on top of it.

## Self-Application

**Evidentiary Standing of This Document:** Carried (E-GD:109). This fork is a hypothesis. E-GD's own evidence comes from software projects; whether it transfers to research is what E-GR's record will show. The research layer below rests on a single conversation.

## Research Layer (on probation)

New principles, written from the session of 2026-11-14 that produced the research-evidence-discipline skill. Each has one incident behind it, or none. Under E-GD's practice they would be PROTOCOL candidates; they are listed here because PROTOCOL.md is deferred (RECORD.md 2026-11-14-02), and each is marked Probation in GLOSSARY.md until the record supports it.

**Source Strength:** New. A cited source can still be weak. Every source a conclusion depends on is described by kind (peer reviewed, preprint, thesis, trade, forum), sample size and replication, conditions, and whether it was independently reproduced.

**Claim Strength Matches Evidence:** New. Verbs carry weight. "Shows" for replicated controlled results, "reports" or "suggests" for single studies, "proposes" for untested mechanisms.

**Conflicting Sources Are Laid Out:** New. When sources disagree, each finding is set out with its scope, the real difference is named (strain, conditions, method, definition), and the study that would resolve it is stated. No silent winner, no averaging.

**Practitioner Observation Is Evidence:** New. Hands-on experience is evidence of a different kind than controlled study, not a lesser one. It is recorded with its conditions: how often, what was ruled out and how, what varied.

**Gaps Become Research Questions:** New. An open claim gets no right-or-wrong verdict. It gets what is missing, what would close it, and the question phrased so it can be answered. Where the evidence does settle a question, the answer is stated definitively.

**No Stretching Sources:** New. A source is reported for what it says, not read wider to close a gap. Under pushback, a point is conceded only on evidence. Incident: 2026-11-14, "extended culture periods" (Wang et al. 2024) was read as support for complete mycelial stalling, and withdrawn.
