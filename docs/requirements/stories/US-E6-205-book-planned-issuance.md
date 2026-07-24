---
id: US-E6-205
project: farm-credit-ba-exercise

type: story
status: draft

description: Book a validated planned issuance after funding capacity and security identification are complete.

categories:
  - "[[Stories]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"
tags:
  - farm-credit
  - requirements

created: 2026-07-23
updated: 2026-07-23

epic: EPIC-E6
feature: FEATURE-E6-02
---

# US-E6-205 Book Planned Issuance

## TL;DR

Create the official planned issuance record after all scheduling prerequisites are complete.

---

## User Story

As a Funding Operations Analyst,

I want to book the planned issuance,

so that the approved issuance is recorded and available for execution and downstream processing.

---

## Business Value

Booking creates the authoritative issuance record used by execution, allocation, settlement, reporting, and lifecycle processes.

---

## Scope

### Included

- Confirm scheduling prerequisites
- Create the planned issuance record
- Record booking date and time
- Record the user or process that completed the booking
- Set the planned issuance to booked status

### Excluded

- Market execution
- Investor allocation
- Trade confirmation
- Settlement processing
- Post-trade reporting

---

## Related Artifacts

### Parent Feature

- [[FEATURE-E6-02-schedule-and-book-issuance]]

### Acceptance Criteria

- [[AC-E6-205]]

### Business Rules

- [[BR-FEATURE-E6-02]]

---

## Notes
