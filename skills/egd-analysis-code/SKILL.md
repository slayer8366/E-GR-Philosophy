---
name: egd-analysis-code
description: Sends analysis code written for an E-GR study to E-GD's rules. Use whenever a Planner or Analyst writes or changes code that produces a research result: statistics scripts, data cleaning, figure generation, pipelines.
---

# Analysis code under E-GD

E-GR governs research. Analysis code is software, and E-GD governs it (RECORD.md 2026-11-14-01, decision 1). This skill is the bridge between them.

## When it applies

Any code whose output enters a result: a script that cleans data, fits a model, runs an ANOVA, builds a table or draws a figure that will be reported. A one-off script whose output nobody will rely on is exempt, as E-GD's OVERVIEW.md says under "When not to use this".

## What to do

1. Load E-GD's BOOTSTRAP.md (slayer8366/E-GD-Philosophy) and follow it for the code.
2. Load the E-GD ENFORCEMENT.md entries for the eight Code-only headwords as the code touches them:
   - Atomic State Mutations
   - Isolated Hardware and Integration Layers
   - Decouple Business Logic from Presentation
   - Observable Configuration References
   - Automated Boundary Enforcement
   - Unattended Execution Discipline
   - Uniform Code Paths
   - Additive Enhancements
3. Keep E-GR's rules for the study itself. The pre-registration, the controls, the conditions and the report stay under E-GR. The code's own intent record, if E-GD requires one, cites the E-GR study entry it serves.

## Where the two meet

- **Roles.** E-GD's Coder and E-GR's Analyst are the same kind of role. When the Analyst writes code, E-GD's Coder rules apply to that code. Neither makes a design decision.
- **Records.** The code's record lives with the code, under E-GD. The result's record lives with the study, under E-GR. Each cites the other by ID and commit.
- **Conflicts.** Where an E-GD rule and an E-GR rule disagree on the same step, stop and ask the Operator. Do not pick.

## Standing

This bridge is untested. Its first uses will show whether one skill is enough, or whether the meeting points above need rules of their own.
