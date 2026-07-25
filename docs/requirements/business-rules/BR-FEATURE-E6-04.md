---
id: BR-FEATURE-E6-04
project: farm-credit-ba-exercise

type: business-rule
status: approved

description: Defines the business rules governing dealer confirmation, settlement instructions, settlement processing, exception resolution, and final settlement completion.

categories:
  - "[[Business Rules]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"
tags:
  - farm-credit
  - requirements

created: 2026-07-23
updated: 2026-07-23

epic: EPIC-E6
feature: FEATURE-E6-04
---

# BR-FEATURE-E6-04 Confirm and Settle Issuance

## TL;DR

Defines the confirmation, settlement-instruction, monitoring, exception, and completion rules governing FEATURE-E6-04.

## Purpose

Define the business constraints that govern dealer-transaction confirmation, settlement-instruction creation and submission, settlement-status monitoring, exception resolution, and final settlement completion for an issuance.

---

## Business Rules

### BR-E6-04.1 Finalized Transactions Required

Only dealer transactions produced from completed execution and allocation processing may proceed to transaction confirmation.

---

### BR-E6-04.2 Transaction Confirmation Required

A settlement instruction must not be created until its associated dealer transaction has been confirmed.

---

### BR-E6-04.3 Confirmation Data Integrity

Confirmed dealer transaction information must agree with the finalized execution and allocation records.

---

### BR-E6-04.4 Required Settlement Information

A settlement instruction must contain all required security, quantity, amount, currency, settlement-date, settlement-method, party, and account information before it may be submitted.

---

### BR-E6-04.5 Settlement-Instruction Validation

A settlement instruction must pass all required validation before it may be marked ready for submission.

---

### BR-E6-04.6 Duplicate Instruction Prevention

Only one active settlement instruction may exist for the same dealer transaction and settlement obligation unless a replacement or resubmission is explicitly authorized and traceable.

---

### BR-E6-04.7 Submission Traceability

Every settlement-instruction submission and resubmission must preserve its submitting actor, date and time, status, and relationship to prior attempts.

---

### BR-E6-04.8 Status History Preservation

Settlement acknowledgement, rejection, processing, matching, failure, and completion statuses must be retained as part of the settlement history.

---

### BR-E6-04.9 Exception Creation

A rejected, failed, unmatched, invalid, or materially delayed settlement instruction must be identified and managed as a settlement exception.

---

### BR-E6-04.10 Authorized Corrections

Settlement information may be corrected only by an authorized actor, and the original value, corrected value, reason, user, and date and time must be retained.

---

### BR-E6-04.11 Exception Resolution Traceability

All settlement-exception investigation, corrective action, resubmission, and resolution activity must be auditable.

---

### BR-E6-04.12 Blocking Exceptions

An issuance must not be marked settled while any blocking settlement exception remains unresolved.

---

### BR-E6-04.13 Complete Dealer Settlement

Every required dealer transaction associated with the issuance must reach a settled status before the issuance may be marked settled.

---

### BR-E6-04.14 Securities and Cash Completion

Both required securities movement and required cash movement must complete successfully before settlement completion may be recorded.

---

### BR-E6-04.15 Final Settlement Record

The final settlement record must preserve the settled quantities, amounts, settlement date and time, completion actor, supporting statuses, acknowledgements, and exception history.

---

### BR-E6-04.16 Duplicate Completion Prevention

An issuance that is already marked settled must not receive an unintended duplicate settlement-completion record.

---

### BR-E6-04.17 Downstream Availability

Finalized settlement information must be available to authorized downstream accounting, reconciliation, reporting, and lifecycle processes.

---

## Related Artifacts

### Feature

- [[FEATURE-E6-04-confirm-and-settle-issuance]]

### Stories

- [[US-E6-401-confirm-dealer-transactions]]
- [[US-E6-402-create-settlement-instructions]]
- [[US-E6-403-submit-and-monitor-settlement]]
- [[US-E6-404-resolve-settlement-exceptions]]
- [[US-E6-405-record-settlement-completion]]

### Acceptance Criteria

- [[AC-E6-401]]
- [[AC-E6-402]]
- [[AC-E6-403]]
- [[AC-E6-404]]
- [[AC-E6-405]]
