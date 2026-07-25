"""Rule A — the dependency rule.

A module in `domain/`, when it imports from `army_builder`, may only import
from `army_builder.domain`.

Applies to project imports only; everything else is Rule B's business
(see test_purity.py). The two rules cover disjoint halves of every import, so
a single mistake fails exactly one test.
"""

import pytest

from .imports import (
    DOMAIN_DIR,
    PROJECT_ROOT,
    discover_modules,
    imported_names,
    imports_in,
    is_project_module,
    report,
)


def violates_layering(name: str, allowed: frozenset[str]) -> bool:
    """A project import landing outside the allowed set.

    Membership rather than prefix matching, so `army_builder.domain_helpers`
    cannot masquerade as part of `army_builder.domain`.
    """
    return is_project_module(name) and name not in allowed


# --------------------------------------------------------------------------
# The rule
# --------------------------------------------------------------------------


@pytest.mark.architecture
def test_domain_does_not_import_outer_layers():
    allowed = discover_modules(DOMAIN_DIR)
    violations = [
        f"{path.relative_to(PROJECT_ROOT)} imports {name}"
        for path, name in imports_in(DOMAIN_DIR)
        if violates_layering(name, allowed)
    ]
    assert not violations, report(
        "domain may only import from army_builder.domain:", violations
    )


# --------------------------------------------------------------------------
# Self-tests: prove the rule detects what it claims to
# --------------------------------------------------------------------------

ALLOWED = frozenset(
    {
        "army_builder.domain",
        "army_builder.domain.army",
        "army_builder.domain.regiment",
        "army_builder.domain.unit",
    }
)

LEGAL_IMPORTS = [
    "army_builder.domain",
    "army_builder.domain.unit",
    "army_builder.domain.regiment",
    # Non-project names are Rule B's problem, never a layering violation.
    "dataclasses",
    "json",
    "pytest",
]

ILLEGAL_IMPORTS = [
    "army_builder",  # the root package sits outside domain
    "army_builder.use_cases",
    "army_builder.use_cases.create_army",
    "army_builder.serializers.unit",
    "army_builder.domain_helpers.thing",  # prefix trap: not a subpackage of domain
    "army_builder.domainlike",
]


@pytest.mark.meta
@pytest.mark.parametrize("name", LEGAL_IMPORTS)
def test_legal_imports_pass(name):
    assert not violates_layering(name, ALLOWED)


@pytest.mark.meta
@pytest.mark.parametrize("name", ILLEGAL_IMPORTS)
def test_illegal_imports_are_caught(name):
    assert violates_layering(name, ALLOWED)


@pytest.mark.meta
def test_relative_escape_is_caught():
    """The two-dot case end to end: extraction plus judgement."""
    names = imported_names(
        "from ..serializers.unit import UnitEncoder", "army_builder.domain.army"
    )
    assert [violates_layering(name, ALLOWED) for name in names] == [True]
