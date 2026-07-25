#!/usr/bin/env python3
"""
Validate governed Farm Credit requirement artifacts.

The validator is read-only. It verifies:

- governed artifact discovery;
- YAML front matter delimiters and supported syntax;
- required metadata properties;
- canonical metadata property ordering;
- directory-to-type consistency;
- approved lifecycle status values;
- required categories and tags;
- lowercase kebab-case tags;
- ISO YYYY-MM-DD dates;
- unique artifact identifiers;
- identifier and filename conventions;
- required and prohibited relationship properties;
- relationship targets and parent-chain consistency;
- non-empty document bodies;
- exactly one visible H1 containing the artifact ID;
- canonical document sections as advisory warnings.

Headings inside fenced code blocks are ignored.

Exit status:

- 0 when no validation errors are found;
- 1 when one or more validation errors are found.

Warnings do not cause a nonzero exit status unless
--strict-structure is used.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path


ROOT = Path("docs/requirements")
PROJECT = "farm-credit-ba-exercise"

DIRECTORY_TYPES = {
    "epics": "epic",
    "features": "feature",
    "stories": "story",
    "acceptance-criteria": "acceptance-criteria",
    "business-rules": "business-rule",
    "reviews": "review",
}

TYPE_CATEGORIES = {
    "epic": [
        "[[Epics]]",
        "[[Requirements]]",
        "[[Reference Exercises]]",
    ],
    "feature": [
        "[[Features]]",
        "[[Requirements]]",
        "[[Reference Exercises]]",
    ],
    "story": [
        "[[Stories]]",
        "[[Requirements]]",
        "[[Reference Exercises]]",
    ],
    "acceptance-criteria": [
        "[[Acceptance Criteria]]",
        "[[Requirements]]",
        "[[Reference Exercises]]",
    ],
    "business-rule": [
        "[[Business Rules]]",
        "[[Requirements]]",
        "[[Reference Exercises]]",
    ],
    "review": [
        "[[Reviews]]",
        "[[Requirements]]",
        "[[Reference Exercises]]",
    ],
}

RELATIONSHIPS = {
    "epic": [],
    "feature": ["epic"],
    "story": ["epic", "feature"],
    "acceptance-criteria": ["epic", "feature", "story"],
    "business-rule": ["epic", "feature"],
    "review": ["epic", "feature"],
}

RELATIONSHIP_TARGET_TYPES = {
    "epic": "epic",
    "feature": "feature",
    "story": "story",
}

COMMON_KEYS = [
    "id",
    "project",
    "type",
    "status",
    "description",
    "categories",
    "tags",
    "created",
    "updated",
]

APPROVED_STATUSES = {
    "planned",
    "draft",
    "review",
    "approved",
    "complete",
}

ID_PATTERNS = {
    "epic": re.compile(r"^EPIC-E\d+$"),
    "feature": re.compile(r"^FEATURE-E\d+-\d{2}$"),
    "story": re.compile(r"^US-E\d+-\d{3}$"),
    "acceptance-criteria": re.compile(r"^AC-E\d+-\d{3}$"),
    "business-rule": re.compile(
        r"^BR-FEATURE-E\d+-\d{2}$"
    ),
    "review": re.compile(
        r"^REVIEW-FEATURE-E\d+-\d{2}$"
    ),
}

TAG_PATTERN = re.compile(
    r"^[a-z0-9]+(?:-[a-z0-9]+)*$"
)

CANONICAL_SECTIONS = {
    "epic": [
        "TL;DR",
        "Business Objective",
        "Business Value",
        "Scope",
        "Success Criteria",
        "Features",
        "Related Artifacts",
    ],
    "feature": [
        "TL;DR",
        "Business Objective",
        "Business Value",
        "Scope",
        "Business Rules",
        "Stories",
        "Related Artifacts",
    ],
    "story": [
        "TL;DR",
        "User Story",
        "Business Value",
        "Scope",
        "Related Artifacts",
    ],
    "acceptance-criteria": [
        "Acceptance Criteria",
        "Related Artifacts",
    ],
    "business-rule": [
        "TL;DR",
        "Business Rules",
        "Related Artifacts",
    ],
    "review": [
        "TL;DR",
        "Purpose",
        "Scope Reviewed",
        "Findings",
        "Decisions",
        "Follow-up Actions",
        "Related Artifacts",
    ],
}


@dataclass
class Finding:
    level: str
    path: Path
    message: str


@dataclass
class Artifact:
    path: Path
    directory: str
    expected_type: str
    metadata: dict[str, object]
    key_order: list[str]
    body: str
    findings: list[Finding] = field(default_factory=list)

    @property
    def artifact_id(self) -> str:
        value = self.metadata.get("id", "")
        return value if isinstance(value, str) else ""

    @property
    def artifact_type(self) -> str:
        value = self.metadata.get("type", "")
        return value if isinstance(value, str) else ""


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate governed requirement artifacts."
        )
    )

    parser.add_argument(
        "--strict-structure",
        action="store_true",
        help=(
            "Treat missing or out-of-order canonical body "
            "sections as errors instead of warnings."
        ),
    )

    parser.add_argument(
        "--quiet",
        action="store_true",
        help=(
            "Show findings and summary without per-artifact "
            "PASS lines."
        ),
    )

    return parser.parse_args()


def add_finding(
    artifact: Artifact,
    level: str,
    message: str,
) -> None:
    artifact.findings.append(
        Finding(
            level=level,
            path=artifact.path,
            message=message,
        )
    )


def split_front_matter(
    text: str,
    path: Path,
) -> tuple[list[str], str]:
    lines = text.splitlines()

    if not lines or lines[0].strip() != "---":
        raise ValueError(
            "missing opening YAML delimiter"
        )

    try:
        closing_index = next(
            index
            for index, line in enumerate(
                lines[1:],
                start=1,
            )
            if line.strip() == "---"
        )
    except StopIteration as exc:
        raise ValueError(
            "missing closing YAML delimiter"
        ) from exc

    metadata_lines = lines[1:closing_index]
    body_lines = lines[closing_index + 1 :]

    return metadata_lines, "\n".join(body_lines)


def unquote_scalar(value: str) -> str:
    value = value.strip()

    if (
        len(value) >= 2
        and value[0] == value[-1]
        and value[0] in {'"', "'"}
    ):
        return value[1:-1]

    return value


def parse_simple_yaml(
    lines: list[str],
) -> tuple[dict[str, object], list[str]]:
    """
    Parse the limited YAML form used by governed artifacts.

    Supported forms:

        key: value

        key:
          - value
          - value
    """

    metadata: dict[str, object] = {}
    key_order: list[str] = []
    current_list_key: str | None = None

    for line_number, line in enumerate(
        lines,
        start=2,
    ):
        if not line.strip():
            continue

        list_match = re.fullmatch(
            r"\s{2}-\s+(.+?)\s*",
            line,
        )

        if list_match:
            if current_list_key is None:
                raise ValueError(
                    f"line {line_number}: "
                    "list item without a list property"
                )

            current_value = metadata[current_list_key]

            if current_value == "":
                metadata[current_list_key] = []
                current_value = metadata[current_list_key]

            if not isinstance(current_value, list):
                raise ValueError(
                    f"line {line_number}: malformed list "
                    f"for {current_list_key}"
                )

            current_value.append(
                unquote_scalar(
                    list_match.group(1)
                )
            )
            continue

        if line.startswith(" ") or line.startswith("\t"):
            raise ValueError(
                f"line {line_number}: "
                "unsupported indentation"
            )

        key_match = re.fullmatch(
            r"([A-Za-z][A-Za-z0-9_-]*):"
            r"(?:\s*(.*))?",
            line,
        )

        if not key_match:
            raise ValueError(
                f"line {line_number}: "
                "unsupported YAML syntax"
            )

        key = key_match.group(1)
        raw_value = key_match.group(2) or ""

        if key in metadata:
            raise ValueError(
                f"line {line_number}: "
                f"duplicate property {key}"
            )

        key_order.append(key)
        metadata[key] = unquote_scalar(raw_value)

        current_list_key = (
            key
            if raw_value == ""
            else None
        )

    return metadata, key_order


def discover_artifact_paths(
) -> list[tuple[Path, str, str]]:
    discovered: list[tuple[Path, str, str]] = []

    for directory, artifact_type in DIRECTORY_TYPES.items():
        directory_path = ROOT / directory

        if not directory_path.is_dir():
            continue

        for path in sorted(
            directory_path.glob("*.md")
        ):
            if path.name == "README.md":
                continue

            discovered.append(
                (
                    path,
                    directory,
                    artifact_type,
                )
            )

    return discovered


def load_artifacts(
) -> tuple[list[Artifact], list[Finding]]:
    artifacts: list[Artifact] = []
    load_findings: list[Finding] = []

    for (
        path,
        directory,
        expected_type,
    ) in discover_artifact_paths():
        try:
            text = path.read_text(
                encoding="utf-8"
            )

            metadata_lines, body = (
                split_front_matter(
                    text,
                    path,
                )
            )

            metadata, key_order = (
                parse_simple_yaml(
                    metadata_lines
                )
            )

        except (
            OSError,
            UnicodeError,
            ValueError,
        ) as exc:
            load_findings.append(
                Finding(
                    level="ERROR",
                    path=path,
                    message=str(exc),
                )
            )
            continue

        artifacts.append(
            Artifact(
                path=path,
                directory=directory,
                expected_type=expected_type,
                metadata=metadata,
                key_order=key_order,
                body=body,
            )
        )

    return artifacts, load_findings


def validate_required_metadata(
    artifact: Artifact,
) -> None:
    for key in COMMON_KEYS:
        if key not in artifact.metadata:
            add_finding(
                artifact,
                "ERROR",
                f"missing required property: {key}",
            )
            continue

        value = artifact.metadata[key]

        if (
            isinstance(value, str)
            and not value.strip()
        ):
            add_finding(
                artifact,
                "ERROR",
                f"required property is blank: {key}",
            )

        if (
            isinstance(value, list)
            and not value
        ):
            add_finding(
                artifact,
                "ERROR",
                f"required list property is empty: {key}",
            )


def validate_property_order(
    artifact: Artifact,
) -> None:
    expected_order = (
        COMMON_KEYS
        + RELATIONSHIPS[
            artifact.expected_type
        ]
    )

    unknown_keys = [
        key
        for key in artifact.key_order
        if key not in expected_order
    ]

    for key in unknown_keys:
        add_finding(
            artifact,
            "ERROR",
            f"unsupported metadata property: {key}",
        )

    known_actual_order = [
        key
        for key in artifact.key_order
        if key in expected_order
    ]

    expected_present_order = [
        key
        for key in expected_order
        if key in artifact.metadata
    ]

    if (
        known_actual_order
        != expected_present_order
    ):
        add_finding(
            artifact,
            "ERROR",
            "metadata properties are not in "
            "canonical order; "
            f"expected {expected_present_order}, "
            f"found {known_actual_order}",
        )


def validate_identity(
    artifact: Artifact,
) -> None:
    artifact_id = artifact.artifact_id
    artifact_type = artifact.artifact_type

    if artifact_type != artifact.expected_type:
        add_finding(
            artifact,
            "ERROR",
            f"type must be "
            f"{artifact.expected_type!r} "
            f"for directory "
            f"{artifact.directory!r}; "
            f"found {artifact_type!r}",
        )

    pattern = ID_PATTERNS[
        artifact.expected_type
    ]

    if (
        artifact_id
        and not pattern.fullmatch(
            artifact_id
        )
    ):
        add_finding(
            artifact,
            "ERROR",
            "ID does not match "
            f"{artifact.expected_type} "
            f"convention: {artifact_id}",
        )

    if artifact_id:
        stem = artifact.path.stem

        if (
            stem != artifact_id
            and not stem.startswith(
                f"{artifact_id}-"
            )
        ):
            add_finding(
                artifact,
                "ERROR",
                "filename must begin with "
                f"artifact ID {artifact_id}",
            )


def validate_common_values(
    artifact: Artifact,
) -> None:
    project = artifact.metadata.get(
        "project"
    )

    if project != PROJECT:
        add_finding(
            artifact,
            "ERROR",
            f"project must be {PROJECT!r}; "
            f"found {project!r}",
        )

    status = artifact.metadata.get(
        "status"
    )

    if status not in APPROVED_STATUSES:
        add_finding(
            artifact,
            "ERROR",
            f"unsupported status: {status!r}",
        )

    description = artifact.metadata.get(
        "description"
    )

    if not isinstance(description, str):
        add_finding(
            artifact,
            "ERROR",
            "description must be a scalar string",
        )
    elif not description.strip():
        add_finding(
            artifact,
            "ERROR",
            "description must not be blank",
        )

    validate_categories(artifact)
    validate_tags(artifact)
    validate_dates(artifact)


def validate_categories(
    artifact: Artifact,
) -> None:
    categories = artifact.metadata.get(
        "categories"
    )

    expected = TYPE_CATEGORIES[
        artifact.expected_type
    ]

    if not isinstance(categories, list):
        add_finding(
            artifact,
            "ERROR",
            "categories must be a YAML list",
        )
        return

    if categories != expected:
        add_finding(
            artifact,
            "ERROR",
            f"categories must be {expected}; "
            f"found {categories}",
        )


def validate_tags(
    artifact: Artifact,
) -> None:
    tags = artifact.metadata.get("tags")

    if not isinstance(tags, list):
        add_finding(
            artifact,
            "ERROR",
            "tags must be a YAML list",
        )
        return

    for required_tag in (
        "farm-credit",
        "requirements",
    ):
        if required_tag not in tags:
            add_finding(
                artifact,
                "ERROR",
                f"missing required tag: "
                f"{required_tag}",
            )

    if len(tags) != len(set(tags)):
        add_finding(
            artifact,
            "ERROR",
            "tags contain duplicate values",
        )

    for tag in tags:
        if (
            not isinstance(tag, str)
            or not TAG_PATTERN.fullmatch(tag)
        ):
            add_finding(
                artifact,
                "ERROR",
                "tag must use lowercase "
                f"kebab-case: {tag!r}",
            )


def validate_dates(
    artifact: Artifact,
) -> None:
    parsed_dates: dict[str, date] = {}

    for key in ("created", "updated"):
        value = artifact.metadata.get(key)

        if not isinstance(value, str):
            add_finding(
                artifact,
                "ERROR",
                f"{key} must be a "
                "YYYY-MM-DD scalar",
            )
            continue

        if not re.fullmatch(
            r"\d{4}-\d{2}-\d{2}",
            value,
        ):
            add_finding(
                artifact,
                "ERROR",
                f"{key} must use YYYY-MM-DD: "
                f"{value!r}",
            )
            continue

        try:
            parsed_dates[key] = (
                date.fromisoformat(value)
            )
        except ValueError:
            add_finding(
                artifact,
                "ERROR",
                f"{key} is not a valid "
                f"calendar date: {value!r}",
            )

    if (
        "created" in parsed_dates
        and "updated" in parsed_dates
        and parsed_dates["updated"]
        < parsed_dates["created"]
    ):
        add_finding(
            artifact,
            "ERROR",
            "updated date precedes created date",
        )


def validate_relationship_shape(
    artifact: Artifact,
) -> None:
    expected_relationships = RELATIONSHIPS[
        artifact.expected_type
    ]

    for key in expected_relationships:
        value = artifact.metadata.get(key)

        if (
            not isinstance(value, str)
            or not value.strip()
        ):
            add_finding(
                artifact,
                "ERROR",
                "missing or blank required "
                f"relationship: {key}",
            )

    for key in RELATIONSHIP_TARGET_TYPES:
        if (
            key not in expected_relationships
            and key in artifact.metadata
        ):
            add_finding(
                artifact,
                "ERROR",
                f"relationship {key!r} "
                "does not apply to "
                f"{artifact.expected_type}",
            )


def extract_visible_lines(
    lines: list[str],
) -> list[str]:
    """
    Return lines outside fenced code blocks.

    Supports backtick and tilde fences.
    """

    visible_lines: list[str] = []
    inside_fence = False
    fence_character: str | None = None
    fence_length = 0

    for line in lines:
        stripped = line.lstrip()

        fence_match = re.match(
            r"^(`{3,}|~{3,})",
            stripped,
        )

        if fence_match:
            marker = fence_match.group(1)
            marker_character = marker[0]
            marker_length = len(marker)

            if not inside_fence:
                inside_fence = True
                fence_character = marker_character
                fence_length = marker_length

            elif (
                fence_character
                == marker_character
                and marker_length >= fence_length
            ):
                inside_fence = False
                fence_character = None
                fence_length = 0

            continue

        if not inside_fence:
            visible_lines.append(line)

    return visible_lines


def validate_body(
    artifact: Artifact,
    strict_structure: bool,
) -> None:
    if not artifact.body.strip():
        add_finding(
            artifact,
            "ERROR",
            "document body is empty",
        )
        return

    lines = artifact.body.splitlines()

    visible_lines: list[str] = []
    inside_fence = False
    fence_character: str | None = None

    for line in lines:
        stripped = line.lstrip()
        fence_match = re.match(r"^(`{3,}|~{3,})", stripped)

        if fence_match:
            marker = fence_match.group(1)
            marker_character = marker[0]

            if not inside_fence:
                inside_fence = True
                fence_character = marker_character
            elif fence_character == marker_character:
                inside_fence = False
                fence_character = None

            continue

        if not inside_fence:
            visible_lines.append(line)

    h1_lines = [
        line.strip()
        for line in visible_lines
        if re.match(r"^#(?!#)\s+\S", line)
    ]

    if len(h1_lines) != 1:
        add_finding(
            artifact,
            "ERROR",
            "document must contain exactly "
            f"one H1; found {len(h1_lines)}",
        )
    elif (
        artifact.artifact_id
        and artifact.artifact_id not in h1_lines[0]
    ):
        add_finding(
            artifact,
            "ERROR",
            "H1 must contain artifact ID "
            f"{artifact.artifact_id}",
        )

    h2_titles = [
        match.group(1).strip()
        for line in visible_lines
        if (
            match := re.match(
                r"^##(?!#)\s+(.+?)\s*$",
                line,
            )
        )
    ]

    expected_sections = CANONICAL_SECTIONS[
        artifact.expected_type
    ]

    present_expected = [
        section
        for section in expected_sections
        if section in h2_titles
    ]

    missing_sections = [
        section
        for section in expected_sections
        if section not in h2_titles
    ]

    level = "ERROR" if strict_structure else "WARNING"

    if missing_sections:
        add_finding(
            artifact,
            level,
            "missing canonical H2 sections: "
            + ", ".join(missing_sections),
        )

    present_in_document_order = [
        section
        for section in h2_titles
        if section in expected_sections
    ]

    expected_present_order = [
        section
        for section in expected_sections
        if section in h2_titles
    ]

    if present_in_document_order != expected_present_order:
        add_finding(
            artifact,
            level,
            "canonical H2 sections are out of order",
        )

def validate_unique_ids(
    artifacts: list[Artifact],
    load_findings: list[Finding],
) -> dict[str, Artifact]:
    by_id: dict[str, Artifact] = {}

    for artifact in artifacts:
        artifact_id = artifact.artifact_id

        if not artifact_id:
            continue

        existing = by_id.get(artifact_id)

        if existing is not None:
            load_findings.append(
                Finding(
                    level="ERROR",
                    path=artifact.path,
                    message=(
                        f"duplicate artifact ID "
                        f"{artifact_id}; also used by "
                        f"{existing.path}"
                    ),
                )
            )
        else:
            by_id[artifact_id] = artifact

    return by_id


def validate_relationship_targets(
    artifacts: list[Artifact],
    by_id: dict[str, Artifact],
) -> None:
    for artifact in artifacts:
        expected_relationships = RELATIONSHIPS[
            artifact.expected_type
        ]

        for relationship in expected_relationships:
            target_id = artifact.metadata.get(
                relationship
            )

            if (
                not isinstance(target_id, str)
                or not target_id
            ):
                continue

            target = by_id.get(target_id)

            if target is None:
                add_finding(
                    artifact,
                    "ERROR",
                    f"{relationship} references "
                    "nonexistent artifact ID: "
                    f"{target_id}",
                )
                continue

            expected_target_type = (
                RELATIONSHIP_TARGET_TYPES[
                    relationship
                ]
            )

            if (
                target.artifact_type
                != expected_target_type
            ):
                add_finding(
                    artifact,
                    "ERROR",
                    f"{relationship} must reference "
                    f"a {expected_target_type}; "
                    f"{target_id} is "
                    f"{target.artifact_type}",
                )


GOVERNED_WIKI_LINK_PATTERN = re.compile(
    r"^("
    r"EPIC-E\d+"
    r"|FEATURE-E\d+-\d{2}"
    r"|US-E\d+-\d{3}"
    r"|AC-E\d+-\d{3}"
    r"|BR-FEATURE-E\d+-\d{2}"
    r"|REVIEW-FEATURE-E\d+-\d{2}"
    r")(?:-|$)"
)


def validate_governed_wiki_links(
    artifacts: list[Artifact],
    by_id: dict[str, Artifact],
) -> None:
    # Validate governed-artifact-looking wiki links in visible body text.
    filename_stems = {
        artifact.path.stem: artifact
        for artifact in artifacts
    }

    for artifact in artifacts:
        visible_lines = extract_visible_lines(
            artifact.body.splitlines()
        )

        for line_number, line in enumerate(
            visible_lines,
            start=1,
        ):
            for match in re.finditer(
                r"\[\[([^\]]+)\]\]",
                line,
            ):
                raw_target = match.group(1).strip()
                target = raw_target.split("|", 1)[0].strip()

                governed_match = (
                    GOVERNED_WIKI_LINK_PATTERN.match(target)
                )

                if governed_match is None:
                    continue

                artifact_id = governed_match.group(1)

                if (
                    artifact_id in by_id
                    and (
                        target == artifact_id
                        or target in filename_stems
                    )
                ):
                    continue

                add_finding(
                    artifact,
                    "ERROR",
                    "wiki link references nonexistent "
                    "governed artifact: "
                    f"[[{raw_target}]] "
                    f"(visible body line {line_number})",
                )


def validate_parent_chain(
    artifacts: list[Artifact],
    by_id: dict[str, Artifact],
) -> None:
    for artifact in artifacts:
        metadata = artifact.metadata
        artifact_type = artifact.expected_type

        epic_id = metadata.get("epic")
        feature_id = metadata.get("feature")
        story_id = metadata.get("story")

        feature = (
            by_id.get(feature_id)
            if isinstance(feature_id, str)
            else None
        )

        story = (
            by_id.get(story_id)
            if isinstance(story_id, str)
            else None
        )

        if (
            feature is not None
            and isinstance(epic_id, str)
        ):
            feature_epic = (
                feature.metadata.get("epic")
            )

            if feature_epic != epic_id:
                add_finding(
                    artifact,
                    "ERROR",
                    f"epic {epic_id} does not "
                    f"match {feature_id} parent "
                    f"epic {feature_epic}",
                )

        if (
            artifact_type
            == "acceptance-criteria"
            and story is not None
        ):
            story_feature = (
                story.metadata.get("feature")
            )

            story_epic = (
                story.metadata.get("epic")
            )

            if story_feature != feature_id:
                add_finding(
                    artifact,
                    "ERROR",
                    f"feature {feature_id} does not "
                    f"match {story_id} parent "
                    f"feature {story_feature}",
                )

            if story_epic != epic_id:
                add_finding(
                    artifact,
                    "ERROR",
                    f"epic {epic_id} does not "
                    f"match {story_id} parent "
                    f"epic {story_epic}",
                )


def validate_artifacts(
    artifacts: list[Artifact],
    strict_structure: bool,
) -> None:
    for artifact in artifacts:
        validate_required_metadata(artifact)
        validate_property_order(artifact)
        validate_identity(artifact)
        validate_common_values(artifact)
        validate_relationship_shape(artifact)

        validate_body(
            artifact,
            strict_structure,
        )


def print_results(
    artifacts: list[Artifact],
    load_findings: list[Finding],
    quiet: bool,
) -> tuple[int, int]:
    findings = list(load_findings)

    for artifact in artifacts:
        findings.extend(
            artifact.findings
        )

    findings.sort(
        key=lambda finding: (
            str(finding.path),
            (
                0
                if finding.level == "ERROR"
                else 1
            ),
            finding.message,
        )
    )

    errors = [
        finding
        for finding in findings
        if finding.level == "ERROR"
    ]

    warnings = [
        finding
        for finding in findings
        if finding.level == "WARNING"
    ]

    findings_by_path: dict[
        Path,
        list[Finding],
    ] = {}

    for finding in findings:
        findings_by_path.setdefault(
            finding.path,
            [],
        ).append(finding)

    print(
        "REQUIREMENT ARTIFACT VALIDATION"
    )
    print("=" * 80)

    if not quiet:
        for artifact in artifacts:
            artifact_findings = (
                findings_by_path.get(
                    artifact.path,
                    [],
                )
            )

            artifact_errors = [
                finding
                for finding in artifact_findings
                if finding.level == "ERROR"
            ]

            artifact_warnings = [
                finding
                for finding in artifact_findings
                if finding.level == "WARNING"
            ]

            if artifact_errors:
                status = "FAIL"
            elif artifact_warnings:
                status = "WARN"
            else:
                status = "PASS"

            print(
                f"{status:<7} "
                f"{artifact.path}"
            )

    if findings:
        print()
        print("FINDINGS")
        print("-" * 80)

        for finding in findings:
            print(
                f"{finding.level:<7} "
                f"{finding.path}: "
                f"{finding.message}"
            )

    print()
    print("=" * 80)

    discovered_count = (
        len(artifacts)
        + len(load_findings)
    )

    print(
        f"Artifacts discovered: "
        f"{discovered_count}"
    )

    print(
        f"Artifacts parsed:     "
        f"{len(artifacts)}"
    )

    print(
        f"Errors:               "
        f"{len(errors)}"
    )

    print(
        f"Warnings:             "
        f"{len(warnings)}"
    )

    if errors:
        print(
            "Result:               FAIL"
        )
    else:
        print(
            "Result:               PASS"
        )

    return len(errors), len(warnings)


def main() -> int:
    args = parse_arguments()

    if not ROOT.is_dir():
        print(
            "ERROR: governed root does "
            f"not exist: {ROOT}",
            file=sys.stderr,
        )
        return 1

    artifacts, load_findings = (
        load_artifacts()
    )

    validate_artifacts(
        artifacts,
        strict_structure=(
            args.strict_structure
        ),
    )

    by_id = validate_unique_ids(
        artifacts,
        load_findings,
    )

    validate_relationship_targets(
        artifacts,
        by_id,
    )

    validate_governed_wiki_links(
        artifacts,
        by_id,
    )

    validate_parent_chain(
        artifacts,
        by_id,
    )

    error_count, _warning_count = (
        print_results(
            artifacts,
            load_findings,
            quiet=args.quiet,
        )
    )

    return 1 if error_count else 0


if __name__ == "__main__":
    sys.exit(main())
