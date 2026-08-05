from army_builder.domain.army import Army
from army_builder.use_cases.repositories import ArmyReaderRepo


class LoadArmyRequest:
    def __init__(self, army_name: str):
        self.army_name = army_name
        self.errors = []

    def __bool__(self) -> bool:
        return len(self.errors) == 0


class ListArmyRequest:
    pass


def load_army_use_case(repo: ArmyReaderRepo, request: LoadArmyRequest) -> Army:

    if not request:
        raise ValueError("Invalid army request.")
    try:
        army = repo.get_army_by_name(request.army_name)
    except Exception as e:
        raise ValueError(e) from None

    return army


def list_armies_use_case(repo: ArmyReaderRepo, request: ListArmyRequest) -> list[Army]:
    raise NotImplementedError
