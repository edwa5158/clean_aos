from typing import Protocol

from army_builder.domain.warscroll import Warscroll


class WarscrollRepository(Protocol):
    def list(self) -> list[Warscroll]: ...


def warscroll_list_use_case(repo: WarscrollRepository) -> list[Warscroll]:
    return repo.list()
