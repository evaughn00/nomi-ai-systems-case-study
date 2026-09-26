# Selected Architecture Decisions

## ADR-001 — Local-first is the default

**Decision:** Prefer local processing/storage and loopback-bound services where practical.

**Reasoning:** Privacy, inspectability, and independence from external availability are first-class constraints.

**Trade-off:** Local-first can increase hardware, packaging, and maintenance complexity.

---

## ADR-002 — Model output cannot directly promote durable system change

**Decision:** Treat model-generated changes as candidates requiring evidence and explicit promotion.

**Reasoning:** A model can be useful without being authoritative.

**Trade-off:** Slower iteration in exchange for traceability and rollback.

---

## ADR-003 — Reported security state and enforced security state are separate

**Decision:** Verification must test the enforcement boundary, not only configuration/status output.

**Reasoning:** The sandbox finding showed that a system can claim limits it does not actually enforce.

**Trade-off:** More test work, but stronger confidence in safety assertions.

---

## ADR-004 — Simulation must be visibly distinct from execution

**Decision:** UI and records should distinguish simulated behavior from live execution.

**Reasoning:** Operators should not have to infer whether an action actually happened.

**Trade-off:** More UI/status complexity.

---

## ADR-005 — Public portfolio evidence is sanitized, not open-source theater

**Decision:** Keep the private implementation private while publishing reviewable architecture, evidence, decisions, and bounded findings.

**Reasoning:** Recruiters need proof of judgment and depth; they do not need private credentials, sensitive topology, or the full system source.

**Trade-off:** Reviewers cannot inspect the complete implementation from the public repository.
