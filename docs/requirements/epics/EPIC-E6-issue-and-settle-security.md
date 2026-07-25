---
id: EPIC-E6
project: farm-credit-ba-exercise

type: epic
status: draft

description: Enable the organization to propose, approve, issue, and settle debt securities through a controlled and auditable business process.

categories:
  - "[[Epics]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"
tags:
  - farm-credit
  - requirements
  - debt-issuance
  - security-settlement
  - business-analysis
  - interview-study

created: 2026-07-22
updated: 2026-07-23
---

# EPIC-E6 — Issue and Settle Security

## TL;DR

Provide a controlled, traceable, and auditable business lifecycle for proposing, approving, issuing, settling, and reporting debt securities.

## Business Objective

Enable authorized business users to propose, review, approve, issue, and settle debt securities through a controlled, traceable, and auditable business process.

## Business Problem

Debt issuance activities may depend on fragmented workflows, manual coordination, inconsistent approvals, and limited visibility into transaction status and history.

The organization needs a standardized process that supports:

- consistent transaction capture
- validation of required transaction information
- independent review and approval
- controlled correction and resubmission
- issuance and settlement readiness
- complete transaction and approval history

## Business Value

This Epic provides the foundation for a more reliable debt issuance process by improving:

- operational consistency
- approval governance
- transaction transparency
- auditability
- error prevention
- readiness for downstream issuance and settlement

## Scope

This Epic includes the business capabilities needed to:

- propose a new debt transaction
- validate transaction information
- submit a transaction for approval
- review and approve or return the transaction
- correct and resubmit returned transactions
- preserve approval and change history
- prepare approved transactions for issuance
- support issuance and settlement processing

## Out of Scope

The current exercise does not yet define:

- detailed accounting entries
- external market connectivity
- payment-processing implementation
- security-master integration
- regulatory-reporting implementation
- technical architecture
- production deployment design

## Success Criteria

The Epic is successful when:

- authorized users can create debt transaction proposals
- required business information is validated before submission
- submitted transactions are protected from uncontrolled change
- approval decisions are independently recorded
- returned transactions include a reason for correction
- corrected transactions can be resubmitted
- approved transactions are ready for downstream issuance
- material actions and decisions are auditable

## Features

- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]
- [[FEATURE-E6-02-schedule-and-book-issuance]]
- [[FEATURE-E6-03-execute-and-allocate-issuance]]
- [[FEATURE-E6-04-confirm-and-settle-issuance]]
- [[FEATURE-E6-05-post-trade-reporting]]

## Key Actors

- Issuance Officer
- Treasury Approver
- Debt Issuance Platform
- Downstream Issuance and Settlement Functions

## Related Diagrams

- [[E6-00-issue-and-settle-security-500-foot-business-view]]
- [[E6-01A-propose-and-approve-debt-transaction-business-activity-view]]
- [[E6-01B-propose-and-approve-debt-transaction-actor-and-decision-view]]
- [[E6-01D2-propose-and-approve-debt-transaction-business-decision-flow]]
- [[E6-01E-propose-and-approve-debt-transaction-information-evolution]]
- [[E6-01F-v1-propose-and-approve-debt-transaction-business-control-map-detailed]]
- [[E6-01F-v2-propose-and-approve-debt-transaction-business-control-map-compact]]

## Related Artifacts

- [[E6-00-issue-and-settle-security-500-foot-business-view]]
