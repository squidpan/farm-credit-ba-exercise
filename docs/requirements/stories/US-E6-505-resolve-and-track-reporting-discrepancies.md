---
id: US-E6-505
project: farm-credit-ba-exercise

type: story
status: draft

description: Enables an authorized analyst to investigate, resolve, and track reporting discrepancies identified during post-trade reconciliation.

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
feature: FEATURE-E6-05
---

# US-E6-505 Resolve and Track Reporting Discrepancies

## TL;DR

Investigate reporting discrepancies, document their resolution, and preserve the complete resolution history.

## User Story

As a Reporting or Operations Analyst,  
I want to investigate and resolve post-trade reporting discrepancies,  
so that reports can be corrected, reconciled, and finalized with a complete audit trail.

## Business Value

This story supports:

- Accurate reporting
- Controlled discrepancy resolution
- Clear ownership and accountability
- Reduced unresolved exceptions
- Reliable report finalization
- Audit traceability

## Scope

This story includes:

- Reviewing unresolved reconciliation discrepancies
- Assigning ownership and status
- Recording investigation notes and supporting evidence
- Identifying the cause and required corrective action
- Recording whether the report, source record, or mapping requires correction
- Tracking resolution progress
- Recording approval or rejection of the proposed resolution
- Closing resolved discrepancies
- Preserving the complete discrepancy history

This story excludes:

- Directly modifying authoritative source records
- Generating replacement reports
- Publishing or delivering corrected reports
- Defining technical correction procedures
- Archiving the final reporting package
- Changing approved business rules or tolerances

## Related Artifacts

### Feature

- [[FEATURE-E6-05-post-trade-reporting]]

### Acceptance Criteria

- [[AC-E6-505]]

### Business Rules

- [[BR-FEATURE-E6-05]]

### Previous Story

- [[US-E6-504-reconcile-post-trade-reporting-data]]

### Next Story

- [[US-E6-506-archive-post-trade-reporting-records]]

## Notes

Detailed ownership, status transitions, evidence, approval, rejection, closure, reopening, and audit requirements are defined in [[AC-E6-505]] and [[BR-FEATURE-E6-05]].
