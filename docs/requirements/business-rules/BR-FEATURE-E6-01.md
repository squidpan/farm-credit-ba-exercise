---
id: BR-FEATURE-E6-01
project: farm-credit-ba-exercise

type: business-rule
status: approved

description: Business rules governing the proposal and approval workflow for debt transactions.

categories:
  - "[[Business Rules]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"
tags:
  - farm-credit
  - requirements
  - business-rules
  - debt-issuance

created: 2026-07-22
updated: 2026-07-23

epic: EPIC-E6
feature: FEATURE-E6-01
---

# BR-FEATURE-E6-01 — Business Rules for FEATURE-E6-01

## TL;DR

Defines the authorization, validation, approval, resubmission, history, and audit rules governing proposed debt transactions.

## Business Rules

| Rule ID | Business Rule |
|---------|---------------|
| BR-E6-001 | Only authorized Issuance Officers may create Draft debt transactions. |
| BR-E6-002 | A debt transaction must successfully pass validation before it may be submitted for approval. |
| BR-E6-003 | Only transactions in Pending Approval status may be reviewed. |
| BR-E6-004 | Only authorized reviewers may approve or return a transaction. |
| BR-E6-005 | An approval decision is immutable once recorded. |
| BR-E6-006 | Returned transactions preserve all previous submission history. |
| BR-E6-007 | A corrected transaction must be revalidated before resubmission. |
| BR-E6-008 | Every submission and approval decision must create an auditable record. |

## Related Artifacts

### Related Feature

- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]

### Related Stories

- [[US-E6-101-propose-new-debt-transaction]]
- [[US-E6-102-validate-proposed-transaction]]
- [[US-E6-103-submit-transaction-for-approval]]
- [[US-E6-104-review-debt-transaction]]
- [[US-E6-105-correct-and-resubmit-returned-transaction]]
