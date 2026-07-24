---
id: US-E6-405
project: farm-credit-ba-exercise

type: story
status: draft

description: Enables a Settlement Operations Analyst to verify and record final cash and securities settlement for an issuance.

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

# US-E6-405 Record Settlement Completion

## TL;DR

Verify that all required securities and cash movements are complete and record the issuance as settled.

---

## User Story

As a Settlement Operations Analyst,

I want to record settlement completion for the issuance,

so that the organization has an accurate and auditable record of completed cash and securities movement.

---

## Business Value

Recording settlement completion provides authoritative evidence that all required dealer transactions have settled, unresolved exceptions have been cleared, and the issuance is ready for downstream accounting, reconciliation, reporting, and lifecycle servicing.

---

## Scope

### Included

- Retrieve final settlement statuses
- Verify completion of required securities movement
- Verify completion of required cash movement
- Confirm all dealer transactions are settled
- Confirm no blocking settlement exceptions remain
- Record settlement date and time
- Record final settled quantities and amounts
- Record the settlement-completion status
- Preserve settlement evidence and history
- Mark the issuance as settled
- Hand off settled issuance information to downstream processes

### Excluded

- Changing execution terms
- Changing dealer allocations
- Creating or submitting settlement instructions
- Resolving open settlement exceptions
- Performing accounting reconciliation
- Producing post-trade reports
- Processing lifecycle events

---

## Related Artifacts

### Parent Feature

- [[FEATURE-E6-04-confirm-and-settle-issuance]]

### Upstream Stories

- [[US-E6-403-submit-and-monitor-settlement]]
- [[US-E6-404-resolve-settlement-exceptions]]

### Downstream Feature

- [[FEATURE-E6-05-post-trade-reporting]]

### Acceptance Criteria

- [[AC-E6-405]]

### Business Rules

- [[BR-FEATURE-E6-04]]

---

## Notes

The issuance must not be marked settled until all required dealer transactions have completed cash and securities settlement and no blocking exceptions remain unresolved.

The final settlement record should preserve the settled quantities, amounts, dates, statuses, supporting evidence, user, and timestamp.
