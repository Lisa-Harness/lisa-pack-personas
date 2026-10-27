"""Catalog discovery test for the personas pack's pre-turn operations.

The pack ships ``discussion_briefing``, the enrichment step that runs before
each ``thinker`` turn. It lives here rather than in a separate search pack
because ``thinker`` is its only consumer and the kernel resolves
``pre_turn_operation_ids`` across pack boundaries.
"""

from __future__ import annotations

import json

from sdk.content import build_operation_catalog_json, resolve_operation_roots

from lisa_packs.personas import get_content_root


def test_discussion_briefing_discovered() -> None:
    """The pack's operations/ directory exposes discussion_briefing."""
    roots = resolve_operation_roots([get_content_root()])
    assert roots, "no operations/ directory found in personas pack"

    catalog = json.loads(build_operation_catalog_json(roots))

    assert "discussion_briefing" in catalog
    op = catalog["discussion_briefing"]
    assert op["operation_id"] == "discussion_briefing"
    assert op["description"]
    assert op["tool_ids"] == ["web_search"]
    assert op["response_format_model_path"].startswith(
        "lisa_packs.personas.operations."
    )
    assert op["exportable"] is True


def test_discussion_briefing_timeout_accommodates_provider_latency() -> None:
    """The timeout must exceed the 15s value that timed out twice on 2026-10-26."""
    roots = resolve_operation_roots([get_content_root()])
    catalog = json.loads(build_operation_catalog_json(roots))

    assert catalog["discussion_briefing"]["timeout_seconds"] >= 45


def test_discussion_briefing_model_importable() -> None:
    """The response model path in the front matter resolves to a real class."""
    from lisa_packs.personas.operations.research.discussion_briefing import (
        DiscussionBriefingStructuredOutput,
    )

    output = DiscussionBriefingStructuredOutput()
    assert output.output_text == ""
    assert output.source_kind == ""
    assert output.briefing_points == []
    assert output.source_urls == []
