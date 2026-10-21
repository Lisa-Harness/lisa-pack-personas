"""Catalog discovery test for the personas pack.

The pack ships mode content only — no operations and no tools. These
tests pin that the mode catalog discovers both personas and that the
front matter each mode declares is what the SDK actually reads.
"""

from __future__ import annotations

import json

from sdk.content import build_mode_catalog_json, resolve_mode_roots

from lisa_packs.personas import get_content_root

_EXPECTED_MODES = frozenset({"researcher", "thinker"})


def test_mode_roots_discovered() -> None:
    """The pack's modes/ directory is discovered as a mode root."""
    roots = resolve_mode_roots([get_content_root()])
    assert roots, "no modes/ directory found in personas pack"


def test_both_personas_discovered() -> None:
    """Both shipped personas appear in the mode catalog."""
    roots = resolve_mode_roots([get_content_root()])
    catalog = json.loads(build_mode_catalog_json(roots))

    assert set(catalog) == _EXPECTED_MODES
    for mode_id, mode in catalog.items():
        assert mode["mode_id"] == mode_id
        assert mode["mode_provider_id"] == "lisa-pack-personas"
        assert mode["description"], f"{mode_id} has no description"
        assert mode["instruction_body"], f"{mode_id} has no instruction body"


def test_personas_declare_their_routing_contract() -> None:
    """Each persona declares the routing fields the SDK routes on."""
    roots = resolve_mode_roots([get_content_root()])
    catalog = json.loads(build_mode_catalog_json(roots))

    for mode_id, mode in catalog.items():
        assert mode["mode_kind"] in {"chat", "action", "workflow"}, mode_id
        assert mode["command_pattern"], f"{mode_id} has no command pattern"
