"""Reading the import graph out of source files.

Pure mechanics — no rules live here. This module answers one question:
"what does this file import?", as a set of absolute dotted names. Deciding
which of those names are *allowed* is the job of the rule modules.

Nothing here executes the code it inspects; files are parsed, never imported.
"""

import ast
from pathlib import Path

import army_builder
import army_builder.domain

PACKAGE = "army_builder"
PACKAGE_DIR = Path(army_builder.__file__).parent
PROJECT_ROOT = PACKAGE_DIR.parent
DOMAIN_DIR = Path(army_builder.domain.__file__).parent


def module_name_for(path: Path) -> str:
    """Dotted import name for a source file, e.g. `army_builder.domain.unit`.

    A package's `__init__.py` maps to the package itself, since nobody writes
    `from army_builder.domain.__init__ import Unit`.
    """
    parts = path.resolve().relative_to(PROJECT_ROOT).with_suffix("").parts
    if parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)


def discover_modules(directory: Path) -> frozenset[str]:
    """Every importable dotted name under `directory`, packages included."""
    return frozenset(module_name_for(path) for path in directory.rglob("*.py"))


def _absolute_name(node: ast.ImportFrom, package_parts: list[str]) -> str:
    """Resolve an `ImportFrom` to an absolute dotted name.

    `node.level` is the number of leading dots: 1 is the package containing the
    module, 2 is one package above that, and so on. Resolving here means
    relative imports get checked like any other instead of being skipped —
    `from ..serializers.unit import X` escapes its package and must be seen.
    """
    tail = node.module.split(".") if node.module else []
    if node.level == 0:
        return ".".join(tail)
    base = package_parts[: len(package_parts) - (node.level - 1)]
    return ".".join([*base, *tail])


def imported_names(source: str, module: str, *, is_package: bool = False) -> set[str]:
    """Absolute dotted names imported by `source`, which lives at `module`."""
    package_parts = module.split(".") if is_package else module.split(".")[:-1]

    names: set[str] = set()
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            names.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            names.add(_absolute_name(node, package_parts))
    return names


def imports_in(directory: Path) -> list[tuple[Path, str]]:
    """Every (file, imported name) pair under `directory`."""
    found: list[tuple[Path, str]] = []
    for path in sorted(directory.rglob("*.py")):
        names = imported_names(
            path.read_text(),
            module_name_for(path),
            is_package=path.name == "__init__.py",
        )
        found.extend((path, name) for name in sorted(names))
    return found


def is_project_module(name: str) -> bool:
    """True for our own package. Compares whole segments, so a hypothetical
    `army_builder_utils` does not count as `army_builder`."""
    return name.split(".")[0] == PACKAGE


def report(header: str, violations: list[str]) -> str:
    """Assertion message: one violation per line, nothing truncated."""
    return "\n".join([header, *(f"  - {v}" for v in violations)])
