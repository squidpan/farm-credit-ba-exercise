---
id: US-E6-103
project: farm-credit-ba-exercise

type: story
status: draft

description: Enables an authorized Issuance Officer to submit a validated debt transaction for independent approval.

categories:
  - "[[Stories]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"
tags:
  - farm-credit
  - requirements
  - debt-issuance
  - approval
  - workflow
  - user-story

created: 2026-07-22
updated: 2026-07-23

epic: EPIC-E6
feature: FEATURE-E6-01
---

# US-E6-103 Submit Transaction for Approval

## TL;DR

Submit an eligible and currently validated Draft transaction into the independent approval workflow.

---

## User Story

As an Issuance Officer,

I want to submit a validated debt transaction for approval,

so that an authorized reviewer can evaluate the proposed issuance before it proceeds to execution.

---

## Business Value

Ensures every proposed debt issuance receives an independent business review before it proceeds to execution.

---

## Scope

### Included

- Authorize submission of the transaction
- Confirm that the transaction has a current successful validation result
- Prevent submission of an ineligible transaction
- Change transaction status from Draft to Pending Approval
- Route or assign the transaction to an authorized reviewer
- Record submitter identity and submission timestamp
- Protect submitted business information from direct modification
- Prevent duplicate submission

### Excluded

- Creation of the initial Draft transaction
- Detailed transaction validation
- Reviewer evaluation of the transaction
- Approval or return decisions
- Correction of returned transactions
- Issuance scheduling
- Market execution
- Settlement

---

## Related Artifacts

### Parent Feature

- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]

### Acceptance Criteria

- [[AC-E6-103]]

### Business Rules

- [[BR-FEATURE-E6-01]]

### Related Diagrams

- [[E6-01A-propose-and-approve-debt-transaction-business-activity-view]]
- [[E6-01C-propose-and-approve-debt-transaction-successful-approval-sequence]]
- [[E6-01D2-propose-and-approve-debt-transaction-business-decision-flow]]
- [[E6-01E-propose-and-approve-debt-transaction-information-evolution]]

### Previous Story

- [[US-E6-102-validate-proposed-transaction]]

### Next Story

- [[US-E6-104-review-debt-transaction]]

---

## Notes

The transaction must have a current successful validation result at the time of submission. After submission, governed business information remains protected until the transaction is approved or returned for correction.
