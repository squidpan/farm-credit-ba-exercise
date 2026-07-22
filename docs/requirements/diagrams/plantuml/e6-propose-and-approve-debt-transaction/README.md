---
id: INDEX-E6-APPROVED-DIAGRAMS
project: farm-credit-ba-exercise
type: index
status: approved

categories:
  - "[[Indexes]]"
  - "[[Diagrams]]"
  - "[[Requirements]]"

tags:
  - farm-credit
  - debt-issuance
  - plantuml
  - interview-study

description: Index of the approved E6 and E6-01 PlantUML diagrams and companion explanation guides.
created: 2026-07-21
updated: 2026-07-22
---

# E6 Approved Diagram Set

## Objective

Document Epic E6 — Issue and Settle Security, with current focus on Feature E6-01 — Propose and Approve Debt Transaction.

Each diagram answers one specific business question. The set is intentionally layered rather than repetitive.

## Approved Diagram Inventory

| ID | Diagram | Layer | Source | Guide |
|---|---|---|---|---|
| E6-00 | 500-Foot Business View | L0 Executive Overview | [[E6-00-issue-and-settle-security-500-foot-business-view]] | [[E6-00-issue-and-settle-security-500-foot-business-view]] |
| E6-01A | Business Activity View | L1 Business Workflow | [[E6-01A-propose-and-approve-debt-transaction-business-activity-view]] | [[E6-01A-propose-and-approve-debt-transaction-business-activity-view]] |
| E6-01B | Actor and Decision View | L2 Responsibilities | [[E6-01B-propose-and-approve-debt-transaction-actor-and-decision-view]] | [[E6-01B-propose-and-approve-debt-transaction-actor-and-decision-view]] |
| E6-01C | Successful Approval Sequence | L8 Sequence | [[E6-01C-propose-and-approve-debt-transaction-successful-approval-sequence]] | [[E6-01C-propose-and-approve-debt-transaction-successful-approval-sequence]] |
| E6-01D1 | Return, Correct and Resubmit Sequence | L8 Sequence | [[E6-01D1-propose-and-approve-debt-transaction-return-correct-and-resubmit-sequence]] | [[E6-01D1-propose-and-approve-debt-transaction-return-correct-and-resubmit-sequence]] |
| E6-01D2 | Business Decision Flow | L3 Business Decisions | [[E6-01D2-propose-and-approve-debt-transaction-business-decision-flow]] | [[E6-01D2-propose-and-approve-debt-transaction-business-decision-flow]] |
| E6-01E | Transaction Information Evolution | L4 Information Evolution | [[E6-01E-propose-and-approve-debt-transaction-information-evolution]] | [[E6-01E-propose-and-approve-debt-transaction-information-evolution]] |
| E6-01F-v1 | Business Control Map — Detailed | L5 Business Controls | [[E6-01F-v1-propose-and-approve-debt-transaction-business-control-map-detailed]] | [[E6-01F-v1-propose-and-approve-debt-transaction-business-control-map-detailed]] |
| E6-01F-v2 | Business Control Map — Compact | L5 Business Controls | [[E6-01F-v2-propose-and-approve-debt-transaction-business-control-map-compact]] | [[E6-01F-v2-propose-and-approve-debt-transaction-business-control-map-compact]] |

## Visual Decomposition Standard

1. L0 Executive Overview
2. L1 Business Workflow
3. L2 Responsibilities
4. L3 Business Decisions
5. L4 Information Evolution
6. L5 Business Controls
7. L6 Business Rules
8. L7 State Lifecycle
9. L8 Sequence
10. Stories
11. Acceptance Criteria
12. UAT

## Packaging Decisions

- The more-spaced E6-01B source was selected as the canonical approved Actor and Decision View.
- Both E6-01F control maps are retained as approved complementary versions.
- Filenames were normalized for stable sorting, searchability, and future overlay into a Career System-style repository.
