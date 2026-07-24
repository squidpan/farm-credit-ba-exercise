#!/usr/bin/env python3
"""
Normalize YAML front matter for Farm Credit requirement artifacts.

Default behavior is a dry run. Use --apply to write changes.

The script:
- excludes README and other non-artifact Markdown files;
- preserves document bodies;
- preserves valid existing metadata values where possible;
- adds required project and relationship metadata;
- standardizes categories, tags, types, and property ordering;
- derives missing Acceptance Criteria descriptions from related Stories.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path("docs/requirements")
PROJECT = "farm-credit-ba-exercise"
EPIC_ID = "EPIC-E6"
UPDATED_DATE = "2026-07-23"

DIRECTORY_TYPES = {
    "epics": "epic",
    "features": "feature",
    "stories": "story",
    "acceptance-criteria": "acceptance-criteria",
    "business-rules": "business-rule",
    "reviews": "review",
}

TYPE_CATEGORIES = {
    "epic": "[[Epics]]",
    "feature": "[[Features]]",
    "story": "[[Stories]]",
    "acceptance-criteria": "[[Acceptance Criteria]]",
    "business-rule": "[[Business Rules]]",
    "review": "[[Reviews]]",
}

RELATIONSHIPS = {
    "epic": [],
    "feature": ["epic"],
    "story": ["epic", "feature"],
    "acceptance-criteria": ["epic", "feature", "story"],
    "business-rule": ["epic", "feature"],
    "review": ["epic", "feature"],
}

ORDERED_COMMON_KEYS = [
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


@dataclass
class Document:
    path: Path
    metadata: dict[str, object]
    body: str


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Normalize requirement artifact YAML front matter."
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write normalized metadata to files. Default is dry run.",
    )
    return parser.parse_args()


def split_front_matter(text: str, path: Path) -> tuple[list[str], str]:
    lines = text.splitlines()

    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{path}: missing opening YAML delimiter")

    try:
        closing_index = next(
            index
            for index, line in enumerate(lines[1:], start=1)
            if line.strip() == "---"
        )
    except StopIteration as exc:
        raise ValueError(f"{path}: missing closing YAML delimiter") from exc

    metadata_lines = lines[1:closing_index]
    body_lines = lines[closing_index + 1 :]

    body = "\n".join(body_lines)
    if text.endswith("\n"):
        body += "\n"

    return metadata_lines, body


def parse_simple_yaml(lines: list[str], path: Path) -> dict[str, object]:
    """
    Parse the limited YAML shape used by these documents.

    Supported forms:
      key: value

      key:
        - value
        - value
    """

    metadata: dict[str, object] = {}
    current_list_key: str | None = None

    for line_number, line in enumerate(lines, start=2):
        if not line.strip():
            continue

        list_match = re.match(r'^\s+-\s+"?(.*?)"?\s*$', line)
        if list_match and current_list_key:
            value = list_match.group(1)
            current_value = metadata[current_list_key]

            if current_value == "":
                metadata[current_list_key] = []
                current_value = metadata[current_list_key]

            if not isinstance(current_value, list):
                raise ValueError(
                    f"{path}:{line_number}: malformed list for {current_list_key}"
                )

            current_value.append(value)
            continue

        key_match = re.match(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$", line)
        if not key_match:
            raise ValueError(
                f"{path}:{line_number}: unsupported YAML line: {line}"
            )

        key = key_match.group(1)
        raw_value = (key_match.group(2) or "").strip()

        if raw_value:
            metadata[key] = strip_yaml_quotes(raw_value)
            current_list_key = None
        else:
            metadata[key] = ""
            current_list_key = key

    return metadata


def strip_yaml_quotes(value: str) -> str:
    if len(value) >= 2:
        if value.startswith('"') and value.endswith('"'):
            return value[1:-1]
        if value.startswith("'") and value.endswith("'"):
            return value[1:-1]

    return value


def load_document(path: Path) -> Document:
    text = path.read_text(encoding="utf-8")
    metadata_lines, body = split_front_matter(text, path)
    metadata = parse_simple_yaml(metadata_lines, path)

    return Document(path=path, metadata=metadata, body=body)


def artifact_paths() -> Iterable[Path]:
    for directory_name in DIRECTORY_TYPES:
        directory = ROOT / directory_name

        for path in sorted(directory.glob("*.md")):
            if path.name.upper() == "README.MD":
                continue

            yield path


def infer_feature_id(artifact_id: str) -> str | None:
    feature_match = re.search(r"FEATURE-E6-(\d{2})", artifact_id)
    if feature_match:
        return f"FEATURE-E6-{feature_match.group(1)}"

    numbered_match = re.search(r"E6-(\d)(\d{2})", artifact_id)
    if numbered_match:
        feature_number = int(numbered_match.group(1))
        return f"FEATURE-E6-{feature_number:02d}"

    return None


def infer_story_id(artifact_id: str) -> str | None:
    match = re.fullmatch(r"AC-E6-(\d{3})", artifact_id)
    if not match:
        return None

    return f"US-E6-{match.group(1)}"


def story_title_from_filename(path: Path) -> str:
    stem = path.stem

    stem = re.sub(r"^US-E6-\d{3}-", "", stem)
    return stem.replace("-", " ").title()


def build_story_titles(documents: list[Document]) -> dict[str, str]:
    titles: dict[str, str] = {}

    for document in documents:
        if document.path.parent.name != "stories":
            continue

        artifact_id = str(document.metadata.get("id", "")).strip()
        if not artifact_id:
            continue

        title = story_title_from_filename(document.path)
        titles[artifact_id] = title

    return titles


def normalize_list(value: object) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]

    if value is None:
        return []

    text = str(value).strip()
    return [text] if text else []


def unique_preserving_order(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []

    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)

    return result


def normalize_categories(
    artifact_type: str,
    existing: object,
) -> list[str]:
    required = [
        TYPE_CATEGORIES[artifact_type],
        "[[Requirements]]",
        "[[Reference Exercises]]",
    ]

    existing_values = normalize_list(existing)

    return unique_preserving_order(required + existing_values)


def normalize_tags(existing: object) -> list[str]:
    required = ["farm-credit", "requirements"]
    existing_values = normalize_list(existing)

    normalized_existing = [
        value.strip().lower().replace(" ", "-")
        for value in existing_values
        if value.strip()
    ]

    return unique_preserving_order(required + normalized_existing)


def normalize_description(
    artifact_type: str,
    metadata: dict[str, object],
    story_titles: dict[str, str],
) -> str:
    existing = str(metadata.get("description", "")).strip()
    if existing:
        return existing

    artifact_id = str(metadata.get("id", "")).strip()

    if artifact_type == "acceptance-criteria":
        story_id = infer_story_id(artifact_id)
        story_title = story_titles.get(story_id or "", "")

        if story_title and story_id:
            return (
                "Defines the acceptance criteria for the "
                f"{story_id} {story_title} story."
            )

        if story_id:
            return f"Defines the acceptance criteria for the {story_id} story."

    return f"Defines the {artifact_type.replace('-', ' ')} requirements for {artifact_id}."


def normalize_metadata(
    document: Document,
    story_titles: dict[str, str],
) -> dict[str, object]:
    directory_name = document.path.parent.name
    artifact_type = DIRECTORY_TYPES[directory_name]

    existing = document.metadata
    artifact_id = str(existing.get("id", "")).strip()

    if not artifact_id:
        raise ValueError(f"{document.path}: missing artifact id")

    normalized: dict[str, object] = {}

    normalized["id"] = artifact_id
    normalized["project"] = PROJECT
    normalized["type"] = artifact_type
    normalized["status"] = str(existing.get("status", "draft")).strip() or "draft"
    normalized["description"] = normalize_description(
        artifact_type,
        existing,
        story_titles,
    )
    normalized["categories"] = normalize_categories(
        artifact_type,
        existing.get("categories"),
    )
    normalized["tags"] = normalize_tags(existing.get("tags"))

    created = str(existing.get("created", "")).strip()

    if not created:
        created = UPDATED_DATE

    normalized["created"] = created
    normalized["updated"] = UPDATED_DATE

    if "epic" in RELATIONSHIPS[artifact_type]:
        normalized["epic"] = EPIC_ID

    if "feature" in RELATIONSHIPS[artifact_type]:
        feature_id = infer_feature_id(artifact_id)
        if not feature_id:
            raise ValueError(
                f"{document.path}: unable to infer Feature from {artifact_id}"
            )
        normalized["feature"] = feature_id

    if "story" in RELATIONSHIPS[artifact_type]:
        story_id = infer_story_id(artifact_id)
        if not story_id:
            raise ValueError(
                f"{document.path}: unable to infer Story from {artifact_id}"
            )
        normalized["story"] = story_id

    return normalized


def yaml_quote(value: str) -> str:
    if value.startswith("[[") and value.endswith("]]"):
        return f'"{value}"'

    return value


def render_front_matter(metadata: dict[str, object]) -> str:
    lines = ["---"]

    for index, key in enumerate(ORDERED_COMMON_KEYS):
        if key not in metadata:
            continue

        value = metadata[key]

        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {yaml_quote(str(item))}")
        else:
            lines.append(f"{key}: {value}")

        if key in {"project", "status", "description", "tags"}:
            lines.append("")

    relationship_keys = [
        key
        for key in ("epic", "feature", "story")
        if key in metadata
    ]

    if relationship_keys:
        if lines[-1] != "":
            lines.append("")

        for key in relationship_keys:
            lines.append(f"{key}: {metadata[key]}")

    lines.append("---")
    return "\n".join(lines)


def render_document(metadata: dict[str, object], body: str) -> str:
    front_matter = render_front_matter(metadata)

    normalized_body = body.lstrip("\n")

    return f"{front_matter}\n\n{normalized_body}"


def summarize_changes(
    original: dict[str, object],
    normalized: dict[str, object],
) -> list[str]:
    changes: list[str] = []

    keys = unique_preserving_order(
        list(original.keys()) + list(normalized.keys())
    )

    for key in keys:
        old_value = original.get(key)
        new_value = normalized.get(key)

        if old_value != new_value:
            if key not in original:
                changes.append(f"add {key}")
            elif key not in normalized:
                changes.append(f"remove {key}")
            else:
                changes.append(f"update {key}")

    original_order = [
        key
        for key in original
        if key in normalized
    ]
    normalized_order = [
        key
        for key in normalized
        if key in original
    ]

    if original_order != normalized_order:
        changes.append("reorder properties")

    return unique_preserving_order(changes)


def main() -> int:
    arguments = parse_arguments()

    try:
        documents = [load_document(path) for path in artifact_paths()]
        story_titles = build_story_titles(documents)

        changed_files = 0

        mode = "APPLY" if arguments.apply else "DRY RUN"
        print(f"REQUIREMENT METADATA NORMALIZATION — {mode}")
        print("=" * 80)

        for document in documents:
            normalized_metadata = normalize_metadata(
                document,
                story_titles,
            )

            normalized_text = render_document(
                normalized_metadata,
                document.body,
            )
            original_text = document.path.read_text(encoding="utf-8")

            if normalized_text == original_text:
                print(f"OK      {document.path}")
                continue

            changed_files += 1
            changes = summarize_changes(
                document.metadata,
                normalized_metadata,
            )

            print(f"CHANGE  {document.path}")
            for change in changes:
                print(f"        - {change}")

            if arguments.apply:
                document.path.write_text(
                    normalized_text,
                    encoding="utf-8",
                )

        print()
        print("=" * 80)
        print(f"Artifacts checked: {len(documents)}")
        print(f"Artifacts changed: {changed_files}")
        print(f"Mode:              {mode}")

        if not arguments.apply:
            print()
            print("No files were modified.")
            print("Run again with --apply only after reviewing this output.")

        return 0

    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
