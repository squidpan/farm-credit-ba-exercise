---
id: US-E6-202
project: farm-credit-ba-exercise

type: story
status: draft

description: Validate that the proposed issuance date complies with funding calendars and operational constraints.

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

# US-E6-202 Validate Issuance Window

## TL;DR

Validate the proposed issuance window before operational resources are committed.

---

## User Story

As an Issuance Officer,

I want the system to validate the proposed issuance window,

so that debt issuances occur only on approved funding days and do not conflict with operational constraints.

---

## Business Value

Validation prevents invalid or conflicting issuance schedules before funding capacity and operational resources are committed.

---

## Scope

### Included

- Funding calendar validation
- Holiday validation
- Operational conflict validation

### Excluded

- Funding capacity reservation
- Security identifier assignment
- Booking the planned issuance

---

## Related Artifacts

### Parent Feature

- [[FEATURE-E6-02-schedule-and-book-issuance]]

### Acceptance Criteria

- [[AC-E6-202]]

### Business Rules

- [[BR-FEATURE-E6-02]]

---

## Notes
