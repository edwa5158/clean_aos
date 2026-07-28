#!/usr/bin/env -S uv run python
from army_builder.repository.jsonrepo import JsonRepo
from army_builder.use_cases.warscroll_list import warscroll_list_use_case

FILE_STORE = "./data_store/warscrolls.json"

repo = JsonRepo(FILE_STORE)
result = warscroll_list_use_case(repo)

for unit in result:
    print(unit.to_dict())
