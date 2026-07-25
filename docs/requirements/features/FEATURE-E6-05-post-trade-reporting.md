---
id: FEATURE-E6-05
project: farm-credit-ba-exercise

type: feature
status: draft

description: Defines the post-trade reporting, reconciliation, distribution, and archival activities performed after issuance settlement is completed.

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

# FEATURE-E6-05 Post-Trade Reporting

## TL;DR

Enable authorized business and operations users to generate, validate, distribute, reconcile, and retain post-trade reports after an issuance has settled.

## Business Objective

Provide complete and traceable reporting of issuance, allocation, confirmation, and settlement activity so that internal stakeholders, control functions, and external recipients receive accurate and timely post-trade information.

## Business Value

Supports accurate operational oversight, financial control, compliance, management reporting, and audit review by providing timely and traceable post-trade information.

## Business Context

After an issuance has been executed, allocated, confirmed, and settled, the resulting transaction information must be transformed into reports suitable for operational oversight, financial control, compliance, management reporting, and audit review.

Post-trade reporting depends on finalized information produced by the preceding issuance lifecycle stages. The reporting process must preserve the relationship between the original debt transaction, execution results, allocations, settlement records, reporting outputs, delivery events, reconciliation outcomes, and retained report versions.

## Primary Actors

- Settlement Operations Analyst
- Post-Trade Operations Analyst
- Reporting Analyst
- Risk and Compliance Officer
- Finance or Accounting Analyst
- Treasury Management
- Audit or Control Reviewer
- Authorized External Reporting Recipient

## Trigger

Settlement completion is recorded for an issuance or an authorized reporting cycle begins.

## Preconditions

- The debt transaction has been approved.
- The issuance has been scheduled and booked.
- Execution and allocation information is available.
- Settlement completion has been recorded.
- Required reporting data is available from authoritative sources.
- Reporting rules and recipient requirements are defined.
- The user is authorized to perform the requested reporting activity.

## Scope

This feature includes:

- Collecting finalized issuance and settlement information
- Generating post-trade reports
- Validating report completeness and accuracy
- Publishing reports to authorized internal stakeholders
- Preparing and delivering required compliance or regulatory reports
- Reconciling report contents with authoritative settlement records
- Identifying and resolving reporting discrepancies
- Recording report generation and delivery history
- Archiving approved report versions
- Preserving audit traceability

## Out of Scope

This feature does not include:

- Proposing or approving debt transactions
- Scheduling or booking issuance
- Executing or allocating securities
- Confirming dealer transactions
- Creating or submitting settlement instructions
- Resolving settlement failures before settlement completion
- Servicing interest, maturity, redemption, or other lifecycle events
- Defining detailed accounting ledger-posting logic
- Defining recipient-specific technical transport protocols
- Defining records-retention periods not yet approved by policy

## Functional Flow

1. Identify settled issuance activity eligible for reporting.
2. Collect finalized transaction, allocation, confirmation, and settlement information.
3. Generate the required post-trade report.
4. Validate the report for completeness, accuracy, and consistency.
5. Publish or deliver the report to authorized recipients.
6. Reconcile reported information with authoritative settlement records.
7. Record and resolve any reporting discrepancies.
8. Approve the final report version.
9. Archive the report and preserve generation, delivery, and reconciliation history.
10. Make approved reporting information available for downstream use.

## Business Rules

- [[BR-FEATURE-E6-05]]

## Stories

### US-E6-501 Generate Post-Trade Reports

As a Reporting Analyst, I want to generate post-trade reports from finalized issuance and settlement information so that stakeholders receive an accurate record of completed activity.

### US-E6-502 Publish Reports to Internal Stakeholders

As a Post-Trade Operations Analyst, I want to publish approved reports to authorized internal stakeholders so that operational, financial, and management users can review completed issuance activity.

### US-E6-503 Deliver Compliance and Regulatory Reports

As a Risk and Compliance Officer, I want required post-trade reports delivered to approved recipients so that reporting obligations are completed accurately and on time.

### US-E6-504 Reconcile Reported Activity

As a Finance or Operations Analyst, I want to reconcile reported activity with authoritative settlement records so that discrepancies are identified and resolved.

### US-E6-505 Archive Reports and Audit History

As an Audit or Control Reviewer, I want approved report versions and their processing history retained so that reporting activity remains traceable and reviewable.

## Business Outcomes

Successful completion of this feature provides:

- Accurate post-trade reporting
- Timely distribution of completed issuance information
- Evidence that reporting obligations were fulfilled
- Reconciliation between reports and settlement records
- Controlled correction of reporting discrepancies
- Retained report versions and delivery history
- Complete audit traceability
- Reliable downstream reporting information

## Controls

The feature must ensure that:

- Only settled or otherwise authorized activity is included in final reporting.
- Report data is sourced from authoritative records.
- Required report fields are present before publication.
- Report totals and transaction details are validated.
- Unauthorized users cannot generate, approve, publish, or modify reports.
- Report corrections create a new traceable version.
- Delivery attempts and outcomes are recorded.
- Reconciliation results and unresolved discrepancies are preserved.
- Approved reports cannot be silently overwritten.
- Archived reports remain associated with the underlying issuance and settlement records.

## Assumptions

- Settlement completion is the primary trigger for final post-trade reporting.
- Some reports may be generated on demand, while others may follow a scheduled reporting cycle.
- Internal, compliance, regulatory, and management reports may use different formats and recipient rules.
- Detailed technical interfaces will be defined during implementation analysis.
- Records-retention requirements will be governed by approved policy.
- Accounting and ledger-specific reconciliation may require additional requirements outside this feature.

## Dependencies

### Upstream

- [[FEATURE-E6-01-propose-and-approve-debt-transaction]]
- [[FEATURE-E6-02-schedule-and-book-issuance]]
- [[FEATURE-E6-03-execute-and-allocate-issuance]]
- [[FEATURE-E6-04-confirm-and-settle-issuance]]

### Downstream

- Planned future capability: FEATURE-E6-06 — Manage Security Lifecycle Events (artifact not yet created)

## Related Artifacts

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

### Business Rules

- [[BR-FEATURE-E6-05]]

### Requirements Review

- [[REVIEW-FEATURE-E6-05]]
