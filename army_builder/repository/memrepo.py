from army_builder.domain.unit import Unit


class MemRepo:
    def __init__(self, entries: list[dict]):
        self.entries = entries

    def list(self) -> list[Unit]:
        return [Unit.from_dict(dict) for dict in self.entries]
