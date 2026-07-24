---
id: US-E6-104
project: farm-credit-ba-exercise

type: story
status: draft

description: Enables an authorized reviewer to evaluate a submitted debt transaction and record an approval decision.

categories:
  - "[[Stories]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"
tags:
  - farm-credit
  - requirements
  - debt-issuance
  - approval
  - review
  - user-story

created: 2026-07-22
updated: 2026-07-23

epic: EPIC-E6
feature: FEATURE-E6-01
---

# US-E6-104 Review Debt Transaction

## TL;DR

Enable an authorized reviewer to evaluate a submitted debt transaction and either approve it or return it for correction.

---

## User Story

As an authorized reviewer,

I want to review a submitted debt transaction and record my decision,

so that the proposed issuance is either approved to proceed or returned for correction.

---

## Business Value

Provides independent oversight of proposed debt transactions and ensures that only acceptable transactions proceed beyond the approval stage.

---

## Scope

### Included

- Authorize review of a Pending Approval transaction
- Present submitted transaction information
- Present relevant validation and submission details
- Prevent direct modification of submitted business terms
- Record an approval decision
- Record a return-for-correction decision
- Require a reason when returning a transaction
- Update the transaction workflow status
- Record reviewer identity and decision timestamp
- Make the decision available to the Issuance Officer
- Prevent duplicate decisions
- Preserve the reviewed transaction version

### Excluded

- Creation or validation of the Draft transaction
- Submission into the approval workflow
- Direct correction of transaction information by the reviewer
- Correction and resubmission by the Issuance Officer
- Issuance scheduling
- Market execution
- Settlement

---

## Related Artifacts

### Parent Feature

- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]

### Acceptance Criteria

- [[AC-E6-104]]

### Business Rules

- [[BR-FEATURE-E6-01]]

### Related Diagrams

- [[E6-01B-propose-and-approve-debt-transaction-actor-and-decision-view]]
- [[E6-01C-propose-and-approve-debt-transaction-successful-approval-sequence]]
- [[E6-01D1-propose-and-approve-debt-transaction-return-correct-and-resubmit-sequence]]
- [[E6-01D2-propose-and-approve-debt-transaction-business-decision-flow]]
- [[E6-01F-v1-propose-and-approve-debt-transaction-business-control-map-detailed]]

### Previous Story

- [[US-E6-103-submit-transaction-for-approval]]

### Next Story

- [[US-E6-105-correct-and-resubmit-returned-transaction]]

---

## Notes

The reviewer records a decision against the submitted transaction version. The reviewer does not directly change the submitted business terms.
