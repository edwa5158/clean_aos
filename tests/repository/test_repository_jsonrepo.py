import json

import pytest

from army_builder.domain.warscroll import Warscroll
from army_builder.repository.jsonrepo import JsonRepo


@pytest.fixture
def warscroll_dicts() -> list[dict]:
    return [
        {
            "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
            "name": "Clanrats",
            "is_hero": False,
        },
        {
            "code": "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a",
            "name": "Grey Seer",
            "is_hero": True,
        },
        {
            "code": "913694c6-435a-4366-ba0d-da5334a611b2",
            "name": "Grey Seer on Screaming Bell",
            "is_hero": True,
        },
        {
            "code": "eed76e77-55c1-41ce-985d-ca49bf6c0585",
            "name": "Rat Ogors",
            "is_hero": False,
        },
    ]


@pytest.fixture
def create_scratch_file(tmp_path, warscroll_dicts):
    target = tmp_path / "example.json"

    with open(target, "w", encoding="utf-8") as f:
        json.dump(warscroll_dicts, f, indent=4)

    assert target.exists()
    return target


def test_json_repository_list_without_parameters(create_scratch_file, warscroll_dicts):
    repo = JsonRepo(create_scratch_file)
    warscrolls = [Warscroll.from_dict(dict) for dict in warscroll_dicts]

    assert repo.list() == warscrolls


@pytest.mark.skip(reason="`test_json_repository_with_missing_file` behaviour undecided")
def test_json_repository_with_missing_file():
    pass


@pytest.mark.skip(reason="`test_json_repository_with_invalid_json` behaviour undecided")
def test_json_repository_with_invalid_json():
    pass
