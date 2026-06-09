# Development workflow

This file records durable workflow decisions. Executable rules for local coding agents remain in [AGENTS.md](../AGENTS.md).

## Decision

Separate reasoning, implementation, validation, and final review.

## Roles

- ChatGPT: theory checks, derivation review, API design, architecture review.
- Local coding agents: bounded implementation, tests, refactors, command execution.
- Maintainer: scientific correctness, dependency approval, public API decisions, final review.

## Change control

Workflow-level changes should update this file first, then update [AGENTS.md](../AGENTS.md) only when agent behavior must change.
