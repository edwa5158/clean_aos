from dataclasses import dataclass, field
from typing import List

from army_builder.domain.unit import Unit


@dataclass
class Regiment:
    name: str
    leader: Unit
    unit: List[Unit] = field(default_factory=list)

    def __post_init__(self):
        if not self.leader.is_hero:
            raise ValueError(
                f"Regiment leader must be a hero. '{self.leader.name}' is not a hero"
            )
    
