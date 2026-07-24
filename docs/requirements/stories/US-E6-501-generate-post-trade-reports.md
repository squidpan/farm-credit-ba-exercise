---
id: US-E6-501
project: farm-credit-ba-exercise

type: story
status: draft

description: Enables an authorized reporting analyst to generate a validated post-trade report from finalized issuance and settlement information.

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

# US-E6-501 Generate Post-Trade Reports

## TL;DR

Generate a validated and traceable post-trade report for settled issuance activity.

## User Story

As a Reporting Analyst,  
I want to generate a post-trade report from finalized issuance and settlement information,  
so that authorized stakeholders receive an accurate record of completed issuance activity.

## Business Value

This story provides the initial reporting output required after settlement and supports:

- Operational oversight
- Management and compliance reporting
- Reconciliation
- Audit traceability
- Downstream reporting processes

## Scope

This story includes:

- Selecting settled issuance activity eligible for reporting
- Selecting an approved report type
- Retrieving authoritative transaction and settlement information
- Applying required mappings, calculations, and totals
- Validating required report content
- Creating a uniquely versioned report
- Recording report-generation metadata
- Associating the report with its source records
- Making the report available for authorized review

This story excludes:

- Publishing reports to recipients
- Regulatory or compliance delivery
- Reconciliation and discrepancy resolution
- Final report approval
- Report archival

## Related Artifacts

### Feature

- [[FEATURE-E6-05-post-trade-reporting]]

### Acceptance Criteria

- [[AC-E6-501]]

### Business Rules

- [[BR-FEATURE-E6-05]]

### Previous Story

- [[US-E6-405-record-settlement-completion]]

### Next Story

- [[US-E6-502-publish-reports-to-internal-stakeholders]]

## Notes

Detailed eligibility checks, validation failures, duplicate prevention, version control, and audit requirements are defined in [[AC-E6-501]] and [[BR-FEATURE-E6-05]].
