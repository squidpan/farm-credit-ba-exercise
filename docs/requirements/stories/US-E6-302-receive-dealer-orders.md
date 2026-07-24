---
id: US-E6-302
project: farm-credit-ba-exercise

type: story
status: draft

description: Enables authorized dealers to submit orders for an executed debt issuance.

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

# US-E6-302 Receive Dealer Orders

## TL;DR

Accept dealer orders for an executed issuance and preserve them for allocation processing.

---

## User Story

As an Issuance Officer,

I want authorized dealers to submit orders for an executed issuance,

so that securities can be allocated according to the issuance results.

---

## Business Value

Capturing dealer participation establishes market demand and provides the input required for allocation decisions.

---

## Scope

### Included

- Accept dealer orders
- Validate dealer eligibility
- Record submitted order details
- Preserve submission time
- Make accepted orders available for allocation

### Excluded

- Allocation decisions
- Settlement
- Dealer onboarding
- Post-trade reporting

---

## Related Artifacts

### Parent Feature

- [[FEATURE-E6-03-execute-and-allocate-issuance]]

### Acceptance Criteria

- [[AC-E6-302]]

### Business Rules

- [[BR-FEATURE-E6-03]]

---

## Notes

Only orders submitted during the authorized execution window are eligible for allocation.
