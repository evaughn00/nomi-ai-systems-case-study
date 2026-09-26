#!/usr/bin/env python3
"""Validate public portfolio evidence, privacy boundaries, and anti-overclaim guardrails."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
METRICS = ROOT / "evidence" / "public_metrics.json"

REQUIRED_DOCS = [
    "README.md",
    "ARCHITECTURE.md",
    "CASE_STUDY.md",
    "CONTRIBUTING.md",
    "DESIGN.md",
    "SECURITY.md",
    "VALIDATION.md",
    "NOTICE.md",
    "docs/IMPLEMENTATION_BOUNDARIES.md",
    "docs/RECRUITER_WALKTHROUGH.md",
    "docs/DECISIONS.md",
    "docs/PUBLICATION_NOTE.md",
    "docs/GITHUB_WORKFLOW.md",
    "docs/GITHUB_PROFILE_README.md",
    "docs/SECURITY_FINDINGS.md",
    ".github/pull_request_template.md",
]

FORBIDDEN_PUBLIC_PHRASES = [
    "302 tests passed",
    "302 passing tests",
    "276 of 302 tests passing",
    "91% pass rate",
    "production-ready NOMI",
    "fully production ready",
]

PRIVATE_PATTERNS = [
    (re.compile(r"/home/[A-Za-z0-9_.-]+/"), "private Unix home path"),
    (re.compile(r"[A-Za-z]:\\\\Users\\\\[^\\\\\s]+", re.I), "private Windows user path"),
    (re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"), "GitHub token-like value"),
    (re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"), "API-key-like value"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "AWS access-key-like value"),
]

TEXT_SUFFIXES = {".md", ".json", ".py", ".yml", ".yaml", ".txt", ".gitignore"}


def iter_text_files():
    for p in ROOT.rglob("*"):
        if not p.is_file() or ".git" in p.parts:
            continue
        if p.name == ".gitignore" or p.suffix.lower() in TEXT_SUFFIXES:
            yield p


def main() -> int:
    errors: list[str] = []

    for rel in REQUIRED_DOCS:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required document: {rel}")

    data = json.loads(METRICS.read_text(encoding="utf-8"))

    if data["current_locked_green_in_supplied_lineage_evidence"] != 276:
        errors.append("expected public green checkpoint to remain 276")

    inventory = data["later_repository_inventory"]
    if inventory["python_test_modules"] != 47:
        errors.append("test-module inventory drifted from 47")
    if inventory["statically_identified_test_functions"] != 302:
        errors.append("test-function inventory drifted from 302")
    if inventory["executed_during_reconciliation"] is not False:
        errors.append("302-test reconciliation must remain marked not executed")
    if inventory["passing_claim_allowed_from_this_reconciliation"] is not False:
        errors.append("302-test reconciliation must not become a passing-test claim")

    files = list(iter_text_files())
    public_docs = [p for p in files if p.suffix.lower() == ".md"]
    corpus = "\n".join(p.read_text(encoding="utf-8", errors="replace").lower() for p in public_docs)

    for phrase in FORBIDDEN_PUBLIC_PHRASES:
        if phrase.lower() in corpus:
            errors.append(f"forbidden overclaim found: {phrase!r}")

    for p in files:
        text = p.read_text(encoding="utf-8", errors="replace")
        for pattern, label in PRIVATE_PATTERNS:
            if pattern.search(text):
                errors.append(f"{label} detected in {p.relative_to(ROOT)}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    required_readme_phrases = [
        "276 passing tests",
        "47 python test modules / 302 identified test functions",
        "not executed during that reconciliation",
        "sanitized public case study",
        "ci badge validates this public evidence package",
        "git history begins when the case study is published",
    ]
    for phrase in required_readme_phrases:
        if phrase not in readme:
            errors.append(f"README is missing evidence/caveat phrase: {phrase!r}")

    if errors:
        print("Portfolio validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Portfolio validation passed.")
    print(f"- required docs: {len(REQUIRED_DOCS)} present")
    print("- evidence guardrail: 276 passing checkpoint preserved")
    print("- evidence guardrail: 302-function inventory remains a non-passing claim")
    print("- public-history disclosure: present")
    print("- overclaim phrase scan: clean")
    print("- private-path / token-like scan: clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
