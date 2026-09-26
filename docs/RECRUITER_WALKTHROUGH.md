# Recruiter Walkthrough

A five-minute review path for NOMI.

## Minute 0–1 — What is it?

Read the first two sections of [../README.md](../README.md).

Key takeaway:

> NOMI is a local-first cognitive AI systems project where AI-assisted development is treated as a governed engineering process rather than trusted by default.

## Minute 1–2 — Is there measurable evidence?

Open [../VALIDATION.md](../VALIDATION.md).

Look for:

- 276-test historical green checkpoint
- 47 Python test modules
- 302 identified test functions with explicit non-execution caveat
- 13-route / 280-control prototype validation
- 96 modeled domains / 38 subsystem records

## Minute 2–3 — What is the architecture?

Open [../ARCHITECTURE.md](../ARCHITECTURE.md).

Key themes:

- local-first
- scoped access
- audit/provenance
- multiple model providers
- deterministic/offline path
- candidate-change governance
- human promotion authority

## Minute 3–4 — What went wrong?

Open [../SECURITY.md](../SECURITY.md).

The most important examples are not hypothetical:

- fail-open privacy behavior
- sandbox limits that were reported but not enforced

The engineering response was to treat displayed policy and real enforcement as separate claims.

## Minute 4–5 — Is the project honest about boundaries?

Open [IMPLEMENTATION_BOUNDARIES.md](IMPLEMENTATION_BOUNDARIES.md).

The project distinguishes:

- verified implementation
- implemented but not fully proven
- prototype/simulation
- planned/research

That distinction is part of the governance model itself.
