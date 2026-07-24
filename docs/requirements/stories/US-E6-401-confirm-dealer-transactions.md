---
id: US-E6-401
project: farm-credit-ba-exercise

type: story
status: draft

description: Enables a Settlement Operations Analyst to confirm final dealer transaction details before settlement instructions are created.

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
feature: FEATURE-E6-04
---

# US-E6-401 Confirm Dealer Transactions

## TL;DR

Confirm that finalized dealer transactions contain complete and accurate information before settlement instructions are created.

---

## User Story

As a Settlement Operations Analyst,

I want to confirm the final details of each dealer transaction,

so that settlement instructions are based on accurate execution and allocation information.

---

## Business Value

Confirming dealer transactions reduces settlement risk by ensuring that dealer identities, security details, quantities, prices, amounts, dates, and settlement-party information agree with the finalized execution record.

---

## Scope

### Included

- Retrieve finalized dealer allocations
- Confirm dealer and settlement-party information
- Confirm the security identifier
- Confirm trade and settlement dates
- Confirm allocated quantities
- Confirm execution prices
- Confirm principal and settlement amounts
- Identify missing or inconsistent information
- Record transaction-confirmation status
- Preserve confirmation history

### Excluded

- Changing approved issuance terms
- Reallocating securities
- Creating settlement instructions
- Submitting settlement instructions
- Completing settlement
- Post-trade reporting

---

## Related Artifacts

### Parent Feature

- [[FEATURE-E6-04-confirm-and-settle-issuance]]

### Upstream Story

- [[US-E6-304-record-execution-results]]

### Downstream Story

- [[US-E6-402-create-settlement-instructions]]

### Acceptance Criteria

- [[AC-E6-401]]

### Business Rules

- [[BR-FEATURE-E6-04]]

---

## Notes

A dealer transaction cannot proceed to settlement-instruction creation until all required transaction and settlement-party information has been confirmed.
