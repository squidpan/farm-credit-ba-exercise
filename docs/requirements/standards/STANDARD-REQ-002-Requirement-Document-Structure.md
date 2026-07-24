---
id: STANDARD-REQ-002
project: farm-credit-ba-exercise

type: standard
status: draft

description: Defines the standard document structure and section ordering for requirement artifacts.

categories:
  - "[[Standards]]"
  - "[[Requirements]]"
  - "[[Reference Exercises]]"

tags:
  - requirements
  - documentation
  - standards

created: 2026-07-23
updated: 2026-07-23
---

# STANDARD-REQ-002

## Requirement Document Structure Standard

## Purpose

Define a consistent document structure for all requirement artifacts.

This standard complements **STANDARD-REQ-001** by defining the organization of the document body after the YAML metadata.

## Scope

This standard applies to:

- Epic
- Feature
- Story
- Acceptance Criteria
- Business Rule
- Review

It governs heading hierarchy, section ordering, writing conventions, and document consistency.

---

## Guiding Principles

- Every artifact should have a recognizable structure.
- Required sections should always appear in the same order.
- Similar artifact types should look similar.
- Documents should be optimized for both human readers and future automation.
- The document structure should communicate purpose before detail.

---

## General Heading Rules

### Heading Levels

Use ATX headings.

```text
#
##
###
```

Avoid skipping heading levels.

Each document contains exactly one H1.

---

### Document Title

The H1 should contain the artifact identifier.

Examples:

```text
# US-E6-101

# FEATURE-E6-01

# AC-E6-101

# BR-FEATURE-E6-01
```

---

### Section Ordering

Sections appear in a consistent order.

Optional sections always appear after required sections.

---

## Canonical Structures

### Epic

```text
Purpose

Business Objective

Scope

Success Criteria

Features

Notes
```

---

### Feature

```text
Purpose

Business Value

Scope

Business Rules

Stories

Notes
```

---

### Story

```text
TL;DR

User Story

Business Value

Scope

Related Artifacts

Notes
```

This ordering reflects the conventions established during the E6 requirements exercise.

---

### Acceptance Criteria

```text
Purpose

Acceptance Criteria

Related Story
```

---

### Business Rule

```text
Purpose

Business Rules

Rationale

Impact
```

---

### Review

```text
Purpose

Scope Reviewed

Findings

Decisions

Follow-up Actions
```

---

## Lists

Use unordered lists when sequence is not important.

Use numbered lists when order matters.

Avoid unnecessary nesting.

---

## Tables

Tables are preferred for:

- Traceability
- Status summaries
- Relationship matrices
- Validation summaries
- Requirement cross-references

Avoid using tables for narrative descriptions.

---

## Code Blocks

Use fenced code blocks for structured content.

Examples include:

- YAML
- Bash
- JSON
- PlantUML

Specify the language whenever practical.

---

## Cross References

Use Obsidian wiki links for repository artifacts.

Prefer artifact identifiers over filenames.

Examples:

```text
[[EPIC-E6]]

[[FEATURE-E6-01]]

[[US-E6-101]]

[[AC-E6-101]]

[[BR-FEATURE-E6-01]]
```

---

## Writing Style

Requirement documents should be:

- concise;
- objective;
- implementation independent;
- written using active voice;
- free of unnecessary narrative.

Use present tense whenever practical.

Avoid implementation details unless the artifact specifically requires them.

---

## Validation Checklist

Before approving a document verify:

- Heading hierarchy is correct.
- Required sections are present.
- Sections follow the prescribed order.
- Cross references resolve correctly.
- Code blocks specify a language where appropriate.
- Formatting is consistent throughout the document.

---

## Relationship to STANDARD-REQ-001

STANDARD-REQ-001 defines the metadata.

STANDARD-REQ-002 defines the document body.

Together they define the complete structure of every requirement artifact.

---

## EFK Candidate

This standard captures the document organization conventions that emerged during the E6 requirements exercise.

After successful reuse and validation, it should be evaluated together with STANDARD-REQ-001 as part of a reusable requirements authoring framework suitable for EFK promotion.
