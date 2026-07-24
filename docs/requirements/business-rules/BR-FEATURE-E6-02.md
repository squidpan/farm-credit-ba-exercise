---
id: BR-FEATURE-E6-02
project: farm-credit-ba-exercise

type: business-rule
status: approved

description: Business rules governing issuance scheduling, validation, capacity reservation, identifier assignment, and booking.

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
feature: FEATURE-E6-02
---

# BR-FEATURE-E6-02 Schedule and Book Issuance

## TL;DR

These rules govern when a planned issuance may be scheduled, validated, assigned funding capacity, assigned a security identifier, and booked.

---

## Business Rules

### BR-E6-02.1 Required Scheduling Information

A planned issuance must contain the required scheduling information before it can be submitted for issuance-window validation.

Required information includes:

- Proposed issuance date
- Expected settlement date
- Security type
- Planned issuance amount
- Maturity information
- Responsible business area

---

### BR-E6-02.2 Authorized Issuance Window

A planned issuance may proceed only when its proposed issuance date falls on an authorized funding day and complies with applicable calendar and operational constraints.

---

### BR-E6-02.3 Conflict Prevention

The system must identify and prevent issuance schedules that conflict with established operational constraints or incompatible planned issuance activities.

---

### BR-E6-02.4 Validation Before Capacity Reservation

Funding capacity may not be reserved until the proposed issuance window has passed all required validations.

---

### BR-E6-02.5 Capacity Availability

Funding capacity may be reserved only when sufficient capacity is available for the planned issuance amount.

---

### BR-E6-02.6 Capacity Reservation Record

Each successful funding-capacity reservation must be associated with the planned issuance and recorded with sufficient information to support traceability.

---

### BR-E6-02.7 Identifier Uniqueness

Each planned security must have a unique security identifier before it can be booked.

A security identifier already associated with another security must not be reused.

---

### BR-E6-02.8 Booking Prerequisites

A planned issuance may be booked only when:

- The issuance schedule is complete
- The issuance window has been validated
- Funding capacity has been reserved
- A unique security identifier has been assigned

---

### BR-E6-02.9 Authoritative Booking Record

Successful booking must create the authoritative planned issuance record for downstream execution, allocation, settlement, reporting, and lifecycle processing.

---

### BR-E6-02.10 Booking Audit Information

The booking record must include:

- Booking date and time
- User or process completing the booking
- Booked status
- Associated security identifier
- Associated funding-capacity reservation

---

### BR-E6-02.11 Rejected Actions

When validation, reservation, identifier assignment, or booking is rejected, the system must record the reason for rejection.

---

## Related Artifacts

### Parent Feature

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

---

## Notes
