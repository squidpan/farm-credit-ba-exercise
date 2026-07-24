---
id: US-E6-301
project: farm-credit-ba-exercise

type: story
status: draft

description: Enables an authorized Issuance Officer to execute a booked issuance and record the execution event.

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
feature: FEATURE-E6-03
---

# US-E6-301 Execute Issuance

## TL;DR

Execute an eligible booked issuance and record the resulting execution status and audit information.

---

## User Story

As an Issuance Officer,

I want to execute a booked issuance,

so that dealer participation and allocation activities can begin.

---

## Business Value

Execution moves the issuance from booking into active market processing and establishes the authoritative event required for dealer participation, allocation, and downstream settlement.

---

## Scope

### Included

- Confirm that the issuance is eligible for execution
- Execute the booked issuance
- Record the execution status
- Record the execution date and time
- Record the responsible user or process
- Make the executed issuance available for dealer participation

### Excluded

- Capturing dealer orders
- Allocating securities
- Releasing execution results to settlement
- Performing settlement
- Producing post-trade reports

---

## Related Artifacts

### Parent Feature

- [[FEATURE-E6-03-execute-and-allocate-issuance]]

### Acceptance Criteria

- [[AC-E6-301]]

### Business Rules

- [[BR-FEATURE-E6-03]]

---

## Notes

Execution should not be permitted until the planned issuance has been successfully booked and contains the required security identification.
