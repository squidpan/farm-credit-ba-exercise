---
id: US-E6-201
project: farm-credit-ba-exercise

type: story
status: draft

description: Schedule an approved debt transaction as a proposed issuance.

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

# US-E6-201 Schedule Issuance

## TL;DR

Capture the required scheduling information for an approved debt transaction before issuance-window validation.

---

## User Story

As an Issuance Officer,

I want to schedule an approved debt transaction for issuance,

so that the proposed issuance can be validated and prepared for booking.

---

## Business Value

Scheduling converts an approved debt transaction into an operationally actionable planned issuance and provides the information needed for validation and downstream preparation.

---

## Preconditions

- The debt transaction has received the required approvals
- Required transaction information is available
- The user is authorized to schedule an issuance

---

## Scope

### Included

- Select the approved debt transaction
- Enter the proposed issuance date
- Enter the expected settlement date
- Confirm security type
- Confirm planned issuance amount
- Confirm maturity information
- Record the responsible business area
- Save the issuance in a scheduled or preliminary state

### Excluded

- Issuance-window validation
- Funding-capacity reservation
- Security identifier assignment
- Booking the planned issuance
- Market execution

---

## Related Artifacts

### Parent Feature

- [[FEATURE-E6-02-schedule-and-book-issuance]]

### Acceptance Criteria

- [[AC-E6-201]]

### Business Rules

- [[BR-FEATURE-E6-02]]

---

## Notes
