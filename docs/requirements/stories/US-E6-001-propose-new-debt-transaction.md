---
id: US-E6-001
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
  - proposal
  - user-story

description: Enables an authorized Issuance Officer to create and preserve a new debt transaction in Draft status.

created: 2026-07-22
updated: 2026-07-22
---

# US-E6-001 — Propose New Debt Transaction

## User Story

As an Issuance Officer,

I want to create a new debt transaction proposal,

so that the debt issuance process can begin using complete and traceable business information.

## Business Context

Every debt issuance begins with a business proposal.

This story covers creation of the initial Draft transaction that will later be validated, reviewed, approved, issued, and settled.

## Business Value

Establishes the initial controlled and traceable business record required to begin the debt issuance workflow.

## Preconditions

- The Issuance Officer is authenticated.
- The Issuance Officer is authorized to create debt transactions.
- Required reference information is available.
- The proposed transaction has not already been entered as an active duplicate.

## Trigger

The Issuance Officer initiates creation of a new debt transaction proposal.

## Acceptance Criteria

### AC-E6-001-01 — Authorize Transaction Creation

Given a user is authenticated,

when the user attempts to create a debt transaction,

then the platform permits the action only when the user is authorized to create debt transactions.

### AC-E6-001-02 — Capture Required Transaction Information

Given an authorized Issuance Officer is creating a debt transaction,

when the officer enters the proposal information,

then the platform provides the required fields needed to establish the initial transaction record.

### AC-E6-001-03 — Identify Missing Required Information

Given an authorized Issuance Officer is creating a debt transaction,

when required information is missing,

then the platform identifies the missing information and does not treat the proposal as ready for validation.

### AC-E6-001-04 — Create Draft Transaction

Given the minimum information required to establish a transaction has been entered,

when the Issuance Officer saves the proposal,

then the platform creates the transaction in Draft status.

### AC-E6-001-05 — Assign Transaction Identity and Audit Information

Given a new Draft transaction is created,

when the platform saves the transaction,

then it assigns a unique transaction identifier and records the creator identity and creation timestamp.

### AC-E6-001-06 — Detect Potential Active Duplicates

Given a proposed transaction may duplicate an existing active transaction,

when the Issuance Officer attempts to save the proposal,

then the platform identifies the potential duplicate for resolution before the proposal proceeds.

## Expected Outcome

A uniquely identified Draft transaction exists with its initial business information and creation history recorded.

The transaction is available for validation.

## Related Feature

- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]

## Related Diagrams

- [[E6-01A-propose-and-approve-debt-transaction-business-activity-view]]
- [[E6-01E-propose-and-approve-debt-transaction-information-evolution]]

## Next Story

- [[US-E6-002-validate-proposed-transaction]]
