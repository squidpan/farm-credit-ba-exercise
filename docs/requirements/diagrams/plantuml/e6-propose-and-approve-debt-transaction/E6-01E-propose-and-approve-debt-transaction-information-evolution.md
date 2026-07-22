---
id: E6-01E
project: farm-credit-ba-exercise
type: diagram-guide
status: approved
epic: E6
feature: E6-01
diagram: E6-01E-propose-and-approve-debt-transaction-information-evolution.puml
layer: "L4 Information Evolution"

categories:
  - "[[Diagrams]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"

tags:
  - farm-credit
  - debt-issuance
  - business-analysis
  - plantuml
  - interview-study

description: How does the transaction record change as it moves from draft to approved?
created: 2026-07-21
updated: 2026-07-22
---

# E6-01E-propose-and-approve-debt-transaction-information-evolution

## Business Question

How does the transaction record change as it moves from draft to approved?

## Purpose

Show how information, version control, decision evidence, and editability evolve through the lifecycle.

## How to Explain It

This diagram treats the transaction as an evolving business record. The initial draft contains proposed terms, validation confirms completeness and rules, submission creates a locked review version, and a return records the reason for change. Corrections produce a new version rather than silently modifying the submitted one. Once approved, the authorized terms, approver identity, timestamp, and audit history become the official record.

## Key Talking Points

- Each lifecycle stage adds business meaning to the record.
- Submission preserves a controlled snapshot.
- Returned and revised versions remain traceable.
- The approved version becomes the official business record.
- Approval evidence travels with the transaction.

## What This Diagram Does Not Show

Detailed screen behavior, database schema, or all business rules.

## Position in the Visual Decomposition

`L4 Information Evolution`

## Related Artifacts

- [[EPIC-E6-issue-and-settle-security]]
- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]
- [[E6-01E-propose-and-approve-debt-transaction-information-evolution]]
