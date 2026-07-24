---
id: US-E6-303
project: farm-credit-ba-exercise

type: story
status: draft

description: Enables an Issuance Officer to allocate executed securities across accepted dealer orders.

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

# US-E6-303 Allocate Securities

## TL;DR

Allocate the executed issuance across accepted dealer orders and preserve the allocation results.

---

## User Story

As an Issuance Officer,

I want to allocate securities across accepted dealer orders,

so that each participating dealer receives an approved portion of the issuance.

---

## Business Value

Allocation converts dealer demand into executable distribution results and provides the dealer-level quantities required for settlement.

---

## Scope

### Included

- Review accepted dealer orders
- Determine allocation quantities
- Ensure total allocation does not exceed the executed amount
- Record dealer-level allocation results
- Identify unallocated quantity
- Make completed allocations available for execution-result recording

### Excluded

- Dealer-order submission
- Settlement instruction creation
- Cash movement
- Post-trade reporting
- Security lifecycle processing

---

## Related Artifacts

### Parent Feature

- [[FEATURE-E6-03-execute-and-allocate-issuance]]

### Acceptance Criteria

- [[AC-E6-303]]

### Business Rules

- [[BR-FEATURE-E6-03]]

---

## Notes

Allocation results must remain traceable to the accepted dealer orders and the executed issuance quantity.
