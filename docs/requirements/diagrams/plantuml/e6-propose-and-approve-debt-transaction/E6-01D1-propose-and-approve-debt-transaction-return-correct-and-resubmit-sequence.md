---
id: E6-01D1
project: farm-credit-ba-exercise
type: diagram-guide
status: approved
epic: E6
feature: E6-01
diagram: E6-01D1-propose-and-approve-debt-transaction-return-correct-and-resubmit-sequence.puml
layer: "L8 Sequence"

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

description: What happens when an approver returns a proposal and the officer corrects and resubmits it?
created: 2026-07-21
updated: 2026-07-22
---

# E6-01D1-propose-and-approve-debt-transaction-return-correct-and-resubmit-sequence

## Business Question

What happens when an approver returns a proposal and the officer corrects and resubmits it?

## Purpose

Explain the exception path and the version/audit history that must be retained.

## How to Explain It

This sequence focuses on the non-happy path. The approver returns the submitted proposal with a specific reason, the platform records the decision and changes the status, and the officer opens the returned transaction. Corrections are saved as a new version, revalidated, and resubmitted. The approver can compare the revised version with the prior submission before approving it. The main BA point is that correction must not overwrite history.

## Key Talking Points

- A return reason is mandatory and actionable.
- The revised transaction becomes a new version.
- Revalidation is required before resubmission.
- The approver can compare current and previous versions.
- The audit trail retains the original submission, return reason, changes, resubmission, and final decision.

## What This Diagram Does Not Show

Every possible rejection reason or product-specific validation rule.

## Position in the Visual Decomposition

`L8 Sequence`

## Related Artifacts

- [[EPIC-E6-issue-and-settle-security]]
- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]
- [[E6-01D1-propose-and-approve-debt-transaction-return-correct-and-resubmit-sequence]]
