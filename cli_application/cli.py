#!/usr/bin/env -S uv run python
from army_builder.repository.jsonrepo import JsonRepo
from army_builder.use_cases.unit_list import unit_list_use_case

FILE_STORE = "./data_store/units.json"

repo = JsonRepo(FILE_STORE)
result = unit_list_use_case(repo)

for unit in result:
    print(unit.to_dict())
