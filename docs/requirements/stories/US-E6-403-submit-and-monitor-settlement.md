---
id: US-E6-403
project: farm-credit-ba-exercise

type: story
status: draft

description: Enables a Settlement Operations Analyst to submit validated settlement instructions and monitor their processing status.

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

# US-E6-403 Submit and Monitor Settlement

## TL;DR

Submit validated settlement instructions to the appropriate settlement participants and monitor them through completion or exception.

---

## User Story

As a Settlement Operations Analyst,

I want to submit validated settlement instructions and monitor their status,

so that I can confirm that securities and cash are progressing toward settlement as expected.

---

## Business Value

Timely submission and monitoring reduce settlement risk by ensuring that instructions reach the appropriate fiscal agent, settlement system, payment system, and dealer participants and that delays or failures are identified promptly.

---

## Scope

### Included

- Retrieve settlement instructions marked ready for submission
- Submit instructions to the applicable settlement participant or system
- Record submission date and time
- Record submission status
- Receive acknowledgement or rejection responses
- Monitor settlement-processing status
- Record status changes
- Identify delayed, rejected, unmatched, or failed instructions
- Preserve submission and status history
- Route settlement exceptions for resolution

### Excluded

- Changing execution or allocation terms
- Creating settlement instructions
- Correcting settlement exceptions
- Recording final settlement completion
- Post-trade reporting
- Lifecycle servicing

---

## Related Artifacts

### Parent Feature

- [[FEATURE-E6-04-confirm-and-settle-issuance]]

### Upstream Story

- [[US-E6-402-create-settlement-instructions]]

### Downstream Stories

- [[US-E6-404-resolve-settlement-exceptions]]
- [[US-E6-405-record-settlement-completion]]

### Acceptance Criteria

- [[AC-E6-403]]

### Business Rules

- [[BR-FEATURE-E6-04]]

---

## Notes

A settlement instruction must not be submitted unless it has passed all required validation and is marked ready for submission.

Status changes should be traceable from initial submission through acknowledgement, processing, settlement, rejection, or failure.
