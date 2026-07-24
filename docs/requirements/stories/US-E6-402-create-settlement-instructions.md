---
id: US-E6-402
project: farm-credit-ba-exercise

type: story
status: draft

description: Enables a Settlement Operations Analyst to create validated settlement instructions for confirmed dealer transactions.

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

# US-E6-402 Create Settlement Instructions

## TL;DR

Create complete and validated settlement instructions for each confirmed dealer transaction.

---

## User Story

As a Settlement Operations Analyst,

I want to create settlement instructions for confirmed dealer transactions,

so that securities and funds can be exchanged accurately on the settlement date.

---

## Business Value

Accurate settlement instructions translate confirmed execution and allocation results into actionable directions for the fiscal agent, settlement systems, dealers, and payment participants.

---

## Scope

### Included

- Retrieve confirmed dealer transactions
- Create settlement instructions
- Identify delivering and receiving parties
- Identify securities and cash accounts
- Record security identifier
- Record settlement date
- Record settlement quantity
- Record settlement amount
- Record settlement currency and method
- Validate required instruction information
- Assign a settlement-instruction identifier
- Mark valid instructions ready for submission

### Excluded

- Changing execution terms
- Changing dealer allocations
- Submitting settlement instructions
- Monitoring settlement
- Resolving settlement exceptions
- Recording final settlement completion
- Post-trade reporting

---

## Related Artifacts

### Parent Feature

- [[FEATURE-E6-04-confirm-and-settle-issuance]]

### Acceptance Criteria

- [[AC-E6-402]]

### Business Rules

- [[BR-FEATURE-E6-04]]

---

## Notes

A settlement instruction should not be marked ready for submission until all required party, account, security, quantity, date, amount, currency, and settlement-method information has been validated.
