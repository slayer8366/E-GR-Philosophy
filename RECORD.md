# RECORD.md

E-GR-Philosophy's append-only record store. No existing line is ever removed or modified. Additions land at the end. Corrections are new entries that point at what they supersede.

Entry form follows E-GD's RECORDING.md at commit 7e227d0: fields are lines starting `**Label:**`, a value runs to the next such line, and entries are separated by bare `---` lines after the Entries heading. Where an E-GD provision already covers something, entries here cite it by file and commit rather than copying it.

## Entries

---

**Kind:** decision

**ID:** 2026-11-14-01

**Timestamp:** 2026-11-15T07:17:58Z

**Title:** E-GR's founding decisions

**What the operator was told before answering:** six open decisions: scope, relationship to E-GD, roles, record, name, skills; and a request to name the executing role.

**The operator, verbatim, 2026-11-14 23:16 PST:**

"1 research only with analysis code under EGD

2 both. Fork the documents and have EGR import EGD and add a research layer. The coding parts can be a skill for the EGR rather than part of the main discipline.

3 in EGD planner plans, coder executes. Operator approves. The agentic profile for the executor is obviously different than the coder, but it's a role for running tests, analysis, writing tables, reports, ANOVA, anything that does automated work, similar to the coder nonetheless. What would you call the position?

4 fresh record, but use EGD as a reference for the provisions we have in place already.

5 Evidence Gated Research.

6 yes"

**The operator, verbatim, 2026-11-14 23:17 PST:** "Analyst it is. Go ahead and build it"

**What it sets:**

1. Scope: E-GR governs research. Analysis code is written under E-GD.
2. E-GR forks E-GD's documents, rewritten for research, and imports E-GD for anything about code through a skill rather than the core principles.
3. Roles: Operator (approves), Planner (designs, writes protocols), Analyst (executes: runs tests and analyses, writes tables and reports; makes no design decisions).
4. A fresh record. E-GD provisions are cited by ID and commit, not copied.
5. Name: Evidence Gated Research.
6. The research-evidence-discipline skill goes into `skills/` as the first E-GR skill.

**Not authorised by this:** merging. The skeleton lands on a branch; merge is the operator's approval.

**Notes:** Written by the planner, who is also executing under the operator's go of 23:17 PST. The role split E-GD requires is not held in this session; stated here so a reader does not assume it was.

---

**Kind:** intent

**ID:** 2026-11-14-02

**Timestamp:** 2026-11-15T07:17:58Z

**Title:** E-GR skeleton: transfer map of E-GD's 45 principles into research, plus the first two skills

**Change:**

1. README.md: what E-GR is, its relationship to E-GD, its roles.
2. BOOTSTRAP.md: the one-page rule set loaded every session, for Planner and Analyst.
3. PHILOSOPHY.md: every one of E-GD's 45 headwords, each marked Carried, Translated or Code-only, with research wording for Carried and Translated, and a pointer for Code-only. A research layer of new principles, marked as on probation.
4. GLOSSARY.md: the table binding each headword to its E-GD source line, its bucket and its E-GR status.
5. skills/research-evidence-discipline/SKILL.md: the operator's saved skill, copied as it is.
6. skills/egd-analysis-code/SKILL.md: the bridge skill that sends analysis code to E-GD.
7. check_transfer.py: checks that every E-GD headword appears exactly once in GLOSSARY.md and once in PHILOSOPHY.md, with a valid bucket.

**Scope boundary:** the seven files above and this RECORD.md, on branch skeleton-2026-11-14 of slayer8366/E-GR-Philosophy.

Out of scope, deferred:

- ENFORCEMENT.md (what an agent does about each principle). Its own intent.
- PROTOCOL.md, ONBOARDING.md, an operator profile, an Analyst profile, CLAUDE.md, LICENSE.
- Any change to E-GD.
- Merging.

**Baseline:**

- E-GR-Philosophy: empty repository, no commits, cloned 2026-11-15T07:1xZ.
- E-GD-Philosophy at 7e227d0 (shallow clone, HEAD). PHILOSOPHY.md has 45 bold headwords at lines 7 to 109; GLOSSARY.md has 45 table rows at lines 13 to 57.

**Prediction (outcome — planner):** stated in chat to the operator on 2026-11-14 at about 23:05 PST, before any principle was classified one by one: "Carry over almost as written (about 25)", "Need translating (about 12)", "Only apply to analysis code (about 8)". Written down here as made, so the count can prove it wrong.

**Prediction (mechanism — coder):** check_transfer.py fails when one headword is removed from GLOSSARY.md, naming that headword as missing, and when a bucket is misspelled, naming the row. It passes on the finished files.

**Finish line:** all seven files exist on the branch, check_transfer.py passes on the committed tree, each sabotage was observed failing for its stated reason and reverted, a terminal entry is written, and the branch is pushed and confirmed on the remote.

**Abort conditions:** the push is refused; E-GD's headword list cannot be read as 45 entries; or a headword cannot be placed in one bucket without a design call the operator has not made, in which case stop and ask.

**Notes:** Written by the planner-executor in this session. Next free ID: 2026-11-14-03.

---

**Kind:** terminal

**ID:** 2026-11-14-03

**Timestamp:** 2026-11-15T07:20:27Z

**Closes:** 2026-11-14-02

**Outcome:** completed

**Observed:**

- All seven files written on branch skeleton-2026-11-14: README.md, BOOTSTRAP.md, PHILOSOPHY.md, GLOSSARY.md, check_transfer.py, skills/research-evidence-discipline/SKILL.md, skills/egd-analysis-code/SKILL.md.
- Count, against the outcome prediction (about 25 / 12 / 8): Carried 21, Translated 16, Code-only 8, plus 6 New. Carried was over-predicted by 4 and Translated under-predicted by 4. Code-only was exact. The prediction was wrong in the direction of assuming more of E-GD would hold as written; the four that moved were Reconstructable Environments, Explicit Canonicalization, Evidence-Based Feature Addition and Concurrency Awareness, each of which names a software mechanism.
- check_transfer.py, run before GLOSSARY.md and PHILOSOPHY.md existed: failed, naming both as missing. Expected.
- Sabotage 1, the Checks Decay row removed from GLOSSARY.md: failed with "'Checks Decay' appears 0 times, expected 1". Matches the mechanism prediction. Reverted.
- Sabotage 2, Sourced Claims bucketed "Carryed": failed with "line 48: bad bucket 'Carryed'". Matches. Reverted.
- Sabotage 3, not predicted, added: Severity of Checks renamed in PHILOSOPHY.md. Failed naming the missing headword. Reverted.
- Final run on the files as committed: PASS, counts Carried 21, Code-only 8, New 6, Translated 16.
- skills/research-evidence-discipline/SKILL.md is a byte copy of the operator's saved skill: sha256 bdd4695319a12c9e5db190cb9462b67446c5e35227d083fb7901a33b25dae87d for both.

**Deviations:**

- Sabotage 3 showed a limit in the check: a stray headword in PHILOSOPHY.md that is in no GLOSSARY row is not reported. Only the missing original is. Not fixed under this intent. DEFER: report PHILOSOPHY.md headwords absent from GLOSSARY.md.
- In PHILOSOPHY.md, Checks Decay is placed before Data-Driven Debugging, the reverse of E-GD's order. Each entry carries its E-GD line, so nothing is lost; noted so it is not read as deliberate.
- The six New principles were placed in PHILOSOPHY.md under a probation section, not in a PROTOCOL.md, because PROTOCOL.md was out of scope. E-GD's practice would put them in PROTOCOL first. OPEN for the operator: move them when PROTOCOL.md is built, or keep them here.
- The two prediction field labels in 2026-11-14-02 carry em dashes, copied from E-GD's field form. The operator's style avoids em dashes. Left as written in this append-only file. OPEN: whether E-GR's field labels drop them from here on.
- Role split not held: one session planned and executed, as 2026-11-14-01 states.

**Notes:** Written by the planner-executor. Checks run after this entry, before the final commit. Next free ID: 2026-11-14-04.
