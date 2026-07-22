---
id: E6-01C
project: farm-credit-ba-exercise
type: diagram-guide
status: approved
epic: E6
feature: E6-01
diagram: E6-01C-propose-and-approve-debt-transaction-successful-approval-sequence.puml
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

description: How do the people and platform components interact during a successful approval?
created: 2026-07-21
updated: 2026-07-22
---

# E6-01C-propose-and-approve-debt-transaction-successful-approval-sequence

## Business Question

How do the people and platform components interact during a successful approval?

## Purpose

Show the ordered interactions for the happy path from draft creation through final approval.

## How to Explain It

This is the happy-path interaction sequence. The officer enters and saves the proposal, requests validation, and submits it. The platform validates against rules and reference data, locks the submitted version, creates the approval request, and notifies the approver. The approver reviews the approval package and approves it, after which the platform records the approval and notifies the officer. It demonstrates both orchestration and the evidence retained at each step.

## Key Talking Points

- Validation is completed before submission.
- The submitted version is locked and recorded.
- The approver receives terms, validation results, and history.
- Approval is persisted before the outcome is communicated.
- The proposer and approver are distinct authorized users.

## What This Diagram Does Not Show

Return and correction behavior, alternate decisions, or all technical integration details.

## Position in the Visual Decomposition

`L8 Sequence`

## Related Artifacts

- [[EPIC-E6-issue-and-settle-security]]
- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]
- [[E6-01C-propose-and-approve-debt-transaction-successful-approval-sequence]]
