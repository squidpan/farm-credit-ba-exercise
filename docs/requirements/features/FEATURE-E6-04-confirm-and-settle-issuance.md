---
id: FEATURE-E6-04
project: farm-credit-ba-exercise

type: feature
status: draft

description: Enables an executed and allocated issuance to be confirmed, instructed, settled, and recorded as complete.

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

# FEATURE-E6-04 Confirm and Settle Issuance

## TL;DR

Confirm executed transactions, generate settlement instructions, complete settlement, record settlement outcomes, and resolve settlement exceptions.

---

## Business Objective

Provide a controlled and auditable settlement process that converts executed dealer allocations into completed delivery-versus-payment (DVP) settlement records.

---

## Business Value

Improves settlement accuracy, operational control, exception visibility, and auditability while supporting timely completion of securities and funds exchange.

---

## Business Context

Feature E6-03 completes execution and allocation of securities to dealers.

Feature E6-04 begins once execution has been finalized and the issuance is ready for settlement. The objective is to ensure both securities and funds are exchanged accurately, settlement instructions are communicated to the appropriate parties, exceptions are managed, and the issuance is recorded as successfully settled.

---

## Primary Actors

- Settlement Operations Analyst
- Issuance Officer
- Dealer Operations Representative
- Fiscal Agent
- Payment and Securities Settlement Systems

---

## Preconditions

- Issuance execution is complete.
- Dealer allocations are finalized.
- Settlement date has been established.
- Settlement accounts have been validated.
- Required approvals have been completed.

---

## Scope

### Included

- Confirm dealer settlement transactions
- Create settlement instructions
- Validate settlement readiness
- Submit settlement instructions
- Monitor settlement status
- Resolve settlement exceptions
- Record completed settlement
- Mark issuance as settled

### Excluded

- Issuance scheduling
- Dealer order capture
- Allocation processing
- Investor reporting
- Interest payments
- Maturity processing
- Secondary-market activity

---

## Business Rules

- [[BR-FEATURE-E6-04]]

## Stories

- US-E6-401 Confirm Dealer Transactions
- US-E6-402 Create Settlement Instructions
- US-E6-403 Submit and Monitor Settlement
- US-E6-404 Resolve Settlement Exceptions
- US-E6-405 Record Settlement Completion

---

## Business Outcomes

- Confirmed settlement transactions
- Valid settlement instructions
- Traceable settlement processing
- Controlled exception management
- Recorded settlement completion
- Complete audit trail

---

## Downstream Handoff

Successful completion provides settlement information to:

- Accounting
- Reconciliation
- Regulatory Reporting
- Investor Reporting
- Lifecycle Servicing

---

## Related Artifacts

### Parent Epic

- [[EPIC-E6-issue-and-settle-security]]

### Upstream Feature

- [[FEATURE-E6-03-execute-and-allocate-issuance]]

### Planned Stories

- [[US-E6-401-confirm-dealer-transactions]]
- [[US-E6-402-create-settlement-instructions]]
- [[US-E6-403-submit-and-monitor-settlement]]
- [[US-E6-404-resolve-settlement-exceptions]]
- [[US-E6-405-record-settlement-completion]]

### Planned Business Rule

- [[BR-FEATURE-E6-04]]

### Planned Review

- [[REVIEW-FEATURE-E6-04-requirements-walkthrough]]
