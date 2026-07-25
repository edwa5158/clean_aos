from dataclasses import dataclass, field

from army_builder.domain.unit import Unit


@dataclass
class Regiment:
    name: str
    leader: Unit
    unit: list[Unit] = field(default_factory=list)

    def __post_init__(self):
        if not self.leader.is_hero:
            raise ValueError(
                f"Regiment leader must be a hero. '{self.leader.name}' is not a hero"
            )
