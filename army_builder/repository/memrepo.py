from army_builder.domain.unit import Unit


class MemRepo:
    def __init__(self, entries: list[dict]):
        self.units = entries

    def list(self) -> list[Unit]:
        return [Unit.from_dict(unit_dict) for unit_dict in self.units]
