# Code style

This file records Python-specific code conventions that affect API contracts, type-checkability, numerical behavior, and maintainability.

## Boundary

Use this file for stable Python code decisions, not for formatting rules or temporary implementation plans.

Appropriate entries include typing policy, tensor conventions, mutability policy, public API shape, error handling, module boundaries, docstring conventions, and numerical precision assumptions.

Do not duplicate rules already stated in [`../AGENTS.md`](../AGENTS.md). Do not use this file as a checklist for individual tasks.

## Current policy

Keep this file sparse until repeated implementation decisions expose a real convention.

Public APIs should be annotated when the annotation clarifies the contract. Internal annotations should be added when they improve readability, static checking, or testability; they should not be added merely to imitate static languages.

Python type annotations are semantic documentation and tool-facing contracts. They are not performance specialization hints in ordinary Python execution.

Avoid premature abstraction around tensors, devices, dtypes, and array shapes. When such conventions become stable, record them here before relying on them across modules.
