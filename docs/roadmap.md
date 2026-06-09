# Roadmap

This file defines the public staged scope of PyGS as a scientific software project.

## Contract

Record project-facing milestones and phase boundaries:

* current scope;
* completed setup phase;
* next scientific kernel;
* benchmark phases;
* deferred extensions;
* decision gates for expanding scope.

## Current scope

PyGS first targets bosonic Gaussian states in PyTorch: geometry-aware setup, differentiable energies, and reproducible optimization examples.

## Phases

Fill with the present package boundary: bosonic Gaussian states first.

- [x] Phase 0: project scaffold
    - package metadata
    - CI
    - formatting and linting
    - minimal documentation structure
    - AI-assisted development harness
- [ ] Phase 1: bosonic Gaussian core
    - quadrature/ladder operator
    - covariance parametrization
- [ ] Phase 2: quadratic Hamiltonian benchmark
    - analytically solvable ground-state tests
    - autodiff gradient checks
- [ ] Phase 3: model-oriented examples
    - stable examples suitable for documentation

## Deferred directions

fermions, multi-GPU benchmarks, and publication-oriented examples are deferred.

## Decision gates

Expand scope only after the current phase has tests, documentation, and a stable public boundary.

## Risks

- convention mismatch between parametrization and symplectic forms;
- unstable constrained parametrization;
- premature abstraction;
