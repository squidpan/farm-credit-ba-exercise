---
id: BR-FEATURE-E6-01
project: farm-credit-ba-exercise
type: business-rule
status: approved

feature: FEATURE-E6-01

categories:
  - "[[Business Rules]]"
  - "[[Requirements]]"

tags:
  - farm-credit
  - business-rules
  - debt-issuance

description: Business rules governing the proposal and approval workflow for debt transactions.

created: 2026-07-22
updated: 2026-07-22
---

# Business Rules — FEATURE-E6-01

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

## Related Feature

- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]

## Related Stories

- [[US-E6-001-propose-new-debt-transaction]]
- [[US-E6-002-validate-proposed-transaction]]
- [[US-E6-003-submit-transaction-for-approval]]
- [[US-E6-004-review-debt-transaction]]
- [[US-E6-005-correct-and-resubmit-returned-transaction]]
