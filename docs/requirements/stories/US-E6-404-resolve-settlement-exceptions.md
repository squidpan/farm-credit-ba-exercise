---
id: US-E6-404
project: farm-credit-ba-exercise

type: story
status: draft

description: Enables a Settlement Operations Analyst to identify, investigate, and resolve settlement exceptions before settlement completion.

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

# US-E6-404 Resolve Settlement Exceptions

## TL;DR

Identify, investigate, track, and resolve settlement exceptions before the issuance can be marked as successfully settled.

---

## User Story

As a Settlement Operations Analyst,

I want to investigate and resolve settlement exceptions,

so that failed, delayed, rejected, or unmatched settlement instructions are corrected before settlement completion.

---

## Business Value

Controlled exception management minimizes operational and financial risk by ensuring that settlement problems are identified, investigated, documented, and resolved before the issuance is finalized.

---

## Scope

### Included

- Identify settlement exceptions
- Classify exception type
- Record exception details
- Investigate root cause
- Coordinate with settlement participants
- Correct operational data when authorized
- Resubmit corrected settlement instructions when required
- Track exception status
- Record resolution history
- Mark resolved exceptions ready for settlement completion

### Excluded

- Changing approved issuance terms
- Changing dealer allocations
- Creating settlement instructions
- Recording final settlement completion
- Regulatory reporting
- Lifecycle servicing

---

## Related Artifacts

### Parent Feature

- [[FEATURE-E6-04-confirm-and-settle-issuance]]

### Upstream Story

- [[US-E6-403-submit-and-monitor-settlement]]

### Downstream Story

- [[US-E6-405-record-settlement-completion]]

### Acceptance Criteria

- [[AC-E6-404]]

### Business Rules

- [[BR-FEATURE-E6-04]]

---

## Notes

Settlement completion cannot occur while unresolved settlement exceptions remain open.

All exception investigation, corrective actions, resubmissions, and final resolutions should be retained as part of the operational audit history.
