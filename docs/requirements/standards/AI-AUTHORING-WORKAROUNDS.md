---
id: AI-AUTHORING-WORKAROUNDS
project: farm-credit-ba-exercise

type: operational-guidance
status: temporary

description: Records temporary AI-assisted authoring workarounds that must not be confused with permanent repository documentation standards.

categories:
  - "[[Standards]]"
  - "[[Operations]]"
  - "[[AI Assisted Authoring]]"

tags:
  - ai
  - authoring
  - workaround
  - markdown
  - temporary

created: 2026-07-24
updated: 2026-07-24
---

# AI-AUTHORING-WORKAROUNDS — Temporary AI-Assisted Authoring Guidance

## TL;DR

During interactive ChatGPT-assisted repository work, ChatGPT responses intended for terminal copy/paste or direct insertion into repository files must not use Markdown fenced code blocks until this workaround is explicitly retired.

This is a temporary workflow safeguard for AI-generated working content. It is not a restriction on repository Markdown or professional Business Analyst authoring.

## Purpose

Prevent malformed, improperly closed, or unintentionally nested fenced code blocks in AI-generated chat responses from creating avoidable editing, normalization, validation, or copy/paste problems.

## Scope

This workaround applies to:

- ChatGPT responses intended for terminal copy/paste;
- ChatGPT responses intended for direct insertion into repository files;
- interactive repository-editing instructions;
- generated working snippets shown directly in chat.

This workaround does not prohibit fenced code blocks in:

- manually authored repository Markdown;
- reviewed repository artifacts;
- standards documentation;
- YAML examples;
- JSON examples;
- Bash examples;
- SQL examples;
- PlantUML;
- configuration examples;
- structured text;
- workflow illustrations;
- other content where fenced blocks improve clarity.

## Temporary Rule

Until further notice, ChatGPT should not use Markdown fenced code blocks in interactive responses for this project unless the user explicitly requests them.

Commands should be presented as indented plain text when they need to be copied from chat.

Large repository documents should preferably be generated as downloadable files rather than reconstructed manually from chat output.

## Rationale

Fenced code blocks are useful and desirable in Markdown documentation.

The temporary restriction exists because AI-generated chat content has repeatedly contained malformed, improperly terminated, or awkwardly nested fences. These formatting failures created unnecessary work and interfered with repository editing and normalization.

The workaround addresses the AI-assisted authoring workflow rather than changing the repository documentation standard.

## Relationship to STANDARD-REQ-002

STANDARD-REQ-002 continues to support and encourage properly formed fenced code blocks when they improve clarity.

This workaround must not be interpreted as changing STANDARD-REQ-002.

The professional authoring rule remains:

- use fenced blocks where they improve readability or preserve literal structured content;
- open and close fences correctly;
- specify a language where practical;
- expect repository tooling to preserve correctly formed fenced content.

## Preferred AI-Assisted Workflow

When ChatGPT needs to provide a substantial Markdown artifact:

1. Generate the artifact as a downloadable file.
2. Preserve all required Markdown headings, lists, tables, links, and examples in the file.
3. Have the user copy or move the file into the repository.
4. Inspect the resulting Git diff.
5. Run repository validation before committing.

For short terminal instructions, use indented plain-text commands rather than fenced blocks.

## Retirement Criteria

This workaround may be retired when AI-generated fenced content can be used reliably without repeated malformed-fence or copy/paste issues.

Retirement should be an explicit repository/workflow decision rather than an assumption.

## EFK Candidate Lesson

This document represents operational guidance, not a reusable documentation standard.

EFK should preserve the distinction between:

- authoring standards;
- validator behavior;
- AI-assisted authoring constraints;
- temporary operational workarounds.

Temporary tool limitations should not be promoted into permanent standards unless they represent a genuine repository requirement.
