---
id: FEATURE-E6-01
project: farm-credit-ba-exercise

type: feature
status: draft

description: Allow an authorized user to propose a debt transaction and route it through validation, independent review, correction, resubmission, and approval.

categories:
  - "[[Features]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"
tags:
  - farm-credit
  - requirements
  - debt-issuance
  - transaction-approval
  - business-analysis
  - interview-study

created: 2026-07-22
updated: 2026-07-23

epic: EPIC-E6
---

# FEATURE-E6-01 — Propose and Approve Debt Transaction

## TL;DR

Allow an authorized Issuance Officer to create and validate a proposed debt transaction and route it through independent review, correction, resubmission, and approval.

## Business Objective

Provide a controlled business workflow for creating, validating, submitting, reviewing, returning, correcting, resubmitting, and approving a proposed debt transaction.

## Business Value

Reduces the risk of incomplete, invalid, or unauthorized debt transactions proceeding to issuance while preserving independent approval and an auditable decision history.

## Parent Epic

- [[EPIC-E6-issue-and-settle-security]]

## Business Need

Before a debt security can be issued, the organization must confirm that the proposed transaction is complete, valid, authorized, and independently approved.

The process must support both the successful approval path and the return-for-correction path.

## Business Outcome

An approved transaction contains the information and approval evidence needed to proceed to downstream issuance and settlement activities.

## Scope

This Feature includes:

- creation of a draft debt transaction
- assignment of a unique transaction identifier
- capture of required transaction information
- validation of required and conditional information
- correction of validation errors
- submission for Treasury review
- controlled handling of submitted transaction data
- independent approval review
- approval of acceptable transactions
- return of transactions with a reason
- correction and resubmission of returned transactions
- recording of status changes and approval history

## Out of Scope

This Feature does not include:

- execution of the debt issuance
- settlement processing
- cash movement
- accounting entries
- external dealer or investor communication
- regulatory filing
- technical implementation design

## Primary Actors

### Issuance Officer

Responsible for:

- creating the transaction proposal
- entering required information
- correcting validation issues
- submitting the transaction
- correcting and resubmitting returned transactions

### Treasury Approver

Responsible for:

- reviewing submitted transaction information
- confirming whether the proposal is acceptable
- approving the transaction
- returning the transaction with a reason when corrections are required

### Debt Issuance Platform

Responsible for:

- assigning the transaction identifier
- validating required information
- controlling transaction status
- protecting submitted information from uncontrolled change
- recording decisions, timestamps, and history

## Preconditions

- The Issuance Officer is authorized to create debt transactions.
- The Treasury Approver is authorized to review and approve transactions.
- Required reference information is available.
- The proposed transaction has not already been entered as an active duplicate.

## Trigger

The Issuance Officer identifies the need to propose a new debt transaction.

## Main Success Flow

1. The Issuance Officer creates a new debt transaction draft.
2. The platform assigns a unique transaction identifier.
3. The Issuance Officer enters the required transaction information.
4. The platform validates the proposal.
5. The Issuance Officer corrects any validation issues.
6. The Issuance Officer submits the valid transaction for approval.
7. The platform records the submitted transaction version and changes the status to Pending Approval.
8. The Treasury Approver reviews the transaction.
9. The Treasury Approver approves the transaction.
10. The platform records the approver, decision timestamp, and Approved status.
11. The approved transaction becomes available for downstream issuance processing.

## Alternate Flow — Validation Failure

1. The platform identifies missing or invalid information.
2. The transaction remains editable.
3. The platform presents the validation issues.
4. The Issuance Officer corrects the proposal.
5. The platform validates the updated proposal again.

## Alternate Flow — Return for Correction

1. The Treasury Approver determines that the submitted transaction requires correction.
2. The Treasury Approver enters a return reason.
3. The platform records the decision and changes the status to Changes Required.
4. The Issuance Officer reviews the return reason.
5. The Issuance Officer corrects the transaction.
6. The Issuance Officer resubmits the transaction.
7. The platform records the new submitted version.
8. The transaction returns to Pending Approval.

## Business Rules

- Only authorized users may create or approve transactions.
- A proposer may not approve the same transaction.
- Required information must pass validation before submission.
- Submitted transaction information must be protected from uncontrolled change.
- A returned transaction must include a reason.
- Approval must record the approver and decision timestamp.
- Material changes and status transitions must be auditable.

## Stories

- [[US-E6-101-propose-new-debt-transaction]]
- [[US-E6-102-validate-proposed-transaction]]
- [[US-E6-103-submit-transaction-for-approval]]
- [[US-E6-104-review-debt-transaction]]
- [[US-E6-105-correct-and-resubmit-returned-transaction]]

## Related Diagrams

- [[E6-01A-propose-and-approve-debt-transaction-business-activity-view]]
- [[E6-01B-propose-and-approve-debt-transaction-actor-and-decision-view]]
- [[E6-01C-propose-and-approve-debt-transaction-successful-approval-sequence]]
- [[E6-01D1-propose-and-approve-debt-transaction-return-correct-and-resubmit-sequence]]
- [[E6-01D2-propose-and-approve-debt-transaction-business-decision-flow]]
- [[E6-01E-propose-and-approve-debt-transaction-information-evolution]]
- [[E6-01F-v1-propose-and-approve-debt-transaction-business-control-map-detailed]]
- [[E6-01F-v2-propose-and-approve-debt-transaction-business-control-map-compact]]

## Related Artifacts

- [[BR-FEATURE-E6-01]]
- [[REVIEW-FEATURE-E6-01]]
