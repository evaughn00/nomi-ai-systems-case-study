## Summary

Describe the documentation, evidence, or architecture change.

## Evidence impact

- [ ] No public evidence claim changed
- [ ] A public evidence claim changed and its source/category is documented
- [ ] Static inventory has **not** been converted into an execution/pass claim
- [ ] Prototype/simulation boundaries remain explicit

## Privacy / security check

- [ ] No credentials, tokens, secrets, personal data, private paths, internal topology, or exploit-sensitive details were added
- [ ] Any security-sensitive material was handled according to `SECURITY.md`

## Verification

- [ ] `python scripts/validate_portfolio.py`
- [ ] `pytest -q`
