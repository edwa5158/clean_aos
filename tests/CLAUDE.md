# Tests

`tests/domain/`, `tests/serializers/`, `tests/use_cases/`, and `tests/repository/` mirror the package layout. `tests/architecture/` does not mirror anything — it enforces the dependency rule itself:

- `imports.py` — not collected by pytest (the name doesn't match `test_*.py`). Pure mechanics for reading the import graph: path → dotted module name, package discovery, and `ast`-based extraction that **resolves relative imports to absolute names** rather than skipping them, so `from ..serializers.unit import X` is caught.
- `test_layering.py` — Rule A: a `domain/` module importing from `army_builder` may only import `army_builder.domain`. Uses set membership against a computed allowlist, not prefix matching, so `army_builder.domain_helpers` can't masquerade as a subpackage.
- `test_purity.py` — Rule B: non-project imports must be standard library, checked against `sys.stdlib_module_names`.

The two rules cover **disjoint** halves of every import (project names vs. everything else), so one violation fails exactly one test. Keep it that way when adding rules.

Every rule file also carries self-tests that feed handwritten module-name constants through its predicate. That is how the rules are verified — **do not verify them by planting bad imports in real domain modules.** Tests are marked `architecture` (a claim about the project) or `meta` (a claim about the test machinery); the marker follows the nature of the test, not the file it sits in.
