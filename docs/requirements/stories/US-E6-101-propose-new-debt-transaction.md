---
id: US-E6-101
project: farm-credit-ba-exercise

type: story
status: draft

description: Enables an authorized Issuance Officer to create and preserve a new debt transaction in Draft status.

categories:
  - "[[Stories]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"
tags:
  - farm-credit
  - requirements
  - debt-issuance
  - proposal
  - user-story

created: 2026-07-22
updated: 2026-07-23

epic: EPIC-E6
feature: FEATURE-E6-01
---

# US-E6-101 Propose New Debt Transaction

## TL;DR

Create a uniquely identified and traceable Draft transaction containing the initial business information required to begin the debt issuance workflow.

---

## User Story

As an Issuance Officer,

I want to create a new debt transaction proposal,

so that the debt issuance process can begin using complete and traceable business information.

---

## Business Value

Establishes the initial controlled and traceable business record required to begin the debt issuance workflow.

---

## Scope

### Included

- Authorize creation of a debt transaction
- Capture the initial required transaction information
- Identify missing required information
- Save the transaction in Draft status
- Assign a unique transaction identifier
- Record creator identity and creation timestamp
- Identify potential active duplicates
- Make the Draft transaction available for validation

### Excluded

- Detailed transaction validation
- Submission for approval
- Independent transaction review
- Approval or return decisions
- Issuance scheduling
- Market execution
- Settlement

---

## Related Artifacts

### Parent Feature

- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]

### Acceptance Criteria

- [[AC-E6-101]]

### Business Rules

- [[BR-FEATURE-E6-01]]

### Related Diagrams

- [[E6-01A-propose-and-approve-debt-transaction-business-activity-view]]
- [[E6-01E-propose-and-approve-debt-transaction-information-evolution]]

### Next Story

- [[US-E6-102-validate-proposed-transaction]]

---

## Notes

The transaction remains in Draft status until the validation requirements defined by US-E6-102 are satisfied.
