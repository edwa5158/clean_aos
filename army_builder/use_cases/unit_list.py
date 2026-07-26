from army_builder.domain.unit import Unit


def unit_list_use_case(repo) -> list[Unit]:
    return repo.list()
