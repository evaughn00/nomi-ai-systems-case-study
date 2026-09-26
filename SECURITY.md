# Security Policy

## Scope

This repository is a **sanitized portfolio and case-study repository**. It does not contain NOMI's private source tree, production credentials, private infrastructure, personal data, or detailed exploit material.

Security issues in this public repository can still matter—for example, accidental disclosure of a secret, private path, sensitive screenshot, or unsafe publication of internal details.

## Reporting a security issue

Please do **not** publish sensitive findings as a public issue.

Preferred reporting path:

1. Use GitHub's private security-reporting / Security Advisory mechanism for this repository when available.
2. If that is unavailable, contact **erikavaughn@pm.me** with the subject `NOMI portfolio security report`.

Include only the minimum information needed to reproduce or identify the disclosure risk.

## What not to send publicly

Do not post:

- API keys, tokens, passwords, or credentials
- private repository contents
- real internal IP/DNS/network configuration
- personal memory/profile data
- recovery-key or authentication material
- exploit steps against the private NOMI system

## Public security engineering notes

Sanitized lessons from security findings in NOMI are documented separately in [docs/SECURITY_FINDINGS.md](docs/SECURITY_FINDINGS.md). Those notes intentionally describe engineering impact without exposing operational attack instructions.
