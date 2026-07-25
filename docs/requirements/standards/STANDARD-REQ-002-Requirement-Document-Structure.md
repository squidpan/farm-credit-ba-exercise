---
id: STANDARD-REQ-002
project: farm-credit-ba-exercise
type: standard
status: draft
description: Defines the standard document structure, section purpose, ordering, and authoring guidance for requirement artifacts.
categories:
  - "[[Standards]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"
tags:
  - requirements
  - documentation
  - standards
created: 2026-07-23
updated: 2026-07-24
---

# STANDARD-REQ-002 — Requirement Document Structure Standard

## TL;DR

Defines a practical, reusable structure for requirement documents that supports manual Business Analyst authoring, human review, traceability, repository validation, and future automation.

## Purpose

Define a consistent document structure for requirement artifacts while preserving enough flexibility for a Business Analyst to add useful context and examples.

This standard complements **STANDARD-REQ-001** by defining the organization and intent of the document body after YAML metadata.

## Scope

This standard applies to Epic, Feature, Story, Acceptance Criteria, Business Rule, and Review artifacts.

It governs heading hierarchy, canonical section ordering, required and optional sections, section intent, writing conventions, examples, cross-references, and document consistency.

## How to Use This Standard

This standard is an authoring aid and consistency framework.

Canonical structures define the semantic core expected for each artifact type. They provide a dependable starting point, not a maximum document definition.

A Business Analyst should use professional judgment when adding sections that improve clarity, traceability, analysis, review, or stakeholder communication.

Repository tooling should automate stable and objectively testable portions of this standard. It should not turn optional authoring guidance or useful extensions into unnecessary validation failures.

## Guiding Principles

- Every artifact should have a recognizable structure.
- Required sections should appear in a consistent order.
- Similar artifact types should look similar.
- Documents should be optimized for human readers while remaining suitable for automation.
- The document should communicate purpose before detail.
- Standards should help a Business Analyst author good requirements manually rather than impose unnecessary formatting complexity.
- Optional sections are encouraged when they add meaningful business context.
- Traceability should be explicit and understandable to a human reader.

## Artifact Summary and Intent

Metadata and document sections may describe related concepts, but they serve different purposes and should not simply repeat one another.

### YAML Description

The YAML `description` property is a concise metadata-level description of the artifact.

It answers: **What is this artifact?**

It is primarily useful for catalogs, indexes, search, automation, and repository navigation. It should normally be one sentence and remain useful when viewed without the document body.

Example:

`description: Defines the acceptance criteria for proposing a new debt transaction.`

### TL;DR

`TL;DR` is a short reader-oriented summary.

It answers: **What do I need to understand about this artifact quickly?**

Unlike YAML `description`, TL;DR is part of the human-readable document and may summarize the requirement, important behavior, or expected outcome in one or two sentences.

Example:

An authorized Issuance Officer can create a debt transaction proposal as a Draft so that it can be validated before submission for approval.

### Purpose

`Purpose` explains why an artifact or activity exists.

It answers: **Why do we need this artifact or activity?**

Purpose is useful where the reason for creating the artifact is distinct from its Business Objective or Business Value. It should not be added mechanically when it merely repeats other sections.

Purpose is required for Review artifacts, where the reason for conducting the review is distinct from the review outcome. For Epics, Features, Stories, Acceptance Criteria, and Business Rules, Purpose is optional when it adds meaningful context.

Example:

Evaluate a Feature for completeness, consistency, traceability, and testability before implementation.


### Business Objective

`Business Objective` describes the business outcome that an Epic or Feature intends to achieve.

It answers: **What business outcome are we trying to accomplish?**

The level of abstraction differs by artifact type:

- An Epic Business Objective describes the broader outcome spanning multiple capabilities.
- A Feature Business Objective describes the specific capability outcome that contributes to the Epic.

Epic example:

Enable customers to maintain accurate contact information through controlled self-service capabilities.

Feature example:

Enable authenticated customers to update their mailing address without requiring customer-service assistance.


### Business Value

`Business Value` explains why achieving an objective or delivering a requirement is worthwhile.

It answers: **What benefit does the business, user, or organization receive?**

Business Value is required for Epics, Features, and Stories, expressed at the appropriate level of abstraction.

Example:

Reduces manual service requests, improves customer data quality, and decreases the risk of correspondence being sent to an outdated address.


### Relationship Between These Elements

| Element | Primary Question | Primary Audience / Use |
|---|---|---|
| YAML `description` | What is this artifact? | Repository, search, automation |
| TL;DR | What should I understand quickly? | Human reader |
| Purpose | Why does this artifact/activity exist? | Context where needed |
| Business Objective | What outcome are we trying to achieve? | Epic and Feature direction |
| Business Value | Why is this capability worthwhile? | Business and delivery stakeholders |

Some conceptual overlap is expected, but identical wording should not be copied mechanically between these elements.

## General Heading Rules

### Heading Levels

Use ATX headings.

- `#` for the document title
- `##` for primary sections
- `###` for subsections

Avoid skipping heading levels. Each document contains exactly one H1.

### Document Title

The H1 should contain the artifact identifier and may contain a concise human-readable title.

Examples:

- `# US-E6-101 — Propose New Debt Transaction`
- `# FEATURE-E6-01 — Propose and Approve Debt Transaction`
- `# AC-E6-101 — Propose New Debt Transaction`
- `# BR-FEATURE-E6-01 — Business Rules for FEATURE-E6-01`

### Section Ordering

Required sections appear in the canonical order defined for the artifact type.

Optional sections should be placed where they best support comprehension without disrupting the logical flow.

## Canonical Structures

### Required and Optional Sections

**Required sections** establish the minimum recognizable structure for an artifact type and are candidates for repository validation.

**Optional sections** may be added when they improve understanding. Optional does not mean discouraged.

**Extensions** are additional analyst-authored sections appropriate to the requirement, such as actors, workflow flows, dependencies, data considerations, assumptions, or open questions.

A Business Analyst should use professional judgment. Additional sections are permitted when they provide meaningful business context and do not duplicate existing sections unnecessarily.

### Epic

Required sections:

1. TL;DR
2. Business Objective
3. Business Value
4. Scope
5. Success Criteria
6. Features
7. Related Artifacts

Optional or extension sections may include:

- Purpose
- Business Problem
- Out of Scope
- Key Actors
- Assumptions
- Dependencies
- Related Diagrams
- Notes

The Epic defines the broader business outcome and the major capabilities required to achieve it.

#### Epic Example

`# EPIC-CUST-01 — Maintain Customer Contact Information`

`## TL;DR`

Provide controlled self-service capabilities that allow customers to keep contact information accurate.

`## Business Objective`

Enable customers to maintain current contact information through secure, auditable digital workflows.

`## Business Value`

Improves customer-data quality, reduces manual service requests, and lowers the risk of communications being sent to obsolete contact information.

`## Scope`

Includes self-service maintenance of supported customer contact information.

`## Success Criteria`

Customers can successfully maintain supported contact information while required validation, authorization, and audit requirements are satisfied.

`## Features`

Reference the Features that decompose the Epic.

`## Related Artifacts`

Reference relevant diagrams, business rules, reviews, or related Epics.


### Feature

Required sections:

1. TL;DR
2. Business Objective
3. Business Value
4. Scope
5. Business Rules
6. Stories
7. Related Artifacts

Optional or extension sections may include:

- Purpose
- Parent Epic
- Business Need
- Business Outcome
- Out of Scope
- Primary Actors
- Preconditions
- Trigger
- Main Success Flow
- Alternate Flows
- Exception Flows
- Business Controls
- Assumptions
- Dependencies
- Data Requirements
- Related Diagrams
- Open Questions
- Notes

A Feature defines a cohesive business capability that contributes toward its Epic.

#### Feature Example

`# FEATURE-CUST-01 — Update Mailing Address`

`## TL;DR`

Allow an authenticated customer to update a mailing address after required validation.

`## Business Objective`

Enable customers to maintain an accurate mailing address without requiring customer-service assistance.

`## Business Value`

Reduces manual service requests, improves customer contact-data quality, and decreases the risk of correspondence being sent to an outdated address.

`## Scope`

Includes capture, validation, confirmation, and audit of a customer mailing-address change.

`## Business Rules`

Reference the Business Rule artifact governing address changes.

`## Stories`

Reference the Stories that decompose the Feature.

`## Related Artifacts`

Reference the parent Epic, Business Rules, Reviews, diagrams, and other directly related artifacts.


### Story

Required sections:

1. TL;DR
2. User Story
3. Business Value
4. Scope
5. Related Artifacts

Optional sections may include Purpose, Preconditions, Business Rules, and Notes.

A Story expresses a user-centered requirement that delivers a testable increment of business capability.

#### Story Example

`# US-E6-101 — Propose New Debt Transaction`

`## TL;DR`

Allow an authorized Issuance Officer to establish a new debt transaction as a Draft.

`## User Story`

As an Issuance Officer, I want to create a proposed debt transaction so that it can be validated and submitted for approval.

`## Business Value`

Establishes a controlled starting point for the transaction lifecycle and prevents incomplete proposals from bypassing validation.

`## Scope`

Describe what behavior belongs to this Story and what remains the responsibility of other Stories.

`## Related Artifacts`

Reference the parent Feature, Acceptance Criteria, applicable Business Rules, diagrams, and other directly related repository artifacts.

#### Story and Acceptance Criteria Relationship

Acceptance Criteria define the observable conditions that demonstrate that a Story has been satisfied.

When Acceptance Criteria are maintained as separate repository artifacts, the Story should reference them under `Related Artifacts`.

Example:

`### Acceptance Criteria`

`- [[AC-E6-101]]`

Acceptance Criteria should not be hidden inside a generic Notes section when a dedicated Acceptance Criteria artifact exists.

This preserves explicit traceability:

**Epic → Feature → Story → Acceptance Criteria**

### Acceptance Criteria

Required sections:

1. Acceptance Criteria
2. Related Artifacts

Optional or extension sections may include:

- TL;DR
- Purpose
- Notes
- Test Data Considerations
- Examples

Acceptance Criteria should remain focused on observable and testable behavior. A mandatory TL;DR or Purpose section is not required when those sections would merely repeat the YAML description or the criteria themselves.

#### Acceptance Criteria Example

`# AC-CUST-101 — Update Mailing Address`

`## Acceptance Criteria`

`### AC-CUST-101-01 — Require Complete Address Information`

Given an authenticated customer is updating a mailing address,

when required address information is missing,

then the application identifies the missing information and does not save the address change.

`## Related Artifacts`

`### User Story`

`- [[US-CUST-101-update-mailing-address]]`

`### Business Rules`

`- [[BR-FEATURE-CUST-01]]`


### Business Rule

Required sections:

1. TL;DR
2. Business Rules
3. Related Artifacts

Optional or extension sections may include:

- Purpose
- Rationale
- Impact
- Examples
- Exceptions
- Notes

Business Rules define constraints, policies, or conditions that govern business behavior independently of a particular implementation.

Rationale and Impact are useful when they add meaningful context, but they should not be required mechanically for every Business Rule artifact.

#### Business Rule Example

`# BR-FEATURE-CUST-01 — Mailing Address Business Rules`

`## TL;DR`

Defines the authorization, validation, and audit rules that govern customer mailing-address changes.

`## Business Rules`

`BR-CUST-001 — Only an authenticated customer or authorized representative may submit a mailing-address change.`

`BR-CUST-002 — Required address elements must be present before the change may be accepted.`

`## Related Artifacts`

Reference the Feature and Stories governed by these rules.


### Review

Required sections:

1. TL;DR
2. Purpose
3. Scope Reviewed
4. Findings
5. Decisions
6. Follow-up Actions
7. Related Artifacts

Optional or extension sections may include:

- Story Decomposition
- Business Workflow
- Traceability
- Testability
- Overall Assessment
- Open Questions
- Review Outcome
- Conclusion
- Notes

A Review records the outcome of a structured requirements walkthrough or quality review. It is evidence about the requirements rather than a business requirement itself.

#### Review Example

`# REVIEW-FEATURE-CUST-01 — Requirements Walkthrough`

`## TL;DR`

FEATURE-CUST-01 was reviewed for scope, decomposition, traceability, and testability and was considered ready to support downstream design.

`## Purpose`

Evaluate FEATURE-CUST-01 as a complete business capability before implementation.

`## Scope Reviewed`

Identify the requirement artifacts and business behavior included in the walkthrough.

`## Findings`

Record material observations discovered during the review.

`## Decisions`

Record conclusions or decisions reached during the walkthrough.

`## Follow-up Actions`

Record unresolved work and actions required after the review.

`## Related Artifacts`

Reference the Feature, Stories, Acceptance Criteria, Business Rules, diagrams, and other artifacts reviewed.


## Lists

Use unordered lists when sequence is not important.

Use numbered lists when order matters.

Avoid unnecessary nesting.

## Tables

Tables are preferred for traceability, status summaries, relationship matrices, validation summaries, and requirement cross-references.

Avoid using tables for narrative descriptions when prose communicates the information more clearly.

## Code Blocks

Fenced code blocks are supported and encouraged when they improve clarity for structured or technical content.

Examples include YAML, Bash, JSON, SQL, PlantUML, configuration, structured text, and workflow illustrations.

Specify the language whenever practical.

Fenced code blocks must be properly opened and closed.

Code blocks are a normal part of the repository documentation standard. Temporary limitations imposed by a particular authoring tool or AI-assisted workflow should be documented separately and must not redefine this standard.

## Cross References

Use Obsidian wiki links for repository artifacts.

Prefer artifact identifiers or established repository artifact names over arbitrary prose references.

Examples:

- `[[EPIC-E6-issue-and-settle-security]]`
- `[[FEATURE-E6-01-propose-and-approve-debt-transaction]]`
- `[[US-E6-101-propose-new-debt-transaction]]`
- `[[AC-E6-101]]`
- `[[BR-FEATURE-E6-01]]`

Important traceability relationships should be visible to the reader rather than relying only on YAML metadata.

## Writing Style

Requirement documents should be concise, objective, understandable to business and delivery stakeholders, implementation independent where practical, and written using active voice.

Use present tense whenever practical.

Avoid implementation details unless the artifact specifically requires them.

Do not remove useful business context merely to make documents structurally identical.

Consistency supports comprehension; it should not replace professional judgment.

## Validation Checklist

Before approving a document verify:

- Heading hierarchy is correct.
- Exactly one H1 is present.
- Required semantic sections for the artifact type are present.
- Required sections follow the prescribed order.
- Optional sections add useful context rather than unnecessary duplication.
- YAML description, TL;DR, Purpose, Business Objective, and Business Value are used according to their distinct intent where applicable.
- Story Acceptance Criteria are explicitly and bidirectionally traceable when maintained as separate artifacts.
- Cross-references resolve correctly.
- Fenced code blocks, when used, are properly opened and closed and specify a language where practical.
- Formatting is consistent throughout the document.
- The document remains understandable and maintainable by a Business Analyst working manually.

## Relationship to STANDARD-REQ-001

STANDARD-REQ-001 defines artifact metadata.

STANDARD-REQ-002 defines the human-readable document body, canonical structures, section intent, and authoring conventions.

Together they define the baseline structure of requirement artifacts while allowing additional business context where appropriate.

## Relationship to Repository Validation

Repository validation should enforce stable structural rules without turning optional authoring guidance into unnecessary validation failures.

The validator supports the standard; it does not define the standard.

Required structural rules are candidates for automated validation.

Optional sections and qualitative writing guidance generally require human judgment and should not automatically become hard validation errors.

This distinction allows the standards to support both reliable automation and practical Business Analyst work.

## EFK Candidate

This standard captures document organization and authoring conventions that emerged and were refined during the E6 requirements exercise.

It is intentionally written as both a repository standard and a practical authoring reference that a Business Analyst can use when creating requirements manually.

After successful reuse and validation, it should be evaluated together with STANDARD-REQ-001 as part of a reusable requirements authoring framework suitable for EFK promotion.
