---
id: US-E6-204
project: farm-credit-ba-exercise

type: story
status: draft

description: Assign a unique security identifier to a planned issuance after funding capacity has been reserved.

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

# US-E6-204 Assign Security Identifier

## TL;DR

Assign a unique security identifier before the planned issuance is booked.

---

## User Story

As a Funding Operations Analyst,

I want the system to assign a unique security identifier to the planned issuance,

so that the security can be tracked consistently throughout booking, execution, settlement, and lifecycle processing.

---

## Business Value

A unique security identifier prevents duplicate records and provides a consistent reference across downstream issuance and settlement activities.

---

## Scope

### Included

- Generate or obtain a security identifier
- Validate identifier uniqueness
- Associate the identifier with the planned issuance
- Record identifier assignment

### Excluded

- Booking the planned issuance
- Market execution
- Settlement processing
- Post-trade reporting

---

## Related Artifacts

### Parent Feature

- [[FEATURE-E6-02-schedule-and-book-issuance]]

### Acceptance Criteria

- [[AC-E6-204]]

### Business Rules

- [[BR-FEATURE-E6-02]]

---

## Notes
