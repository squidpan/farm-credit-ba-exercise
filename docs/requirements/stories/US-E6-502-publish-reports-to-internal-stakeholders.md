---
id: US-E6-502
project: farm-credit-ba-exercise

type: story
status: draft

description: Enables an authorized operations analyst to publish approved post-trade reports to authorized internal stakeholders.

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

# US-E6-502 Publish Reports to Internal Stakeholders

## TL;DR

Publish an approved post-trade report to authorized internal recipients and preserve the distribution history.

## User Story

As a Post-Trade Operations Analyst,  
I want to publish approved post-trade reports to authorized internal stakeholders,  
so that operational, financial, compliance, and management users can review completed issuance activity.

## Business Value

This story ensures that validated reporting information reaches the appropriate internal users in a controlled and traceable manner.

It supports:

- Operational oversight
- Financial review
- Compliance monitoring
- Management reporting
- Controlled information access
- Distribution auditability

## Scope

This story includes:

- Selecting an approved report version
- Identifying authorized internal recipients
- Validating recipient access
- Publishing the report through an approved internal channel
- Recording the publication date, time, user, recipients, and report version
- Recording successful and failed publication outcomes
- Preventing unauthorized or outdated report publication
- Making the published report available to authorized recipients

This story excludes:

- Generating the report
- Delivering reports to regulators or external recipients
- Reconciling report contents
- Correcting reporting discrepancies
- Archiving the final report package
- Defining detailed technical delivery protocols

## Related Artifacts

### Feature

- [[FEATURE-E6-05-post-trade-reporting]]

### Acceptance Criteria

- [[AC-E6-502]]

### Business Rules

- [[BR-FEATURE-E6-05]]

### Previous Story

- [[US-E6-501-generate-post-trade-reports]]

### Next Story

- [[US-E6-503-deliver-compliance-and-regulatory-reports]]

## Notes

Detailed approval checks, recipient authorization, publication controls, failed-delivery handling, and distribution-history requirements are defined in [[AC-E6-502]] and [[BR-FEATURE-E6-05]].
