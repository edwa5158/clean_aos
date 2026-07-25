from dataclasses import dataclass, field

from army_builder.domain.regiment import Regiment


@dataclass
class Army:
    name: str
    regiment: list[Regiment] = field(default_factory=list)
