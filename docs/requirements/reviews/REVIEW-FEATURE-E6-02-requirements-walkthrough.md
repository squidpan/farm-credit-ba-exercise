---
id: REVIEW-FEATURE-E6-02
project: farm-credit-ba-exercise

type: review
status: approved

description: Requirements walkthrough checklist for FEATURE-E6-02 Schedule and Book Issuance.

categories:
  - "[[Reviews]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"
tags:
  - farm-credit
  - requirements

created: 2026-07-23
updated: 2026-07-23

epic: EPIC-E6
feature: FEATURE-E6-02
---

# REVIEW-FEATURE-E6-02 Requirements Walkthrough

## TL;DR

Walk through the complete FEATURE-E6-02 requirements package and confirm that the feature, stories, acceptance criteria, and business rules are complete, consistent, and ready for stakeholder review.

---

## Purpose

Confirm that the requirements for scheduling and booking an issuance:

- Support the intended business workflow
- Contain complete story coverage
- Define testable acceptance criteria
- Apply consistent business rules
- Provide clear traceability between artifacts
- Identify unresolved questions before approval

---

## Scope Reviewed

### Feature

- [[FEATURE-E6-02-schedule-and-book-issuance]]

### Stories

- [[US-E6-201-schedule-issuance]]
- [[US-E6-202-validate-issuance-window]]
- [[US-E6-203-reserve-funding-capacity]]
- [[US-E6-204-assign-security-identifier]]
- [[US-E6-205-book-planned-issuance]]

### Acceptance Criteria

- [[AC-E6-201]]
- [[AC-E6-202]]
- [[AC-E6-203]]
- [[AC-E6-204]]
- [[AC-E6-205]]

### Business Rules

- [[BR-FEATURE-E6-02]]

---

## Walkthrough Agenda

### 1. Feature Scope

Confirm that the feature covers:

- Scheduling a proposed issuance
- Validating the issuance window
- Reserving funding capacity
- Assigning a unique security identifier
- Booking the planned issuance

Confirm that the feature does not include:

- Market execution
- Investor allocation
- Trade confirmation
- Settlement
- Post-trade reporting
- Security lifecycle processing

---

### 2. Story Review

### US-E6-201 Schedule Issuance

Confirm that:

- Required scheduling details are defined
- The planned issuance can be created in a preliminary state
- The story does not prematurely reserve capacity or book the issuance

### US-E6-202 Validate Issuance Window

Confirm that:

- Authorized funding days are validated
- Holiday and operational constraints are considered
- Conflicting issuance activity is detected
- Failed validation prevents downstream processing

### US-E6-203 Reserve Funding Capacity

Confirm that:

- Capacity is checked before reservation
- Insufficient capacity results in rejection
- Successful reservations are recorded
- Reservation occurs only after schedule validation

### US-E6-204 Assign Security Identifier

Confirm that:

- The identifier is unique
- Duplicate identifiers are rejected
- Assignment is recorded
- Identifier assignment occurs before booking

### US-E6-205 Book Planned Issuance

Confirm that:

- All prerequisites are checked
- Booking creates the authoritative planned issuance record
- Booking audit details are recorded
- The booked record is available to downstream processes

---

## Acceptance Criteria Review

Confirm that every acceptance criterion:

- Uses Given, When, Then structure
- Describes an observable outcome
- Covers both successful and unsuccessful conditions where applicable
- Can be converted into a test case
- Is traceable to one story
- Does not introduce scope outside FEATURE-E6-02

---

## Business Rules Review

Confirm that the business rules address:

- Required scheduling information
- Authorized issuance dates
- Conflict prevention
- Validation before capacity reservation
- Capacity availability
- Reservation traceability
- Identifier uniqueness
- Booking prerequisites
- Authoritative booking records
- Booking audit information
- Rejected action reasons

---

## Traceability Review

Confirm the following links are complete:

- Feature to all five stories
- Each story to its acceptance criteria
- Each story to the feature business rules
- Business rules to all stories
- Business rules to all acceptance criteria
- Review artifact to the complete feature package

---

## Review Questions

- Are all required issuance scheduling fields identified?
- What calendars define an authorized funding day?
- What conditions constitute an operational scheduling conflict?
- How is available funding capacity calculated?
- Can a capacity reservation expire or be released?
- Who or what system assigns the security identifier?
- Which identifier types are required?
- Can a booked issuance be amended or cancelled?
- Which downstream systems consume the booked issuance?
- What audit and retention requirements apply?

---

## Review Outcomes

### Approved

The requirements package is complete and may proceed to design, implementation planning, and test preparation.

### Approved with Changes

The requirements package may proceed after the documented changes are completed.

### Rework Required

The requirements package requires material revision and another walkthrough.

---

## Review Record

| Field | Value |
|---|---|
| Review Date | |
| Facilitator | |
| Business Reviewers | |
| Technology Reviewers | |
| Operations Reviewers | |
| Outcome | |
| Follow-up Date | |

---

## Findings

| ID | Artifact | Finding | Owner | Status |
|---|---|---|---|---|
| | | | | |

---

## Decisions

| ID | Decision | Decision Owner | Date |
|---|---|---|---|
| | | | |

---

## Follow-up Actions

| ID | Action | Owner | Due Date | Status |
|---|---|---|---|---|
| | | | | |

---

## Related Artifacts

- [[FEATURE-E6-02-schedule-and-book-issuance]]
- [[BR-FEATURE-E6-02]]
