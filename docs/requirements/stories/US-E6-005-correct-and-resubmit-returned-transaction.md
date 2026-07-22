---
id: US-E6-005
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
  - correction
  - resubmission
  - user-story

description: Enables an Issuance Officer to correct a returned debt transaction, revalidate it, and resubmit it for approval.

created: 2026-07-22
updated: 2026-07-22
---

# US-E6-005 — Correct and Resubmit Returned Transaction

## User Story

As an Issuance Officer,

I want to correct a debt transaction that was returned by a reviewer and resubmit it,

so that the identified issues can be resolved and the transaction can re-enter the approval workflow.

## Business Context

A reviewer may return a proposed debt transaction when information is incomplete, incorrect, or otherwise unsuitable for approval.

The returned transaction must preserve the prior submission and decision history while allowing an authorized Issuance Officer to make corrections, revalidate the transaction, and submit a new version for review.

## Business Value

Provides a controlled correction and resubmission process without losing the history of the original proposal, reviewer decision, or prior transaction version.

## Preconditions

- A debt transaction is in Returned for Correction status.
- A return decision and return reason have been recorded.
- The Issuance Officer is authorized to modify and resubmit the transaction.
- The previously submitted version and reviewer decision remain preserved.

## Trigger

The Issuance Officer opens the returned transaction and begins correcting the identified issues.

## Acceptance Criteria

### AC-E6-005-01 — Authorize Correction

Given a transaction is in Returned for Correction status,

when a user attempts to edit it,

then the platform permits changes only when the user is authorized to correct the transaction.

### AC-E6-005-02 — Present the Return Reason

Given the Issuance Officer opens the returned transaction,

when the correction activity begins,

then the platform presents the reviewer decision, return reason, and relevant comments.

### AC-E6-005-03 — Permit Correction of Business Information

Given the Issuance Officer is authorized to correct the transaction,

when changes are made,

then the platform permits modification of the applicable business information.

### AC-E6-005-04 — Preserve Prior Submission History

Given a returned transaction is modified,

when the corrected version is saved,

then the platform preserves the previously submitted version and its associated reviewer decision.

### AC-E6-005-05 — Invalidate Prior Validation Results

Given material transaction information is changed,

when the corrected transaction is saved,

then the platform marks prior validation results as no longer current.

### AC-E6-005-06 — Require Revalidation

Given the transaction has been corrected,

when the Issuance Officer attempts to resubmit it,

then the platform requires a current successful validation result.

### AC-E6-005-07 — Prevent Resubmission When Validation Fails

Given the corrected transaction does not have a current successful validation result,

when resubmission is requested,

then the platform rejects the request and keeps the transaction in Returned for Correction status.

### AC-E6-005-08 — Resubmit the Corrected Transaction

Given the corrected transaction has a current successful validation result,

when the authorized Issuance Officer resubmits it,

then the platform changes the transaction status from Returned for Correction to Pending Approval.

### AC-E6-005-09 — Create a New Submission Record

Given the corrected transaction is successfully resubmitted,

when processing completes,

then the platform records a new submission event with the submitter identity and submission timestamp.

### AC-E6-005-10 — Route the Corrected Transaction for Review

Given the corrected transaction enters Pending Approval status,

when resubmission completes,

then the platform routes or assigns the new submission to an authorized reviewer according to the applicable approval rules.

### AC-E6-005-11 — Preserve Submission Lineage

Given the transaction has been resubmitted,

when its history is reviewed,

then the platform associates the original submission, return decision, corrected version, and new submission as part of the same transaction lifecycle.

## Expected Outcome

The corrected transaction has a current successful validation result, is in Pending Approval status, and has a new submission record linked to the prior returned submission and reviewer decision.

## Related Feature

- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]

## Previous Story

- [[US-E6-004-review-debt-transaction]]

## Related Diagrams

- [[E6-01D1-propose-and-approve-debt-transaction-return-correct-and-resubmit-sequence]]
- [[E6-01D2-propose-and-approve-debt-transaction-business-decision-flow]]
- [[E6-01E-propose-and-approve-debt-transaction-information-evolution]]
- [[E6-01F-v1-propose-and-approve-debt-transaction-business-control-map-detailed]]

