"""Tests for the import-reading machinery in imports.py.

These enforce no architectural rule — they prove the parser the rules depend on
actually sees what it claims to. Marked `meta` so they can be filtered out of
an architecture-only run.
"""

import pytest

from .imports import (
    DOMAIN_DIR,
    discover_modules,
    imported_names,
    imports_in,
    is_project_module,
    module_name_for,
)

pytestmark = pytest.mark.meta


# Each case: (source, containing module, is_package, expected names)
EXTRACTION_CASES = [
    ("import json", "army_builder.domain.army", False, {"json"}),
    ("import os, sys", "army_builder.domain.army", False, {"os", "sys"}),
    (
        "import army_builder.use_cases.create_army",
        "army_builder.domain.army",
        False,
        {"army_builder.use_cases.create_army"},
    ),
    (
        "from dataclasses import dataclass, field",
        "army_builder.domain.army",
        False,
        {"dataclasses"},
    ),
    (
        "from army_builder.domain.warscroll import Warscroll",
        "army_builder.domain.army",
        False,
        {"army_builder.domain.warscroll"},
    ),
    # One dot: the package containing the module.
    (
        "from . import warscroll",
        "army_builder.domain.army",
        False,
        {"army_builder.domain"},
    ),
    (
        "from .warscroll import Warscroll",
        "army_builder.domain.army",
        False,
        {"army_builder.domain.warscroll"},
    ),
    # Two dots climb out of domain — the case a `level > 0` skip would miss.
    (
        "from ..serializers.warscroll import WarscrollEncoder",
        "army_builder.domain.army",
        False,
        {"army_builder.serializers.warscroll"},
    ),
    ("from .. import serializers", "army_builder.domain.army", False, {"army_builder"}),
    # Inside a package's __init__.py, one dot means the package itself.
    (
        "from .warscroll import Warscroll",
        "army_builder.domain",
        True,
        {"army_builder.domain.warscroll"},
    ),
    # Imports hidden inside a function body are still found.
    (
        "def f():\n    from army_builder.serializers.warscroll import WarscrollEncoder",
        "army_builder.domain.army",
        False,
        {"army_builder.serializers.warscroll"},
    ),
    ("", "army_builder.domain.army", False, set()),
]


@pytest.mark.parametrize("source, module, is_package, expected", EXTRACTION_CASES)
def test_imported_names_resolves_to_absolute(source, module, is_package, expected):
    assert imported_names(source, module, is_package=is_package) == expected


def test_module_name_for_maps_package_init_to_the_package():
    assert module_name_for(DOMAIN_DIR / "__init__.py") == "army_builder.domain"
    assert (
        module_name_for(DOMAIN_DIR / "warscroll.py") == "army_builder.domain.warscroll"
    )


def test_discover_modules_includes_the_package_itself():
    modules = discover_modules(DOMAIN_DIR)
    assert "army_builder.domain" in modules
    assert "army_builder.domain.warscroll" in modules


def test_imports_in_finds_real_domain_imports():
    names = {name for _, name in imports_in(DOMAIN_DIR)}
    assert "dataclasses" in names
    assert "army_builder.domain.warscroll" in names


@pytest.mark.parametrize(
    "name, expected",
    [
        ("army_builder", True),
        ("army_builder.domain.warscroll", True),
        ("army_builder_utils.thing", False),  # segment compare, not prefix
        ("dataclasses", False),
    ],
)
def test_is_project_module(name, expected):
    assert is_project_module(name) is expected
