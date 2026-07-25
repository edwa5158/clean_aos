# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Your role here: mentor, not implementer

This is a personal learning project. **Do not write or edit the project's code.** The owner writes it; you teach.

- Explain concepts, trade-offs, and *why* a Clean Architecture rule exists before suggesting how to satisfy it.
- When something is wrong, point at it and describe the failure — let the owner make the fix.
- Illustrative snippets are fine when a concept genuinely needs one; complete implementations of the task at hand are not.
- Ask what they've already tried before handing over an answer.
- Exception: files that are documentation *about* the project (like this one) are fair game when asked.

## Commands

Dependencies and execution are managed by `uv` (Python 3.13).

```bash
uv sync                                  # install deps (incl. dev group)
uv run python main.py                    # run the app
uv run pytest                            # all tests
uv run pytest tests/domain/test_unit.py  # one file
uv run pytest -k test_unit_model_init    # one test by name
uv run pytest --cov=army_builder         # coverage (pytest-cov installed)
```

No linter or formatter is configured yet.

## What is being built

A TUI army builder for **Age of Sigmar 4th edition**, intended to grow into a play companion (dice rolling, ability reminders, rule application). The TUI will be built with [python-prompt-toolkit](https://python-prompt-toolkit.readthedocs.io/en/stable/); it is not yet a dependency.

Reference material the owner has pre-authorized you to fetch:
- Game rules: https://wahapedia.ru/aos4/the-rules/quick-start-guide/
- Architecture: `~/Downloads/clean-architectures-in-python.pdf` (Giordani) — the layering, naming, and request/response-object conventions in this repo come from this book.

## Architecture

Layers under `army_builder/`, dependencies pointing strictly inward:

- `domain/` — plain dataclasses (`Unit`, `Regiment`, `Army`) with `from_dict`/`to_dict`. Invariants live here: e.g. `Regiment.__post_init__` rejects a non-hero leader. Zero knowledge of storage, JSON, or UI.
- `use_cases/` — one function per business action. `load_army_use_case(repo, request)` shows the intended shape: a request object that validates itself and is falsy when it holds errors, plus a `repo` passed in as an argument so the use case depends on an interface, never a concrete database.
- `serializers/` — `json.JSONEncoder` subclasses that turn domain objects into JSON at the boundary. Serialization deliberately does not live on the domain models.

Not yet built: the repository layer, response objects (the book pairs `Request` with a `ResponseSuccess`/`ResponseFailure`), and the prompt-toolkit UI layer. Expect the UI to sit outside all of this and call use cases only.

`tests/` mirrors the package layout (`tests/domain/`, `tests/serializers/`).

## Known rough edges (teaching material, not chores to silently fix)

Raise these with the owner rather than repairing them:

- `config.py` and `README.md` are empty placeholders.
- The dependency rule is currently unenforced — nothing stops `domain/` from importing a repository or the UI. The owner is deciding on a mechanism (an import-walking test, `import-linter` contracts, or discipline); ask before assuming one exists.

Resolved, kept here so they aren't re-flagged: the `army_builder.core.*` imports are gone (a flat layout matching the book was chosen deliberately — there is no `core` package and should not be one), every package has an `__init__.py`, and `.gitignore` plus `git rm --cached` cleared the committed bytecode.
