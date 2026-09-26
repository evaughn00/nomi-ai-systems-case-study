# Security Engineering — Sanitized Findings

This document summarizes engineering lessons from NOMI without publishing exploit instructions, credentials, private topology, or sensitive defensive configuration.

## Finding 1 — fail-open privacy behavior

### What went wrong

Adversarial review identified a DNS/WebRTC privacy failure mode where the intended privacy layer could degrade in a fail-open direction.

### Why it mattered

A privacy control that reports a protected state while allowing an unintended network path creates a mismatch between **displayed policy** and **actual enforcement**.

### Engineering response

- classify the issue as an enforcement failure, not a cosmetic bug
- correct the behavior
- re-run verification
- preserve the failure mode as regression knowledge
- prefer fail-closed behavior when a privacy prerequisite is unavailable

### General lesson

Security state should be derived from enforceable conditions, not optimistic configuration.

---

## Finding 2 — sandbox policy vs. real enforcement

### What went wrong

A sandbox reported resource limits that were not actually enforced.

### Why it mattered

A system can appear constrained while still behaving unconstrained. Reporting policy is not equivalent to implementing policy.

### Engineering response

- separate declared limits from measured/enforced limits
- treat failed enforcement as a blocking defect
- correct the enforcement path
- re-test before promotion

### General lesson

For safety boundaries:

> **claimed control ≠ enforced control**

Verification has to test the boundary itself.

## Public disclosure boundary

This case study intentionally omits:

- exploit steps
- exact private topology
- secrets and credentials
- recovery details
- machine-specific configuration
- defensive values that would unnecessarily weaken the private system

The purpose is to demonstrate security engineering judgment, not publish an attack guide.
