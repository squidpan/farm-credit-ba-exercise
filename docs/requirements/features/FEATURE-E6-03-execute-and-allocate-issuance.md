---
id: FEATURE-E6-03
project: farm-credit-ba-exercise

type: feature
status: draft

description: Execute a booked issuance, receive dealer orders, allocate securities, and prepare execution results for settlement.

categories:
  - "[[Features]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"
tags:
  - farm-credit
  - requirements

created: 2026-07-23
updated: 2026-07-23

epic: EPIC-E6
---

# FEATURE-E6-03 Execute and Allocate Issuance

## TL;DR

Execute a booked debt issuance, collect dealer participation, allocate securities, and produce the execution record used by settlement.

---

## Feature Description

After a planned issuance has been booked, the issuance is executed in the market. Dealer orders are received, evaluated, and allocated. The resulting execution information becomes the authoritative input for settlement and post-trade processing.

---

## Business Objective

Execute an approved issuance while ensuring accurate allocation, traceability, and operational control.

---

## Business Value

- Records executed issuance activity
- Supports fair and auditable allocation
- Produces authoritative execution results
- Supplies downstream settlement processing

---

## Primary Actors

- Issuance Officer
- Funding Operations Analyst
- Dealer
- Settlement Operations Analyst

---

## Preconditions

- Planned issuance has been booked
- Security identifier exists
- Funding capacity has been reserved

---

## Trigger

A booked planned issuance is ready for market execution.

---

## Scope

### Included

- Execute issuance
- Receive dealer participation
- Allocate securities
- Record execution results
- Prepare settlement input

### Excluded

- Issuance planning
- Booking
- Settlement
- Post-trade reporting
- Security lifecycle events

---

## Functional Flow

1. Execute issuance.
2. Receive dealer participation.
3. Allocate securities.
4. Record execution results.
5. Deliver execution information to settlement.

---

## Business Rules

- [[BR-FEATURE-E6-03]]

---

## Stories

- [[US-E6-301-execute-issuance]]
- [[US-E6-302-receive-dealer-orders]]
- [[US-E6-303-allocate-securities]]
- [[US-E6-304-record-execution-results]]

---

## Review

- [[REVIEW-FEATURE-E6-03-requirements-walkthrough]]

---

## Related Artifacts

- [[EPIC-E6-issue-and-settle-security]]
- [[FEATURE-E6-02-schedule-and-book-issuance]]
- [[REVIEW-FEATURE-E6-03-requirements-walkthrough]]

## Notes
