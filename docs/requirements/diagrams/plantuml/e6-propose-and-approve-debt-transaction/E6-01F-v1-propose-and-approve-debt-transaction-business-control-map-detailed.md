---
id: E6-01F-v1
project: farm-credit-ba-exercise
type: diagram-guide
status: approved
epic: E6
feature: E6-01
diagram: E6-01F-v1-propose-and-approve-debt-transaction-business-control-map-detailed.puml
layer: "L5 Business Controls"

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

description: What control points protect data quality, submission integrity, approval governance, and audit evidence?
created: 2026-07-21
updated: 2026-07-22
---

# E6-01F-v1-propose-and-approve-debt-transaction-business-control-map-detailed

## Business Question

What control points protect data quality, submission integrity, approval governance, and audit evidence?

## Purpose

Provide the detailed control view and show why each control exists.

## How to Explain It

This detailed control map shows four control gates. Control 1 prevents incomplete or ineligible transactions. Control 2 creates and protects the submitted snapshot. Control 3 enforces authorization, approval limits, and segregation of duties. Control 4 preserves the decision, version history, notifications, and approved terms. I would use this with risk, compliance, audit, or a product owner when converting governance expectations into requirements and tests.

## Key Talking Points

- Controls occur before and after the approval decision.
- Data quality includes required fields, product rules, dates, reference data, and limits.
- Submission integrity protects what the approver actually reviewed.
- Approval governance prevents unauthorized or conflicted decisions.
- Audit integrity preserves evidence of what was approved, by whom, and when.

## What This Diagram Does Not Show

The full process sequence or product-specific rule definitions.

## Position in the Visual Decomposition

`L5 Business Controls`

## Related Artifacts

- [[EPIC-E6-issue-and-settle-security]]
- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]
- [[E6-01F-v1-propose-and-approve-debt-transaction-business-control-map-detailed]]
