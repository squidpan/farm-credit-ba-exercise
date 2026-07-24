---
id: US-E6-102
project: farm-credit-ba-exercise

type: story
status: draft

description: Validates a proposed debt transaction and identifies issues that must be corrected before submission.

categories:
  - "[[Stories]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"
tags:
  - farm-credit
  - requirements
  - debt-issuance
  - validation
  - user-story

created: 2026-07-22
updated: 2026-07-23

epic: EPIC-E6
feature: FEATURE-E6-01
---

# US-E6-102 Validate Proposed Transaction

## TL;DR

Validate a Draft debt transaction and identify issues that must be corrected before the transaction can enter the approval workflow.

---

## User Story

As an Issuance Officer,

I want the proposed debt transaction to be validated,

so that incomplete or invalid business information is corrected before the transaction is submitted for approval.

---

## Business Value

Improves transaction quality and reduces avoidable review delays and downstream processing errors.

---

## Scope

### Included

- Authorize validation of a Draft transaction
- Apply required-field validation
- Apply format and consistency validation
- Apply eligibility and reference-data validation
- Record successful validation
- Identify validation issues
- Keep invalid transactions in Draft status
- Permit correction and revalidation
- Invalidate previous results following material changes
- Make successfully validated transactions eligible for submission

### Excluded

- Creation of the initial Draft transaction
- Submission into the approval workflow
- Reviewer assignment
- Independent approval review
- Approval or return decisions
- Issuance scheduling
- Market execution
- Settlement

---

## Related Artifacts

### Parent Feature

- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]

### Acceptance Criteria

- [[AC-E6-102]]

### Business Rules

- [[BR-FEATURE-E6-01]]

### Related Diagrams

- [[E6-01A-propose-and-approve-debt-transaction-business-activity-view]]
- [[E6-01D2-propose-and-approve-debt-transaction-business-decision-flow]]
- [[E6-01E-propose-and-approve-debt-transaction-information-evolution]]

### Previous Story

- [[US-E6-101-propose-new-debt-transaction]]

### Next Story

- [[US-E6-103-submit-transaction-for-approval]]

---

## Notes

A validation result must remain current. Material changes to transaction information require the transaction to be validated again before submission.
