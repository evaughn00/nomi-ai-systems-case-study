# Contributing to the NOMI Public Case Study

This repository is an evidence and architecture surface for a private engineering project. Contributions should improve **clarity, accuracy, reproducibility of public evidence, or documentation quality** without attempting to recreate or expose NOMI's private source.

## Contribution principles

1. **No claim without evidence.** Numeric or implementation claims must map to a documented source category.
2. **Inventory is not execution.** Static test counts may not be converted into pass-rate claims unless an execution record supports that claim.
3. **Private stays private.** Do not add private source code, credentials, machine paths, personal data, internal network configuration, or exploit details.
4. **Prototype boundaries remain visible.** Browser simulations, mock paths, and design-only work must not be described as live production behavior.
5. **Human review is required.** Changes to evidence, security language, implementation status, or governance claims require explicit review before merge.

## Pull requests

Use the pull-request template. For changes that affect evidence claims, include:

- the claim being changed
- the evidence source/category
- the exact caveat or implementation boundary
- whether any public metric changes

All repository validation checks must pass before merge.

## Security-sensitive changes

Do not open a public issue for a sensitive disclosure. Follow [SECURITY.md](SECURITY.md).
