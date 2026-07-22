---
id: E6-01D2
project: farm-credit-ba-exercise
type: diagram-guide
status: approved
epic: E6
feature: E6-01
diagram: E6-01D2-propose-and-approve-debt-transaction-business-decision-flow.puml
layer: "L3 Business Decisions"

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

description: What decisions determine whether a proposal can proceed, must be corrected, or is approved?
created: 2026-07-21
updated: 2026-07-22
---

# E6-01D2-propose-and-approve-debt-transaction-business-decision-flow

## Business Question

What decisions determine whether a proposal can proceed, must be corrected, or is approved?

## Purpose

Reduce the workflow to its essential business decisions and feedback loops.

## How to Explain It

This diagram isolates the decision logic from the actors and systems. A draft must first be complete, then satisfy business rules, and only then can it be submitted. The approver either accepts it or returns it with a business reason. Any failed decision routes the proposal back for correction and revalidation. I use this view to identify decision points that should become business rules and acceptance criteria.

## Key Talking Points

- Completeness and rule compliance are separate decisions.
- Approval occurs only after successful validation.
- A return includes a business reason.
- All correction paths return to validation.
- Approval releases the transaction for security preparation.

## What This Diagram Does Not Show

Actor responsibilities, data fields, versioning mechanics, or detailed platform messages.

## Position in the Visual Decomposition

`L3 Business Decisions`

## Related Artifacts

- [[EPIC-E6-issue-and-settle-security]]
- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]
- [[E6-01D2-propose-and-approve-debt-transaction-business-decision-flow]]
