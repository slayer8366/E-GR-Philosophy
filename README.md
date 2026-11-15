# Evidence Gated Research

A working method for AI-assisted research where results have to be correct and traceable.

E-GR is a fork of [Evidence Gated Development](https://github.com/slayer8366/E-GD-Philosophy) (E-GD), rewritten for scientific research. E-GD was built for software and says of itself that most of it is "the working practice of science, carried over to a setting where the instrument is a fast, confident agent" (E-GD OVERVIEW.md at 7e227d0). E-GR carries it back.

## Relationship to E-GD

- **Fork.** E-GR's PHILOSOPHY.md takes each of E-GD's 45 principles and marks it Carried (holds as written), Translated (same reason, research mechanism), or Code-only.
- **Import.** Code-only principles are not part of E-GR. Analysis code is written under E-GD, through the egd-analysis-code skill.
- **Research layer.** Principles E-GD does not have, from research practice. They are on probation.

The transfer, as first drawn: 21 Carried, 16 Translated, 8 Code-only, 6 New. `check_transfer.py` verifies the map against E-GD.

## Roles

- **Operator.** You. Approves, closes decisions, and observes what no agent was told to run: the bench, the grow room, the field.
- **Planner.** Designs the study and writes the protocols. Never runs an analysis.
- **Analyst.** Runs tests and analyses, writes tables and reports. Never changes the design.

## What's here

| File | For | What it is |
|---|---|---|
| `BOOTSTRAP.md` | Agents | The one page loaded every session. |
| `PHILOSOPHY.md` | Agents | The 45 transferred principles and the research layer. |
| `GLOSSARY.md` | Machines | Headword index against E-GD, checked by script. |
| `check_transfer.py` | Machines | Verifies GLOSSARY and PHILOSOPHY against E-GD's headwords. |
| `RECORD.md` | Both | The append-only record. |
| `skills/research-evidence-discipline/` | Agents | Evidence rules for research claims. |
| `skills/egd-analysis-code/` | Agents | The bridge that sends analysis code to E-GD. |

Running the check: `python3 check_transfer.py PATH/TO/E-GD-Philosophy/PHILOSOPHY.md`

## Not yet here

ENFORCEMENT.md, PROTOCOL.md, onboarding, role profiles, a CLAUDE.md, and a license. Each comes under its own record entry.

## What this does not claim

E-GD's evidence comes from software projects. Whether its gates hold up in research is untested; E-GR's record is where that will show. The research layer rests on a single working session. Treat all of it as a hypothesis with a paper trail.
