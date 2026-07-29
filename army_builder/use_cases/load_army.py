from typing import Protocol

from army_builder.domain.army import Army


class ArmyReaderRepo(Protocol):
    def list(self) -> list[Army]: ...

    def get_army_by_name(self, army_name: str) -> Army: ...


class ArmyWriterRepo(Protocol):
    def delete(self, army_name: str) -> Army: ...

    def save(self, army_name: str) -> Army: ...


class LoadArmyRequest:
    def __init__(self, army_name: str):
        self.army_name = army_name
        self.errors = []

    def __bool__(self) -> bool:
        return len(self.errors) == 0


def load_army_use_case(repo: ArmyReaderRepo, request: LoadArmyRequest) -> Army:

    if not request:
        raise ValueError("Invalid army request.")
    try:
        army = repo.get_army_by_name(request.army_name)
    except Exception as e:
        raise ValueError(e) from None

    return army
