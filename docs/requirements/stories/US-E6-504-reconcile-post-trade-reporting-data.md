---
id: US-E6-504
project: farm-credit-ba-exercise

type: story
status: draft

description: Enables a reporting or operations analyst to reconcile post-trade report data against authoritative transaction and settlement records.

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

# US-E6-504 Reconcile Post-Trade Reporting Data

## TL;DR

Compare post-trade report data with authoritative source records and identify discrepancies requiring resolution.

## User Story

As a Reporting or Operations Analyst,  
I want to reconcile post-trade report data against finalized transaction and settlement records,  
so that reporting discrepancies are identified before reports are finalized or relied upon.

## Business Value

This story supports:

- Reporting accuracy
- Early discrepancy detection
- Operational control
- Reliable management and compliance reporting
- Reduced downstream corrections
- Audit traceability

## Scope

This story includes:

- Selecting a report version for reconciliation
- Retrieving the report data and authoritative source records
- Comparing required fields, totals, and transaction populations
- Identifying missing, mismatched, or unexpected values
- Classifying reconciliation outcomes
- Recording discrepancies and supporting details
- Associating discrepancies with the affected report and source records
- Making reconciliation results available to authorized users

This story excludes:

- Correcting source-system records
- Editing approved reports directly
- Approving discrepancy resolutions
- Delivering or publishing reports
- Defining technical reconciliation algorithms
- Archiving completed reporting packages

## Related Artifacts

### Feature

- [[FEATURE-E6-05-post-trade-reporting]]

### Acceptance Criteria

- [[AC-E6-504]]

### Business Rules

- [[BR-FEATURE-E6-05]]

### Previous Story

- [[US-E6-503-deliver-compliance-and-regulatory-reports]]

### Next Story

- [[US-E6-505-resolve-and-track-reporting-discrepancies]]

## Notes

Detailed matching rules, tolerance handling, discrepancy classification, reconciliation status, and audit requirements are defined in [[AC-E6-504]] and [[BR-FEATURE-E6-05]].
