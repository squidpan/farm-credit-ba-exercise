---
id: FEATURE-E6-02
project: farm-credit-ba-exercise

type: feature
status: draft

description: Schedule, validate, reserve capacity for, identify, and book a planned debt issuance.

categories:
  - "[[Features]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"
tags:
  - farm-credit
  - requirements

created: 2026-07-23
updated: 2026-07-23

epic: EPIC-E6
---

# FEATURE-E6-02 Schedule and Book Issuance

## TL;DR

Convert an approved debt transaction into a validated and booked planned issuance that is ready for market execution.

---

## Feature Description

This feature supports the operational preparation of an approved debt transaction.

The workflow begins when an Issuance Officer schedules the proposed issuance. The proposed schedule is validated against funding calendars and operational constraints. Funding capacity is then reserved, a unique security identifier is assigned, and the planned issuance is booked as the authoritative record for downstream processing.

---

## Business Objective

Provide a controlled and traceable process for preparing an approved debt transaction for execution.

---

## Business Value

This feature:

- Prevents issuances from being scheduled on invalid dates
- Ensures sufficient funding capacity exists
- Prevents duplicate security identifiers
- Creates an authoritative issuance record
- Provides downstream teams with reliable issuance information
- Supports auditability and operational control

---

## Primary Actors

- Issuance Officer
- Funding Operations Analyst
- Funding Strategy Analyst

---

## Preconditions

- The proposed debt transaction has completed the required approval process
- Required transaction information is available
- The funding calendar is available
- Funding-capacity information is available

---

## Trigger

An approved debt transaction is ready to be scheduled for issuance.

---

## Scope

### Included

- Schedule the proposed issuance
- Validate the issuance window
- Reserve funding capacity
- Assign a unique security identifier
- Book the planned issuance
- Record processing and rejection information

### Excluded

- Debt transaction proposal and approval
- Market execution
- Investor allocation
- Trade confirmation
- Settlement
- Post-trade reporting
- Security lifecycle events

---

## Functional Flow

1. The Issuance Officer schedules the proposed issuance.
2. The system validates the proposed issuance window.
3. Funding Operations reserves the required funding capacity.
4. A unique security identifier is assigned.
5. Funding Operations books the planned issuance.
6. The booked issuance becomes available for downstream execution and allocation.

---

## Business Rules

- [[BR-FEATURE-E6-02]]

---

## Stories

- [[US-E6-201-schedule-issuance]]
- [[US-E6-202-validate-issuance-window]]
- [[US-E6-203-reserve-funding-capacity]]
- [[US-E6-204-assign-security-identifier]]
- [[US-E6-205-book-planned-issuance]]

---

## Acceptance Criteria

- [[AC-E6-201]]
- [[AC-E6-202]]
- [[AC-E6-203]]
- [[AC-E6-204]]
- [[AC-E6-205]]

---

## Review

- [[REVIEW-FEATURE-E6-02-requirements-walkthrough]]

---

## Related Artifacts

- [[EPIC-E6-issue-and-settle-security]]
- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]
- [[REVIEW-FEATURE-E6-02-requirements-walkthrough]]

## Completion Conditions

FEATURE-E6-02 is complete when:

- The proposed issuance has been scheduled
- The issuance window has passed validation
- Funding capacity has been reserved
- A unique security identifier has been assigned
- The planned issuance has been booked
- The authoritative booked record is available for downstream processing

---

## Notes
