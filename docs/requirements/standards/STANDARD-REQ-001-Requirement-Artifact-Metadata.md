---
id: STANDARD-REQ-001
project: farm-credit-ba-exercise

type: standard
status: draft

description: Defines the common metadata, classification, and relationship fields used by requirement artifacts in this repository.

categories:
  - "[[Standards]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"

tags:
  - requirements
  - metadata
  - standards

created: 2026-07-23
updated: 2026-07-23
---

# STANDARD-REQ-001

## Requirement Artifact Metadata Standard

## Purpose

Define a consistent YAML front matter structure for requirement artifacts in this repository.

The standard supports:

- consistent authoring;
- human-readable metadata;
- explicit requirement traceability;
- predictable Obsidian navigation;
- future automated validation.

## Scope

This standard applies to:

- Epic
- Feature
- Story
- Acceptance Criteria
- Business Rule
- Review

The standard does not currently govern PlantUML source files, diagram guides, repository manifests, or general project documentation.

## Guiding Principles

- Use one common metadata order across artifact types.
- Place artifact identity and classification before relationships.
- Include only relationship fields that apply to the artifact.
- Keep categories and tags purposeful.
- Preserve explicit traceability from child artifacts to their parents.
- Avoid empty or speculative metadata properties.

## Common Metadata Order

All governed artifacts use the following common property order:

```yaml
---
id:
project:

type:
status:

description:

categories:
tags:

created:
updated:
---
```

Artifact-specific relationship fields follow the common metadata block:

```yaml
epic:
feature:
story:
```

Only applicable relationship fields are included.

## Common Metadata Properties

| Property | Required | Purpose |
|---|:---:|---|
| `id` | Yes | Stable identifier for the artifact |
| `project` | Yes | Repository or project identifier |
| `type` | Yes | Artifact type |
| `status` | Yes | Current lifecycle state |
| `description` | Yes | Concise summary of the artifact |
| `categories` | Yes | Obsidian classification and navigation |
| `tags` | Yes | Search-oriented keywords |
| `created` | Yes | Artifact creation date |
| `updated` | Yes | Most recent substantive update date |

## Artifact Types

Approved `type` values for governed requirement artifacts are:

```text
epic
feature
story
acceptance-criteria
business-rule
review
```

Governance documents may use:

```text
standard
index
adr
```

Governance documents are outside the requirement hierarchy but follow the same common metadata ordering.

## Status Values

Use the lifecycle state that accurately reflects the artifact.

Approved values are:

```text
planned
draft
review
approved
complete
```

Do not mark an artifact `approved` or `complete` unless the repository workflow supports that state.

## Categories

Every governed requirement artifact includes:

1. its artifact-type category;
2. `[[Requirements]]`;
3. `[[Reference Exercises]]`.

| Artifact Type | Categories |
|---|---|
| Epic | `[[Epics]]`, `[[Requirements]]`, `[[Reference Exercises]]` |
| Feature | `[[Features]]`, `[[Requirements]]`, `[[Reference Exercises]]` |
| Story | `[[Stories]]`, `[[Requirements]]`, `[[Reference Exercises]]` |
| Acceptance Criteria | `[[Acceptance Criteria]]`, `[[Requirements]]`, `[[Reference Exercises]]` |
| Business Rule | `[[Business Rules]]`, `[[Requirements]]`, `[[Reference Exercises]]` |
| Review | `[[Reviews]]`, `[[Requirements]]`, `[[Reference Exercises]]` |

Governance documents may also use:

```text
[[Standards]]
[[Architecture Decision Records]]
```

Category values use quoted Obsidian wiki links in YAML:

```yaml
categories:
  - "[[Stories]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"
```

## Tags

Tags support search and filtering but should remain concise.

All governed artifacts should include:

```yaml
tags:
  - farm-credit
  - requirements
```

Additional tags may identify a meaningful business domain or artifact concern, such as:

```text
debt-issuance
settlement
post-trade-reporting
validation
```

Tags use lowercase kebab-case.

## Relationship Metadata

Relationship fields follow the common metadata block and appear in hierarchy order:

```yaml
epic:
feature:
story:
```

### Relationship Matrix

| Artifact | `epic` | `feature` | `story` |
|---|:---:|:---:|:---:|
| Epic | — | — | — |
| Feature | Required | — | — |
| Story | Required | Required | — |
| Acceptance Criteria | Required | Required | Required |
| Business Rule | Required | Required | — |
| Review | Required | Required | — |

### Relationship Rules

- Every Feature belongs to one Epic.
- Every Story belongs to one Feature and one Epic.
- Every Acceptance Criteria artifact belongs to one Story, one Feature, and one Epic.
- Every Business Rule belongs to the Feature it constrains.
- Every Feature Review belongs to the Feature it evaluates.
- Relationship values use artifact IDs rather than filenames or display titles.
- Relationship fields must not point to nonexistent artifacts.

## YAML Examples

### Epic

```yaml
---
id: EPIC-E6
project: farm-credit-ba-exercise

type: epic
status: draft

description: Defines the business capabilities required to issue and settle a security.

categories:
  - "[[Epics]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"

tags:
  - farm-credit
  - requirements
  - debt-issuance

created: 2026-07-22
updated: 2026-07-23
---
```

### Feature

```yaml
---
id: FEATURE-E6-01
project: farm-credit-ba-exercise

type: feature
status: draft

description: Defines the capability to propose, validate, submit, review, and revise a debt transaction.

categories:
  - "[[Features]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"

tags:
  - farm-credit
  - requirements
  - debt-issuance

created: 2026-07-22
updated: 2026-07-23

epic: EPIC-E6
---
```

### Story

```yaml
---
id: US-E6-101
project: farm-credit-ba-exercise

type: story
status: draft

description: Enables an issuance officer to propose a new debt transaction.

categories:
  - "[[Stories]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"

tags:
  - farm-credit
  - requirements
  - debt-issuance

created: 2026-07-22
updated: 2026-07-23

epic: EPIC-E6
feature: FEATURE-E6-01
---
```

### Acceptance Criteria

```yaml
---
id: AC-E6-101
project: farm-credit-ba-exercise

type: acceptance-criteria
status: draft

description: Defines the conditions required to propose a new debt transaction successfully.

categories:
  - "[[Acceptance Criteria]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"

tags:
  - farm-credit
  - requirements
  - validation

created: 2026-07-23
updated: 2026-07-23

epic: EPIC-E6
feature: FEATURE-E6-01
story: US-E6-101
---
```

### Business Rule

```yaml
---
id: BR-FEATURE-E6-01
project: farm-credit-ba-exercise

type: business-rule
status: draft

description: Defines the business rules governing proposal and approval of a debt transaction.

categories:
  - "[[Business Rules]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"

tags:
  - farm-credit
  - requirements
  - debt-issuance

created: 2026-07-22
updated: 2026-07-23

epic: EPIC-E6
feature: FEATURE-E6-01
---
```

### Review

```yaml
---
id: REVIEW-FEATURE-E6-01
project: farm-credit-ba-exercise

type: review
status: complete

description: Records the requirements walkthrough and consistency findings for Feature E6-01.

categories:
  - "[[Reviews]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"

tags:
  - farm-credit
  - requirements
  - review

created: 2026-07-22
updated: 2026-07-23

epic: EPIC-E6
feature: FEATURE-E6-01
---
```

## Validation Rules

A requirement artifact complies with this standard when:

- all required common properties are present;
- common properties use the prescribed order;
- relationship properties follow the common metadata;
- only applicable relationship fields are included;
- the `type` value matches the artifact;
- categories match the artifact type;
- tags use lowercase kebab-case;
- the description is concise and artifact-specific;
- dates use `YYYY-MM-DD`;
- relationship values reference existing artifact IDs.

## EFK Candidate

This standard is part of a broader four-phase consistency increment:

1. define requirement authoring standards;
2. normalize existing artifacts;
3. reconcile repository naming, indexes, headings, and cross-links;
4. verify compliance and traceability.

After all four phases are completed and validated, the standards, implementation findings, and verification approach should be considered together for EFK handoff.

EFK can then determine whether the framework should be promoted into reusable templates, schemas, examples, and cross-project standards.
