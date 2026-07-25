---
id: BR-FEATURE-E6-03
project: farm-credit-ba-exercise

type: business-rule
status: approved

description: Defines the business rules governing execution, dealer-order capture, allocation, and finalization of an issuance.

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
feature: FEATURE-E6-03
---

# BR-FEATURE-E6-03 Execute and Allocate Issuance

## TL;DR

Defines the eligibility, execution, dealer-order, allocation, and execution-record rules governing FEATURE-E6-03.

## Purpose

Define the business rules that govern execution of a booked issuance, receipt of dealer orders, allocation of securities, and creation of the final execution record.

---

## Business Rules

### BR-E6-03.1 Execution Eligibility

Only a booked issuance with a valid security identifier may be executed.

---

### BR-E6-03.2 Authorized Execution

Only an authorized user or approved system process may execute an issuance.

---

### BR-E6-03.3 Single Execution Record

An issuance may have only one active execution record unless an authorized correction or cancellation process is completed.

---

### BR-E6-03.4 Dealer Eligibility

Only dealers authorized for the issuance may submit orders.

---

### BR-E6-03.5 Order Submission Window

Dealer orders must be submitted within the authorized order-submission window unless an approved exception is recorded.

---

### BR-E6-03.6 Required Order Information

Each dealer order must identify the issuance, participating dealer, requested quantity, and submission date and time.

---

### BR-E6-03.7 Accepted Orders Only

Only accepted and validated dealer orders may participate in allocation.

---

### BR-E6-03.8 Allocation Limit

The total allocated quantity must not exceed the executed issuance quantity.

---

### BR-E6-03.9 Allocation Traceability

Each dealer allocation must be traceable to its originating dealer order and the executed issuance.

---

### BR-E6-03.10 Unallocated Quantity

Any difference between the executed quantity and total allocated quantity must be recorded.

---

### BR-E6-03.11 Settlement Readiness

An issuance may be marked ready for settlement only after the execution and allocation results have been validated and finalized.

---

### BR-E6-03.12 Final Record Protection

Finalized execution and allocation results may be changed only through an authorized correction process.

---

### BR-E6-03.13 Audit Information

Execution, order submission, allocation, rejection, correction, and finalization events must preserve the responsible user or process and the event date and time.

---

## Related Artifacts

### Feature

- [[FEATURE-E6-03-execute-and-allocate-issuance]]

### Stories

- [[US-E6-301-execute-issuance]]
- [[US-E6-302-receive-dealer-orders]]
- [[US-E6-303-allocate-securities]]
- [[US-E6-304-record-execution-results]]

### Acceptance Criteria

- [[AC-E6-301]]
- [[AC-E6-302]]
- [[AC-E6-303]]
- [[AC-E6-304]]
