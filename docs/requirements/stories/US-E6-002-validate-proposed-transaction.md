---
id: US-E6-002
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
  - validation
  - user-story

description: Validates a proposed debt transaction and identifies issues that must be corrected before submission.

created: 2026-07-22
updated: 2026-07-22
---

# US-E6-002 — Validate Proposed Transaction

## User Story

As an Issuance Officer,

I want the proposed debt transaction to be validated,

so that incomplete or invalid business information is corrected before the transaction is submitted for approval.

## Business Context

A transaction must contain complete and valid business information before it enters the approval workflow.

This story covers validation of a Draft transaction and correction of identified validation issues.

## Business Value

Improves transaction quality and reduces avoidable review delays and downstream processing errors.

## Preconditions

- A Draft debt transaction exists.
- The Issuance Officer is authorized to maintain the transaction.
- Applicable reference information and validation rules are available.
- The transaction has not been submitted for approval.

## Trigger

The Issuance Officer requests validation or attempts to submit the Draft transaction for approval.

## Acceptance Criteria

### AC-E6-002-01 — Authorize Transaction Validation

Given a Draft transaction exists,

when a user requests validation,

then the platform permits the action only when the user is authorized to maintain the transaction.

### AC-E6-002-02 — Evaluate Applicable Validation Rules

Given an authorized Issuance Officer requests validation,

when the platform evaluates the transaction,

then it applies the required field, format, consistency, eligibility, and reference-data validation rules applicable to the proposal.

### AC-E6-002-03 — Record Successful Validation

Given the transaction satisfies all applicable validation rules,

when validation completes,

then the platform records a successful validation result and makes the transaction eligible for submission.

### AC-E6-002-04 — Identify Validation Issues

Given the transaction does not satisfy one or more applicable validation rules,

when validation completes,

then the platform identifies each validation issue and provides sufficient information for the Issuance Officer to correct it.

### AC-E6-002-05 — Retain Draft Status After Validation Failure

Given one or more validation issues exist,

when validation fails,

then the transaction remains in Draft status and cannot be submitted for approval.

### AC-E6-002-06 — Permit Correction and Revalidation

Given validation issues have been identified,

when the Issuance Officer corrects the transaction and requests validation again,

then the platform evaluates the updated transaction using the applicable validation rules.

### AC-E6-002-07 — Invalidate Prior Results After Material Change

Given a transaction previously passed validation,

when the Issuance Officer changes information that affects validation,

then the platform marks the previous validation result as no longer current and requires revalidation before submission.

## Expected Outcome

The Draft transaction has a current validation result.

A valid transaction is eligible for submission, while an invalid transaction remains in Draft status with identified issues available for correction.

## Related Feature

- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]

## Previous Story

- [[US-E6-001-propose-new-debt-transaction]]

## Related Diagrams

- [[E6-01A-propose-and-approve-debt-transaction-business-activity-view]]
- [[E6-01D2-propose-and-approve-debt-transaction-business-decision-flow]]
- [[E6-01E-propose-and-approve-debt-transaction-information-evolution]]

## Next Story

- [[US-E6-003-submit-transaction-for-approval]]
