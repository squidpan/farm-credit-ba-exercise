---
id: BR-FEATURE-E6-05
project: farm-credit-ba-exercise

type: business-rule
status: approved

description: Defines the governing business rules for generating, distributing, reconciling, resolving, and archiving post-trade reporting records.

categories:
  - "[[Business Rules]]"
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

# BR-FEATURE-E6-05 Post-Trade Reporting Business Rules

## TL;DR

Post-trade reports must be generated from authoritative finalized records, validated before use, distributed only through approved channels, reconciled against source data, and preserved with complete audit history.

## Business Rules

### BR-E6-05-01 — Authoritative Source Records

Post-trade reports must be generated from authoritative finalized issuance, execution, allocation, confirmation, and settlement records.

### BR-E6-05-02 — Reporting Eligibility

Only settled activity or activity otherwise explicitly authorized for reporting may be included in a finalized post-trade report.

### BR-E6-05-03 — Approved Report Definitions

Every report must use an active and approved report definition that identifies required fields, mappings, calculations, totals, validation rules, and reporting population.

### BR-E6-05-04 — Report Completeness

A report may not be marked ready for review, approved, published, delivered, or archived when required report content is incomplete or invalid.

### BR-E6-05-05 — Report Versioning

Every generated or regenerated report must have a unique and traceable version identifier.

### BR-E6-05-06 — Version Preservation

A new report version must not overwrite or erase a prior version.

### BR-E6-05-07 — Approved Version Distribution

Only an approved report version may be published internally or delivered to an external compliance or regulatory recipient.

### BR-E6-05-08 — Superseded Report Control

A superseded report version must not be distributed unless an authorized exception is documented.

### BR-E6-05-09 — Recipient Authorization

Reports may be distributed only to recipients authorized to receive the applicable report type.

### BR-E6-05-10 — Approved Distribution Channels

Internal publication and external delivery must use approved channels appropriate to the report, recipient, and reporting obligation.

### BR-E6-05-11 — Report Integrity

Published, delivered, and archived report content must match the approved report version without unauthorized modification.

### BR-E6-05-12 — Submission Evidence

Acknowledgements, receipts, reference identifiers, rejections, and other delivery evidence must be associated with the applicable report version and delivery event.

### BR-E6-05-13 — Reporting Deadlines

Compliance and regulatory reports must be evaluated against the applicable reporting deadline, and late or at-risk submissions must be identifiable.

### BR-E6-05-14 — Reconciliation Requirement

Post-trade report data must be reconcilable against the authoritative source records used to generate the report.

### BR-E6-05-15 — Approved Matching Rules

Reconciliation must use approved field mappings, matching rules, calculations, and tolerances.

### BR-E6-05-16 — Discrepancy Identification

Missing records, unexpected records, mismatched values, and totals outside approved tolerances must be recorded as discrepancies.

### BR-E6-05-17 — False-Match Prevention

A report with unresolved discrepancies outside approved tolerances must not be classified as fully matched.

### BR-E6-05-18 — Discrepancy Ownership

Every unresolved discrepancy must have an authorized owner or responsible group.

### BR-E6-05-19 — Resolution Evidence

A discrepancy may not be approved as resolved without sufficient investigation notes, resolution details, and supporting evidence.

### BR-E6-05-20 — Segregated Resolution Approval

Discrepancy approval must be performed by an authorized decision-maker and must remain distinguishable from the investigation activity.

### BR-E6-05-21 — Premature Closure Prevention

A discrepancy may not be closed while required corrective actions or approvals remain incomplete.

### BR-E6-05-22 — History Preservation

Report generation, publication, delivery, reconciliation, discrepancy, regeneration, resubmission, and archival events must be appended without overwriting prior history.

### BR-E6-05-23 — Archival Eligibility

Only finalized reporting records with completed required reporting activities may be archived.

### BR-E6-05-24 — Open Discrepancy Restriction

Reporting records with unresolved discrepancies may not be archived unless an authorized exception is documented.

### BR-E6-05-25 — Archive Completeness

An archival package must include the applicable final report, generation metadata, publication and delivery history, submission evidence, reconciliation results, and discrepancy-resolution records.

### BR-E6-05-26 — Retention Classification

Archived reporting records must be assigned the approved retention classification and retention period.

### BR-E6-05-27 — Archive Protection

Archived records must be protected from unauthorized alteration, replacement, or deletion.

### BR-E6-05-28 — Legal and Regulatory Holds

An active legal, regulatory, audit, or investigative hold must override ordinary record-disposition eligibility.

### BR-E6-05-29 — Authorized Access

Access to reports, discrepancies, delivery evidence, reconciliation results, and archives must be limited to authorized users and processes.

### BR-E6-05-30 — Audit Traceability

Every material post-trade reporting action must record who or what performed the action, what records were affected, when it occurred, and what outcome resulted.

## Related Artifacts

### Feature

- [[FEATURE-E6-05-post-trade-reporting]]

### Stories

- [[US-E6-501-generate-post-trade-reports]]
- [[US-E6-502-publish-reports-to-internal-stakeholders]]
- [[US-E6-503-deliver-compliance-and-regulatory-reports]]
- [[US-E6-504-reconcile-post-trade-reporting-data]]
- [[US-E6-505-resolve-and-track-reporting-discrepancies]]
- [[US-E6-506-archive-post-trade-reporting-records]]

### Acceptance Criteria

- [[AC-E6-501]]
- [[AC-E6-502]]
- [[AC-E6-503]]
- [[AC-E6-504]]
- [[AC-E6-505]]
- [[AC-E6-506]]

### Previous Business Rules

- [[BR-FEATURE-E6-04]]

### Next Business Rules

- Planned future lifecycle Business Rules for FEATURE-E6-06; artifact not yet created.
