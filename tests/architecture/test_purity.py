"""Rule B — domain purity.

A module in `domain/` may only depend on the standard library. No frameworks,
no third-party packages: domain models stay plain Python, which is why they are
bare dataclasses rather than ORM rows.

Applies to non-project imports only; `army_builder.*` names are Rule A's
business (see test_layering.py).
"""

import sys

import pytest

from .imports import DOMAIN_DIR, PROJECT_ROOT, imports_in, is_project_module, report


def violates_purity(name: str) -> bool:
    """A non-project import that is not standard library.

    `sys.stdlib_module_names` holds top-level names only, so `os.path` has to
    be reduced to `os` before lookup.
    """
    top_level = name.split(".")[0]
    return not is_project_module(name) and top_level not in sys.stdlib_module_names


# --------------------------------------------------------------------------
# The rule
# --------------------------------------------------------------------------


@pytest.mark.architecture
def test_domain_imports_only_stdlib():
    violations = [
        f"{path.relative_to(PROJECT_ROOT)} imports {name}"
        for path, name in imports_in(DOMAIN_DIR)
        if violates_purity(name)
    ]
    assert not violations, report(
        "domain may only depend on the standard library:", violations
    )


# --------------------------------------------------------------------------
# Self-tests: prove the rule detects what it claims to
# --------------------------------------------------------------------------

STDLIB_IMPORTS = ["dataclasses", "json", "sys", "os.path", "collections.abc"]

PROJECT_IMPORTS = [
    # Project names are Rule A's problem, never a purity violation — including
    # the illegal ones, so a layering mistake does not fail both tests.
    "army_builder.domain.unit",
    "army_builder.use_cases.create_army",
    "army_builder.serializers.unit",
]

THIRD_PARTY_IMPORTS = ["pytest", "requests", "numpy.linalg", "prompt_toolkit"]


@pytest.mark.meta
@pytest.mark.parametrize("name", STDLIB_IMPORTS + PROJECT_IMPORTS)
def test_stdlib_and_project_imports_pass(name):
    assert not violates_purity(name)


@pytest.mark.meta
@pytest.mark.parametrize("name", THIRD_PARTY_IMPORTS)
def test_third_party_imports_are_caught(name):
    assert violates_purity(name)
