import code
import pytest
import uuid
from unittest import mock

from army_builder.domain.unit import Unit
from army_builder.use_cases.unit_list import unit_list_use_case

@pytest.fixture
def domain_units():
    clanrats = Unit(
        code=uuid.uuid4(),
        name = "Clanrats",
        is_hero = False
    )

    grey_seer = Unit(
        code=uuid.uuid4(),
        name="Grey Seer",
        is_hero=True
    )

    grey_seer_on_screaming_bell = Unit(
        code=uuid.uuid4(),
        name = "Grey Seer on Screaming Bell",
        is_hero=True
    )

    rat_ogors = Unit(
        code=uuid.uuid4(),
        name = "Rat Ogors",
        is_hero=False
    )

    return[clanrats, grey_seer, grey_seer_on_screaming_bell, rat_ogors]

def test_unit_list_without_parameters(domain_units):
    repo = mock.Mock()
    repo.list.return_value = domain_units

    result = unit_list_use_case(repo)

    repo.list.assert_called_with()
    assert result == domain_units