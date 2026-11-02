"""Pack-validation eval: the personas pack stays structurally healthy.

Runs under the framework's ``eval`` marker (deterministic, no model calls).
The pack ships modes (researcher, thinker) and one pre-turn operation; its
tools set is empty, so the eval proves the empty catalog is *expected*.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from packstest.catalog import validate_pack

PACK_PATH = Path(__file__).resolve().parents[4]  # .../lisa-packs/personas


@pytest.mark.eval
def test_personas_pack_validates_from_source() -> None:
    """Entry points load; the pack has no tools by design."""

    report = validate_pack(PACK_PATH)
    assert report.ok, report.summary()
    assert report.tools == {}, f"unexpected tools: {sorted(report.tools)}"


@pytest.mark.eval
def test_personas_pack_entry_points_load() -> None:
    """The content-root entry point resolves from source."""

    report = validate_pack(PACK_PATH)
    assert "lisa.extensions.content_roots" in report.entry_points
    for group, entries in report.entry_points.items():
        for name, value in entries.items():
            assert value is not None, f"{group}:{name} failed to load"