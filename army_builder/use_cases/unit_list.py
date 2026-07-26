from typing import Protocol

from army_builder.domain.unit import Unit


class UnitRepository(Protocol):
    def list(self) -> list[Unit]: ...


def unit_list_use_case(repo: UnitRepository) -> list[Unit]:
    return repo.list()
