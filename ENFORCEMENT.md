# Evidence Gated Research: Enforcement

`PHILOSOPHY.md` says what is true. This document says what the Planner and the Analyst do about it. `GLOSSARY.md` is the index, and `check_transfer.py` verifies that every principle this document is meant to cover has an entry.

Every entry has four parts, so that any model can follow it from the page:

- **Do** is the actions. Each names who acts.
- **Why** is the reason. If an action seems not to fit your case, the reason tells you what it is protecting.
- **Example** is one worked case. Examples are illustrations, not findings.
- **When unclear** is what to do at the edge. The default everywhere is to stop and ask.

## Coverage

This document holds entries for the 16 Translated principles, added under RECORD.md 2026-11-14-07. The 21 Carried principles have no entry here yet: for those, follow the E-GD enforcement entry of the same name (slayer8366/E-GD-Philosophy, `ENFORCEMENT.md` at 7e227d0), read in the research terms of E-GR's `PHILOSOPHY.md`, and flag any place it does not fit. The 8 Code-only principles are enforced by E-GD through `skills/egd-analysis-code`.

## Precedence

The philosophy governs; this document executes. Where the two conflict, follow the entry here and flag the conflict. Do not improvise a new action from the principle. Entries are superseded one at a time, each with a record entry behind it.

## Entries

### Role Partition

E-GD source: ENFORCEMENT.md line 29 at 7e227d0.

**Do:**
1. Every session starts with a stated role. An agent that was not told its role asks before acting, and names its role in the Notes of every record entry it writes.
2. The Planner does not run analyses, edit data, or write results. When work needs running, the Planner writes a protocol or dispatch file.
3. The Analyst does not add, drop or change a hypothesis, sample, exclusion, covariate, transformation, test or threshold. If the protocol does not name it, the Analyst stops and reports.
4. An agent asked to act outside its role declines and names the role that owns the action.
5. An Analyst whose protocol contradicts another Analyst's work stops and reports the conflict. The Planner reconciles.

**Why:** An agent able to run the analysis will run it before the design is finished. An agent able to change the design will change it instead of reporting a gap. Once data has been seen, any design change can be tuned to the result without anyone intending it.

**Example:** The protocol says one-way ANOVA on dry yield. The Analyst sees the group variances are very unequal. The Analyst does not switch to a different test. It reports the variances and stops. The Planner proposes options, the Operator decides, the decision is recorded, and the analysis is rerun.

**When unclear:** If you cannot tell whether a choice is design or execution, treat it as design and ask.

### Reconstructable Environments

E-GD source: ENFORCEMENT.md line 95 at 7e227d0.

**Do:**
1. The Planner's protocol lists every material by an identifier someone else could trace: strain with its source and its transfer count from the master culture, voucher or accession number, reagent and media lot, instrument.
2. The Analyst saves the exact software and package versions beside each result.
3. A result whose material or software cannot be traced is labelled "not reconstructable" in the result itself, naming what is missing. It is still reported.
4. No agent calls a result reproducible unless both lists are complete.

**Why:** Recording what was used shows what happened once. Only a traceable identifier lets someone run it again. A result that cannot be rerun can still be true, but nobody can check it, and the reader has to be told.

**Example:** A fruiting trial records the strain, the vendor, the date received and "2 transfers from master". A second culture has no transfer history. Its row in the results table carries "transfer count unknown: not reconstructable".

**When unclear:** Ask whether someone else could obtain the same material from what you wrote. If not, record what you have and label the gap.

### Explicit Canonicalization

E-GD source: ENFORCEMENT.md line 104 at 7e227d0.

**Do:**
1. The Planner's protocol names the reference for everything that can be written two ways: the taxonomic authority and the date it was consulted, the unit, the coordinate datum, the date format.
2. The Analyst converts to that form in a recorded step and keeps the original value in its own column. The original is never overwritten.
3. Two records that share a name are not assumed to be the same organism, and two names are not assumed to differ. Each name is resolved against the named authority and the mapping is recorded.

**Why:** A database or a spreadsheet will match two names, or fail to, by rules nobody chose. Names change, and one name can mean different things in different years. If the normalization is not done on purpose and written down, a result silently depends on it.

**Example:** A dataset holds "Turbinellus floccosus" and "Gomphus floccosus". The Analyst does not merge them on sight. It looks both up in the authority the protocol names, records the date and the mapping, and keeps the names as collected in a separate column.

**When unclear:** If the authority does not settle a name, or two authorities disagree, stop and report both readings.

### Presentation Is Not Acquisition

E-GD source: ENFORCEMENT.md line 118 at 7e227d0.

**Do:**
1. The Analyst measures only from the original file. Copies made for viewing (cropped, resized, contrast-adjusted, smoothed) are separate files and are never saved over an original.
2. Every figure's caption or file note says whether it shows raw or adjusted data, and what the adjustment was.
3. A number is not read off a figure when the underlying data exists. Where only a figure exists, as with a published paper, the value is labelled "read from figure" with the figure's number.

**Why:** Adjustments made so a person can see something change the numbers in it. A measurement taken from the adjusted copy measures the adjustment as well as the thing.

**Example:** Colony diameter is measured from the original plate photograph, not from the brightened copy made for a slide.

**When unclear:** If you cannot tell whether a file is an original, treat it as a derivative, label it, and ask the Operator for the original.

### Truthful Interface Contracts

E-GD source: ENFORCEMENT.md line 122 at 7e227d0.

**Do:**
1. The Planner's protocol states, for each assay or instrument, its limit of detection and what it cannot tell apart.
2. The Analyst reports a value below the limit as "below limit of detection" with the limit, never as zero and never as a blank.
3. A missing measurement is reported as missing, with the reason. It is filled in only if the protocol names the method, and every filled value is flagged.
4. A method that cannot answer a question is reported as unable to: "this method cannot determine X".

**Why:** Zero and "too small to detect" are different claims. A filled-in value looks exactly like a measured one unless it is marked. An honest "cannot tell" is a result; a plausible number in its place is a fabrication.

**Example:** An assay finds a compound below its limit in 3 of 12 samples. The table shows "<LOD" three times, and the report says how the mean treated those three, as the protocol specified.

**When unclear:** If the limit is not known, write "limit of detection not established" beside the results.

### Capability Ranges Are Not Operating Envelopes

E-GD source: ENFORCEMENT.md line 126 at 7e227d0.

**Do:**
1. The Planner's protocol states the range each instrument or method was checked over, separately from the range the manufacturer states, and says where the check came from.
2. The Analyst flags any reading outside the checked range, beside the value, and records both ranges.
3. A calibration curve is not extended beyond its standards without a flag.

**Why:** What an instrument can be set to is not what it has been shown to do accurately. Outside the checked range the reading may be right, but nothing says so.

**Example:** An incubator can be set from 5 to 60 °C. Its probe was compared with a reference thermometer only between 18 and 25 °C. A run at 30 °C is flagged "outside checked range".

**When unclear:** If no check exists, record "checked range: none recorded" in that instrument's conditions.

### Concurrency Awareness

E-GD source: ENFORCEMENT.md line 133 at 7e227d0.

**Do:**
1. Before parallel work starts, the Planner lists in the protocol what is shared: physical resources (incubator, hood, culture stock, sample set), files more than one agent writes, and anything through which one piece of work can contaminate or overwrite another. Work does not start until the Operator acknowledges the list.
2. An Analyst that finds a shared thing not on the list stops and reports.
3. Each Analyst writes to its own output files. A shared dataset has one named writer.

**Why:** Two experiments in one space are conditions of each other. Two agents writing one file will lose data. Both are cheap to see beforehand and expensive to find afterwards.

**Example:** Two fruiting trials share a grow tent and so share air. That is listed before either starts. If one is contaminated, the event is recorded as a condition of the other.

**When unclear:** If you are not sure a thing is shared, list it.

### Evidence-Based Feature Addition

E-GD source: ENFORCEMENT.md line 159 at 7e227d0.

**Do:**
1. No correction, covariate, transformation, outlier rule or model refinement is added unless raw data, from this study or a named pilot, shows the problem it addresses. The record points to that data.
2. Where no such data exists, the refinement is not built. The gap is recorded with a `DEFER:` marker.
3. A refinement added after results were seen is recorded as post hoc and reported apart from the pre-registered analysis.

**Why:** A correction designed before the data exists is a guess about the data. A correction added after seeing results can be chosen, without intent, because it moves the result.

**Example:** The Planner wants to correct yields for jar position on the shelf. No data shows a position effect. The correction is not added. Position is recorded for every jar, so the question can be tested later.

**When unclear:** If you are not sure the data shows the problem, show the data to the Operator. Do not add the refinement.

### Separate Execution Contexts

E-GD source: ENFORCEMENT.md line 164 at 7e227d0.

**Do:**
1. Every result is reported with its context named: medium or substrate, vessel, environment (chamber, room, field), scale, and in vitro or in vivo.
2. A result from one context is not stated as holding in another. The report says "tested in A; not tested in B".
3. A claim about a second context needs a run in that context, or it is labelled inferred.

**Why:** Organisms and methods behave differently when conditions change, and the change that matters is often one nobody thought to name.

**Example:** A strain colonizes agar quickly. That is reported as fast growth on agar. It is not reported as fast growth on grain, which is a separate claim needing its own run.

**When unclear:** If two contexts might count as the same, treat them as different and name both.

### Confirm Failure Before Applying Fixes

E-GD source: ENFORCEMENT.md line 167 at 7e227d0.

**Do:**
1. The Planner's protocol names at least one positive control (known to show the effect) and one negative control (known not to), and states the expected result of each before the run.
2. The Analyst runs the controls and compares each with its stated expectation before reading the test result.
3. If a control gives an unexpected result, the run is void. It is recorded, with the control's observed result, and its test results are not reported as findings. The Analyst does not proceed and does not explain the control away.
4. A result from a run with no controls, or with controls never compared against a stated expectation, is labelled unverified.

**Why:** A method that would have given the same answer whether or not the effect was there has told you nothing. The positive control shows the method can see the effect. The negative control shows it does not see one that is absent. Stating the expectation first is what stops a surprising control from being reasoned into a pass.

**Example:** A PCR test for mating type runs with a strain known to carry both types as the positive control and a no-template blank as the negative. A band appears in the blank. The run is void, whatever the samples show.

**When unclear:** If no known positive exists, say so. The result is labelled "no positive control available".

### Checks Decay

E-GD source: ENFORCEMENT.md line 172 at 7e227d0.

**Do:**
1. The Planner's protocol states how often each control, calibration and reference material is rerun: every run, every batch, or a stated interval.
2. The Analyst logs each control run: which control, the date read from a clock, the expected result, the observed result.
3. A result whose latest control or calibration is older than the stated interval is labelled "control out of date".
4. A control that gives the same result through a change that should have altered it is flagged to the Operator as possibly not sensitive. The flag is a report. The Analyst does not redesign the control.

**Why:** A control is shown to work when it is run, and nothing keeps it working. Instruments drift, reference cultures degenerate, reagents age. A control that has stopped working looks the same as one that is working.

**Example:** A balance is checked with a reference weight monthly. Yields weighed six weeks after the last check carry "control out of date".

**When unclear:** If the protocol states no interval, ask the Planner. Until answered, label results "no control schedule".

### Data-Driven Debugging

E-GD source: ENFORCEMENT.md line 188 at 7e227d0.

**Do:**
1. Each explanation offered for an anomaly is recorded with the test that was run on it and the outcome.
2. After two explanations for the same anomaly have each been tested and failed, no third is proposed. The next actions are limited to collecting raw data on the anomaly, a controlled comparison that changes one factor, a minimal reproduction, or a direct measurement of the suspected cause.

**Why:** Two failed explanations in a row is evidence that the picture of the problem is wrong. A third explanation built on the same picture is a slower way to the same place.

**Example:** Cultures stop fruiting. Too warm: cooled, no change. Too dark: lit, no change. The guessing stops. The next step is a grid of culture age against transfer count, and a mating-type test on the failed cultures.

**When unclear:** An anomaly is the same one if it is the same observation under the same conditions. If in doubt, count it as the same.

### Validate Real Event Paths

E-GD source: ENFORCEMENT.md line 191 at 7e227d0.

**Do:**
1. The Planner's protocol says what material and conditions each method was validated on.
2. The Analyst reports every difference between that and the samples actually run: matrix, range, handling, age.
3. A method validated only on reference or ideal material is labelled as such wherever its results appear, until it has been tested on material like the real samples.

**Why:** A method that works on clean reference material has been tested on clean reference material. Real samples are older, mixed, degraded or contaminated, and that is where methods fail.

**Example:** A primer set was tested on pure cultures. It is then used on dried field-collected fruiting bodies. Its results carry "validated on pure culture only".

**When unclear:** Report the difference and let the Operator decide whether it matters.

### Assert Structural and Semantic Truths

E-GD source: ENFORCEMENT.md line 194 at 7e227d0.

**Do:**
1. The Planner's protocol states, for each measure, what it is meant to stand for and why it does.
2. The Analyst reports a measure under its own name: "fruiting body count", not "yield", unless the protocol defines yield as count.
3. Evidence that a step ran is not reported as a finding. "The assay completed", "a file was produced" and "the sequence matched something" are not results.
4. An identification by sequence names the reference it was matched against, and says whether that reference comes from type material.

**Why:** A measure is only as good as its link to the thing it is named for. A count can be exact and still say nothing about yield if size varies. A sequence match identifies the reference, and the reference may be mislabelled.

**Example:** A 99% match to a database record labelled with a species name is reported as "99% match to accession N, labelled X, not from type material". It is not reported as "identified as X".

**When unclear:** Report the raw measure under its own name, and ask what it may be taken to mean.

### Intent-Driven Engineering

E-GD source: ENFORCEMENT.md line 209 at 7e227d0.

**Do:**
1. Before any data is collected or opened for a result, a pre-registration entry in `RECORD.md` states: the hypothesis, a prediction concrete enough to be wrong, the sample size and how it was chosen, the exclusions, the tests and thresholds, the controls, the finish line and the abort conditions. If any is missing, no data is touched.
2. The entry is committed and pushed before the data is read.
3. One entry per study or analysis, not per step. Work outside its stated scope needs a new entry.
4. Afterwards, the result is compared with the prediction. A wrong prediction is recorded as wrong, with what was observed. It is never rewritten.
5. An analysis not in the pre-registration is allowed only when labelled exploratory and reported apart.

**Why:** Thresholds, exclusions and tests chosen after the data is seen can produce almost any result. A prediction that could not have been wrong confirms nothing. Writing both down first, where they cannot be changed, is what makes the result mean something.

**Example:** "Prediction: cultures five or more transfers from the master fruit in fewer than half of jars; cultures two or fewer transfers from the master fruit in more than half. Six jars per cell. Contaminated jars are excluded, counted and reported."

**When unclear:** If data was seen before the entry was written, say so in the entry. The result is labelled "not pre-registered".

### Complete Task Prompts

E-GD source: ENFORCEMENT.md line 215 at 7e227d0.

**Do:**
1. Every protocol or dispatch given to an Analyst contains: the role; the data and files in scope; the closed decisions that bear on the task, by record ID; the prediction and finish line; the tests and controls; what is out of scope; and any other work in flight it could collide with.
2. It is committed to the repository as a file under `prompts/preserved/`. It is not sent as chat text.
3. The Planner checks every factual claim in it at its source while writing, and cites the commit or date. A claim that could not be checked is listed as a premise for the Analyst to check first.
4. Each instruction states its reason, so that a less capable model can follow it.
5. The Analyst checks the protocol for each element before starting and returns missing ones by name. It does not fill them in.
6. The Analyst's check is structural only. The Operator confirms the decisions a protocol carries before it is run.

**Why:** An Analyst cannot know a decision it was never told. If the protocol leaves one out, the Analyst makes it without knowing it is making one, and the result looks the same as if the decision had been the Operator's. Only the Operator knows what the Operator decided.

**Example:** The dispatch that created this file, `prompts/preserved/2026-11-14-07.md`: it states its base commit, quotes the Operator's go, lists what not to touch, and gives the predictions before the work.

**When unclear:** Stop and ask. A missing element is returned, never guessed.
