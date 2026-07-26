# clean_aos

A TUI army builder for **Age of Sigmar 4th edition**, built as an exercise in applying
Clean Architecture (following Leonardo Giordani's *Clean Architectures in Python*).

Longer term this may grow into a play companion: dice rolling, ability reminders, and
automatic rule application.

## The dependency rule

Dependencies point **inward only**. An outer layer may know about the layers beneath it;
an inner layer must never know anything about what surrounds it.

| Layer | May import |
| --- | --- |
| `domain/` | stdlib only |
| `use_cases/` | `domain` + stdlib |
| `serializers/` | `domain` + stdlib |
| `repository/` *(future)* | `domain` + `use_cases` + stdlib + its driver (`sqlite3`, …) |
| `ui/` *(future)* | `use_cases`, `serializers`, `domain` |

Nothing imports `ui/`.

`domain/` has the strictest rule and is the one worth guarding hardest — a violation there
is what actually corrupts the architecture. Where an inner layer needs to *use* something
outer, it takes it as an argument (as `load_army_use_case(repo, request)` does) and types it
against a `typing.Protocol` defined in the inner layer, so the dependency is never expressed
as an import in either direction.

## Layout

```
army_builder/
├── domain/       # entities: Unit, Regiment, Army. Invariants live here.
├── use_cases/    # one function per business action; repos passed in
└── serializers/  # JSONEncoder subclasses; domain → JSON at the boundary
tests/            # mirrors the package layout
```

## Commands

Managed with [uv](https://docs.astral.sh/uv/) (Python 3.13).

```bash
uv sync                                  # install dependencies
uv run python main.py                    # run the app
uv run pytest                            # all tests
uv run pytest tests/domain/test_unit.py  # a single file
uv run pytest -k test_unit_model_init    # a single test
uv run pytest --cov=army_builder         # with coverage
uv run ruff check .                      # lint
uv run ruff format .                     # format
```
