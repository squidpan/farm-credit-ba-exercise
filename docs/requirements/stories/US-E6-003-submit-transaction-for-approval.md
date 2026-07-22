---
id: US-E6-003
project: farm-credit-ba-exercise
type: user-story
status: draft

epic: EPIC-E6
feature: FEATURE-E6-01

categories:
  - "[[Stories]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"

tags:
  - farm-credit
  - debt-issuance
  - approval
  - workflow
  - user-story

description: Enables an authorized Issuance Officer to submit a validated debt transaction for independent approval.

created: 2026-07-22
updated: 2026-07-22
---

# US-E6-003 — Submit Transaction for Approval

## User Story

As an Issuance Officer,

I want to submit a validated debt transaction for approval,

so that an authorized reviewer can evaluate the proposed issuance before it proceeds to execution.

## Business Context

Only validated transactions may enter the approval workflow.

This story transfers responsibility from the transaction creator to an authorized reviewer while preserving the transaction state and submission audit information.

## Business Value

Ensures every proposed debt issuance receives an independent business review before it proceeds to execution.

## Preconditions

- A Draft debt transaction exists.
- The transaction has a current successful validation result.
- The Issuance Officer is authorized to submit the transaction.
- The transaction has not already entered the approval workflow.

## Trigger

The Issuance Officer submits the validated Draft transaction for approval.

## Acceptance Criteria

### AC-E6-003-01 — Authorize Submission

Given a validated Draft transaction exists,

when a user requests submission,

then the platform permits the action only when the user is authorized to submit the transaction.

### AC-E6-003-02 — Verify Current Validation

Given an authorized Issuance Officer submits the transaction,

when the platform evaluates submission eligibility,

then it confirms that the transaction has a current successful validation result.

### AC-E6-003-03 — Prevent Submission of an Ineligible Transaction

Given the transaction does not have a current successful validation result,

when submission is requested,

then the platform rejects the submission and keeps the transaction in Draft status.

### AC-E6-003-04 — Transition Transaction Status

Given the transaction is eligible for submission,

when submission completes successfully,

then the platform changes the transaction status from Draft to Pending Approval.

### AC-E6-003-05 — Route Transaction for Review

Given the transaction enters Pending Approval status,

when submission completes,

then the platform routes or assigns the transaction to an authorized reviewer according to the applicable approval rules.

### AC-E6-003-06 — Record Submission Audit Information

Given the transaction is successfully submitted,

when processing completes,

then the platform records the submitter identity and submission timestamp.

### AC-E6-003-07 — Protect the Submitted Transaction

Given a transaction is in Pending Approval status,

when a user attempts to modify business information governed by the approval request,

then the platform prevents the modification unless an applicable workflow action returns the transaction for correction.

### AC-E6-003-08 — Prevent Duplicate Submission

Given a transaction is already in Pending Approval status,

when another submission request is received,

then the platform prevents the transaction from being submitted a second time.

## Expected Outcome

The transaction is in Pending Approval status, has recorded submission audit information, and is available to an authorized reviewer for an approval decision.

## Related Feature

- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]

## Previous Story

- [[US-E6-002-validate-proposed-transaction]]

## Related Diagrams

- [[E6-01A-propose-and-approve-debt-transaction-business-activity-view]]
- [[E6-01C-propose-and-approve-debt-transaction-successful-approval-sequence]]
- [[E6-01D2-propose-and-approve-debt-transaction-business-decision-flow]]
- [[E6-01E-propose-and-approve-debt-transaction-information-evolution]]

## Next Story

- [[US-E6-004-review-debt-transaction]]
