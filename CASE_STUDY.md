# NOMI Case Study

## Context

NOMI is an independent AI systems project created and led by Erika Vaughn beginning in 2026. NOMI is the persistent user-facing AI identity; NOEMA is the underlying architectural lineage and systems substrate.

The project combines AI-assisted software development, local-first architecture, privacy/security engineering, governance, validation, interface design, and hardware-oriented experimentation.

## Problem

Modern AI-assisted development makes it easy to generate capability faster than teams can validate it.

The project therefore focuses on a harder question:

**How do you let an AI system evolve without allowing proposed changes, model output, or optimistic status reporting to silently become trusted behavior?**

## My role

**Creator & Lead Architect**

Responsibilities include:

- system architecture
- backend/API design
- multi-model engineering workflow design
- AI evaluation and verification
- security/privacy architecture
- change-governance design
- interface architecture
- test/validation strategy
- hardware/sensor integration direction
- implementation review and final promotion authority

## Approach

### 1. Local-first architecture

Prefer local processing, local storage, and loopback-bound services where practical. External access is deliberate rather than assumed.

### 2. Multi-model engineering

Use multiple models as independent engineering perspectives rather than as a single source of truth.

ChatGPT, Claude, Gemini, and DeepSeek have been used across implementation support, critique, adversarial review, architecture analysis, and test reasoning.

### 3. Governed promotion

Model-generated or learned changes are treated as candidates.

The architecture uses concepts including:

- change classification
- provenance
- transition records
- adversarial verification
- test gates
- human approval
- shadow/staged validation
- rollback/recovery independence
- append-only auditability

### 4. Security verification

Adversarial review is expected to find mismatches between what a subsystem **claims** and what it actually **enforces**.

Two important examples were a fail-open privacy condition and unenforced sandbox resource constraints. Both changed how system-state claims were treated.

### 5. Visible governance

The GUI was designed to expose state rather than hide it: permissions, provenance, simulation status, safety restrictions, approval state, and recovery/system health.

## Measurable evidence

- historical green checkpoints reaching **276 passing tests**
- later repository reconciliation: **47 Python test modules / 302 identified test functions** (inventory, not an executed-pass claim)
- validated **13-route** browser prototype covering governance, memory, provenance, uncertainty, prediction, system health, and related operational views
- detailed prototype counts and QA evidence retained in `DESIGN.md` rather than used as headline hiring claims

## What I learned

### A control is only real if it is enforced

The sandbox finding reinforced that configuration and enforcement must be tested separately.

### Fail-closed behavior is a design choice

A privacy or authorization layer should not silently relax itself when a prerequisite disappears.

### AI evaluation is broader than answer quality

For an AI system that can influence its own development, evaluation also includes:

- provenance
- authorization
- change boundaries
- rollback
- security invariants
- execution truth

### Interface design can carry safety information

A system that clearly shows “simulation,” “blocked,” “candidate,” or “approved” gives the operator a better basis for judgment than one that collapses everything into a single conversational surface.

## Current boundary

NOMI remains active development. Some components have implementation/test evidence, some are prototypes or simulations, and some remain design or research work.

This case study deliberately documents those categories rather than presenting the entire roadmap as shipped functionality.
