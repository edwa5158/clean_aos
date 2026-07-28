import json
from pathlib import Path

from army_builder.domain.warscroll import Warscroll


class JsonRepo:
    def __init__(self, warscrolls_store: str | Path):
        self._warscrolls_store = warscrolls_store

    def _warscrolls(self) -> list[dict]:
        with open(self._warscrolls_store) as f:
            return json.load(f)

    def list(self) -> list[Warscroll]:
        return [
            Warscroll.from_dict(warscroll_dict) for warscroll_dict in self._warscrolls()
        ]
