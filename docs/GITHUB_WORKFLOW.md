# GitHub Workflow for the Public Case Study

The public GitHub repository is intended to demonstrate disciplined engineering communication without pretending to be NOMI's private source repository.

## Issues

Use issues for public, non-sensitive work such as:

- documentation defects
- evidence/caveat corrections
- architecture explanation improvements
- recruiter walkthrough improvements

Security-sensitive disclosures should follow `SECURITY.md`, not public issues.

## Pull requests

Pull requests are the governance surface for public claims. The PR template asks whether a change alters evidence, whether prototype boundaries remain visible, and whether any sensitive material was introduced.

## GitHub Actions

`.github/workflows/validate.yml` runs two public checks:

1. `python scripts/validate_portfolio.py`
2. `pytest -q`

These checks validate the **portfolio package and its evidence guardrails**. They do not run NOMI's private test suite and must never be described as doing so.

## Releases

If releases are used, tag them as public case-study snapshots, for example:

- `portfolio-v1.0`
- `portfolio-v1.1`

Do not create a public release named after a private passing-test checkpoint in a way that implies the public repository produced that test run.

## Projects

A GitHub Project can later track public portfolio work such as:

- evidence review
- screenshot sanitization
- architecture diagrams
- recruiter walkthrough improvements
- Vercel portfolio integration

It should not expose private NOMI backlog items or security-sensitive work.
