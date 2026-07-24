---
id: US-E6-105
project: farm-credit-ba-exercise

type: story
status: draft

description: Enables an Issuance Officer to correct a returned debt transaction, revalidate it, and resubmit it for approval.

categories:
  - "[[Stories]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"
tags:
  - farm-credit
  - requirements
  - debt-issuance
  - correction
  - resubmission
  - user-story

created: 2026-07-22
updated: 2026-07-23

epic: EPIC-E6
feature: FEATURE-E6-01
---

# US-E6-105 Correct and Resubmit Returned Transaction

## TL;DR

Allow an Issuance Officer to correct a returned transaction, revalidate it, and resubmit it while preserving complete submission history.

---

## User Story

As an Issuance Officer,

I want to correct a debt transaction that was returned by a reviewer and resubmit it,

so that the identified issues can be resolved and the transaction can re-enter the approval workflow.

---

## Business Value

Provides a controlled correction and resubmission process without losing the history of the original proposal, reviewer decision, or prior transaction version.

---

## Scope

### Included

- Authorize correction
- Present reviewer comments and return reason
- Modify returned transaction information
- Preserve previous submission history
- Invalidate obsolete validation results
- Require successful revalidation
- Prevent invalid resubmission
- Create a new submission
- Record submission audit information
- Route the corrected transaction for review
- Preserve complete transaction lineage

### Excluded

- Initial Draft creation
- Initial validation
- Initial submission
- Independent reviewer decision
- Issuance scheduling
- Market execution
- Settlement

---

## Related Artifacts

### Parent Feature

- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]

### Acceptance Criteria

- [[AC-E6-105]]

### Business Rules

- [[BR-FEATURE-E6-01]]

### Related Diagrams

- [[E6-01D1-propose-and-approve-debt-transaction-return-correct-and-resubmit-sequence]]
- [[E6-01D2-propose-and-approve-debt-transaction-business-decision-flow]]
- [[E6-01E-propose-and-approve-debt-transaction-information-evolution]]
- [[E6-01F-v1-propose-and-approve-debt-transaction-business-control-map-detailed]]

### Previous Story

- [[US-E6-104-review-debt-transaction]]

---

## Notes

Each resubmission represents a new approval cycle while maintaining traceability to all previous versions and reviewer decisions.
