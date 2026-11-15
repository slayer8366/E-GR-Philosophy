#!/usr/bin/env python3
"""Check E-GR's transfer map against E-GD's headwords.

Every bold headword in E-GD's PHILOSOPHY.md must appear exactly once as a
row in E-GR's GLOSSARY.md, with a valid bucket, and exactly once as a bold
headword in E-GR's PHILOSOPHY.md. Rows bucketed New must not be E-GD
headwords, and must also appear once in E-GR's PHILOSOPHY.md. Every bold
headword in E-GR's PHILOSOPHY.md must have a row in E-GR's GLOSSARY.md.

E-GR's ENFORCEMENT.md must exist (R1). An entry is a line `### <Headword>`;
its body runs to the next line starting `### ` or `## `, or the end of the
file. Every GLOSSARY headword whose bucket is in ENFORCED_BUCKETS has exactly
one entry (R2). Every entry's headword is a GLOSSARY headword bucketed
Carried or Translated (R3). Every entry's body has each of the labels
`**Do:**`, `**Why:**`, `**Example:**` and `**When unclear:**` exactly once,
at the start of a line (R4).

Usage: python3 check_transfer.py PATH_TO_EGD_PHILOSOPHY_MD
Exit 0 on pass, 1 on any failure, each failure printed on its own line.
"""
import re
import sys
from pathlib import Path

BUCKETS = {"Carried", "Translated", "Code-only", "New"}
ENFORCED_BUCKETS = {"Translated"}
LABELS = ("**Do:**", "**Why:**", "**Example:**", "**When unclear:**")
HEAD_RE = re.compile(r"^\*\*([^*]+?):\*\*")
HERE = Path(__file__).resolve().parent


def headwords(path):
    return [m.group(1).strip() for line in path.read_text().splitlines()
            if (m := HEAD_RE.match(line))]


def glossary_rows(path):
    rows = []
    for n, line in enumerate(path.read_text().splitlines(), 1):
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if cells[0] == "Headword":
            continue
        rows.append((n, cells))
    return rows


def enforcement_entries(path):
    entries = []
    for line in path.read_text().splitlines():
        if line.startswith("### "):
            entries.append((line[4:].strip(), []))
        elif line.startswith("## "):
            entries.append((None, []))
        elif entries:
            entries[-1][1].append(line)
    return [(h, body) for h, body in entries if h is not None]


def main(egd_philosophy):
    failures = []
    egd = headwords(Path(egd_philosophy))
    if len(egd) != 45:
        failures.append(f"E-GD PHILOSOPHY.md: expected 45 headwords, read {len(egd)}")

    gloss_path = HERE / "GLOSSARY.md"
    phil_path = HERE / "PHILOSOPHY.md"
    for p in (gloss_path, phil_path):
        if not p.exists():
            failures.append(f"missing file: {p.name}")
    if failures and not (gloss_path.exists() and phil_path.exists()):
        return failures

    rows = glossary_rows(gloss_path)
    by_head = {}
    for n, cells in rows:
        if len(cells) < 3:
            failures.append(f"GLOSSARY.md line {n}: fewer than 3 cells")
            continue
        by_head.setdefault(cells[0], []).append((n, cells))
        if cells[2] not in BUCKETS:
            failures.append(f"GLOSSARY.md line {n}: bad bucket '{cells[2]}' for '{cells[0]}'")

    egr_heads = headwords(phil_path)
    for h in egd:
        g = by_head.get(h, [])
        if len(g) != 1:
            failures.append(f"GLOSSARY.md: '{h}' appears {len(g)} times, expected 1")
        elif g[0][1][2] == "New":
            failures.append(f"GLOSSARY.md line {g[0][0]}: E-GD headword '{h}' bucketed New")
        c = egr_heads.count(h)
        if c != 1:
            failures.append(f"PHILOSOPHY.md: '{h}' appears {c} times, expected 1")

    for h, g in by_head.items():
        if h in egd:
            continue
        if any(cells[2] != "New" for _, cells in g):
            failures.append(f"GLOSSARY.md: '{h}' is not an E-GD headword and not bucketed New")
        if egr_heads.count(h) != 1:
            failures.append(f"PHILOSOPHY.md: New headword '{h}' appears {egr_heads.count(h)} times, expected 1")

    for h in egr_heads:
        if h not in by_head:
            failures.append(f"PHILOSOPHY.md: '{h}' has no GLOSSARY.md row")

    enf_path = HERE / "ENFORCEMENT.md"
    if not enf_path.exists():
        failures.append(f"missing file: {enf_path.name}")
    else:
        entries = enforcement_entries(enf_path)
        entry_heads = [h for h, _ in entries]
        for h, g in by_head.items():
            if any(len(c) > 2 and c[2] in ENFORCED_BUCKETS for _, c in g):
                n = entry_heads.count(h)
                if n != 1:
                    failures.append(f"ENFORCEMENT.md: '{h}' appears {n} times, expected 1")
        for h, body in entries:
            g = by_head.get(h, [])
            if not any(len(c) > 2 and c[2] in ("Carried", "Translated") for _, c in g):
                failures.append(f"ENFORCEMENT.md: '{h}' is not a Carried or Translated headword")
            for label in LABELS:
                n = sum(1 for line in body if line.startswith(label))
                if n != 1:
                    failures.append(f"ENFORCEMENT.md: '{h}' has {n} '{label}' lines, expected 1")

    counts = {b: sum(1 for g in by_head.values() for _, c in g if len(c) > 2 and c[2] == b)
              for b in sorted(BUCKETS)}
    print("counts: " + ", ".join(f"{b} {n}" for b, n in counts.items()))
    return failures


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    fails = main(sys.argv[1])
    for f in fails:
        print("FAIL: " + f)
    print("PASS" if not fails else f"{len(fails)} failure(s)")
    sys.exit(1 if fails else 0)
