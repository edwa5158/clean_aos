from army_builder.domain.warscroll import Warscroll


class MemRepo:
    def __init__(self, entries: list[dict]):
        self.warscrolls = entries

    def list(self) -> list[Warscroll]:
        return [
            Warscroll.from_dict(warscroll_dict) for warscroll_dict in self.warscrolls
        ]
