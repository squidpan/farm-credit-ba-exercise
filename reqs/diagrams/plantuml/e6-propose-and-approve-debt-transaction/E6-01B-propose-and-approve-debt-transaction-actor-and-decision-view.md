---
id: E6-01B
project: farm-credit-ba-exercise
type: diagram-guide
status: approved
epic: E6
feature: E6-01
diagram: E6-01B-propose-and-approve-debt-transaction-actor-and-decision-view.puml
layer: "L2 Responsibilities"

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

description: Who is responsible for proposing, validating, deciding, and recording the outcome?
created: 2026-07-21
updated: 2026-07-22
---

# E6-01B-propose-and-approve-debt-transaction-actor-and-decision-view

## Business Question

Who is responsible for proposing, validating, deciding, and recording the outcome?

## Purpose

Clarify responsibility boundaries among the Issuance Officer, Debt Issuance Platform, and Treasury Approver.

## How to Explain It

This is the responsibility view. The Issuance Officer owns proposing and submitting the transaction. The platform owns validation, workflow control, and recording the result. The Treasury Approver independently decides whether the transaction should proceed. I use this diagram to separate human accountability from platform behavior and to make clear that the platform supports the decision but does not make the business approval decision.

## Key Talking Points

- The officer proposes; the approver decides.
- The platform validates and controls workflow.
- The final decision and status are recorded centrally.
- Responsibility separation supports segregation of duties.

## What This Diagram Does Not Show

The full lifecycle, detailed exception loops, or internal service interactions.

## Position in the Visual Decomposition

`L2 Responsibilities`

## Related Artifacts

- [[EPIC-E6-issue-and-settle-security]]
- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]
- [[E6-01B-propose-and-approve-debt-transaction-actor-and-decision-view]]
