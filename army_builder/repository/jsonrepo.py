import json
from pathlib import Path

from army_builder.domain.unit import Unit


class JsonRepo:
    def __init__(self, units_store: str | Path):
        self._units_store = units_store

    def _units(self) -> list[dict]:
        with open(self._units_store) as f:
            return json.load(f)

    def list(self) -> list[Unit]:
        return [Unit.from_dict(unit_dict) for unit_dict in self._units()]
