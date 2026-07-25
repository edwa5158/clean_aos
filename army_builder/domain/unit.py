from __future__ import annotations

import dataclasses
import uuid
from dataclasses import dataclass


@dataclass
class Unit:
    code: uuid.UUID
    name: str
    is_hero: bool = False
    is_general: bool = False

    @classmethod
    def from_dict(cls, d) -> Unit:
        return cls(**d)

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)
