from dataclasses import dataclass, field
from typing import List

from army_builder.domain.regiment import Regiment


@dataclass
class Army:
    name: str
    regiment: List[Regiment] = field(default_factory=list)
