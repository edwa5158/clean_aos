import pytest

from army_builder.domain.warscroll import Warscroll
from army_builder.repository.memrepo import MemRepo


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


def test_repository_list_without_parameters(warscroll_dicts):
    repo = MemRepo(warscroll_dicts)
    warscrolls = [Warscroll.from_dict(dict) for dict in warscroll_dicts]

    assert repo.list() == warscrolls
