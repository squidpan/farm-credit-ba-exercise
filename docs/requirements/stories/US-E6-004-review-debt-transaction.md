---
id: US-E6-004
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
  - review
  - user-story

description: Enables an authorized reviewer to evaluate a submitted debt transaction and record an approval decision.

created: 2026-07-22
updated: 2026-07-22
---

# US-E6-004 — Review Debt Transaction

## User Story

As an authorized reviewer,

I want to review a submitted debt transaction and record my decision,

so that the proposed issuance is either approved to proceed or returned for correction.

## Business Context

A transaction in Pending Approval status requires independent review before it can proceed to downstream issuance activities.

This story covers review of the submitted transaction, recording a decision, and updating the transaction workflow state.

## Business Value

Provides independent oversight of proposed debt transactions and ensures that only acceptable transactions proceed beyond the approval stage.

## Preconditions

- A debt transaction is in Pending Approval status.
- The transaction has been routed or assigned to an authorized reviewer.
- The reviewer has access to the submitted transaction information.
- No approval decision has already been recorded for the current submission.

## Trigger

The authorized reviewer opens the Pending Approval transaction and initiates review.

## Acceptance Criteria

### AC-E6-004-01 — Authorize Transaction Review

Given a transaction is in Pending Approval status,

when a user attempts to review it,

then the platform permits the review only when the user is authorized to perform the approval action.

### AC-E6-004-02 — Present Submitted Transaction Information

Given an authorized reviewer opens the transaction,

when the review begins,

then the platform presents the submitted transaction information and relevant validation and submission details.

### AC-E6-004-03 — Prevent Reviewer Modification of Submitted Terms

Given the reviewer is evaluating the transaction,

when the reviewer attempts to modify submitted business terms,

then the platform prevents direct modification of those terms.

### AC-E6-004-04 — Approve the Transaction

Given the reviewer determines that the transaction is acceptable,

when the reviewer records an approval decision,

then the platform changes the transaction status from Pending Approval to Approved.

### AC-E6-004-05 — Return the Transaction for Correction

Given the reviewer determines that changes are required,

when the reviewer records a return decision,

then the platform requires a return reason and changes the transaction status from Pending Approval to Returned for Correction.

### AC-E6-004-06 — Record Approval Decision Audit Information

Given the reviewer records an approval or return decision,

when the decision is accepted,

then the platform records the reviewer identity, decision, decision timestamp, and any required comments or reason.

### AC-E6-004-07 — Make the Decision Available

Given an approval decision has been recorded,

when processing completes,

then the platform makes the decision and resulting transaction status available to the Issuance Officer.

### AC-E6-004-08 — Prevent Duplicate Decision

Given an approval decision has already been recorded for the current submission,

when another decision is attempted,

then the platform prevents a second decision from being recorded for that submission.

### AC-E6-004-09 — Preserve the Submitted Version

Given the reviewer records a decision,

when processing completes,

then the platform preserves the version of the transaction that was reviewed and associates the decision with that version.

## Expected Outcome

The transaction has a recorded review decision.

An accepted transaction is in Approved status and may proceed to the next issuance activity, while a transaction requiring changes is in Returned for Correction status with the return reason available to the Issuance Officer.

## Related Feature

- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]

## Previous Story

- [[US-E6-003-submit-transaction-for-approval]]

## Related Diagrams

- [[E6-01B-propose-and-approve-debt-transaction-actor-and-decision-view]]
- [[E6-01C-propose-and-approve-debt-transaction-successful-approval-sequence]]
- [[E6-01D1-propose-and-approve-debt-transaction-return-correct-and-resubmit-sequence]]
- [[E6-01D2-propose-and-approve-debt-transaction-business-decision-flow]]
- [[E6-01F-v1-propose-and-approve-debt-transaction-business-control-map-detailed]]

## Next Story

- [[US-E6-005-correct-and-resubmit-returned-transaction]]
