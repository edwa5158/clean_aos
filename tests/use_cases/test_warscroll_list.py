import uuid
from unittest import mock

import pytest

from army_builder.domain.warscroll import Warscroll
from army_builder.use_cases.warscroll_list import warscroll_list_use_case


@pytest.fixture
def domain_warscrolls():
    clanrats = Warscroll(code=uuid.uuid4(), name="Clanrats", is_hero=False)

    grey_seer = Warscroll(code=uuid.uuid4(), name="Grey Seer", is_hero=True)

    grey_seer_on_screaming_bell = Warscroll(
        code=uuid.uuid4(), name="Grey Seer on Screaming Bell", is_hero=True
    )

    rat_ogors = Warscroll(code=uuid.uuid4(), name="Rat Ogors", is_hero=False)

    return [clanrats, grey_seer, grey_seer_on_screaming_bell, rat_ogors]


def test_warscroll_list_without_parameters(domain_warscrolls):
    repo = mock.Mock()
    repo.list.return_value = domain_warscrolls

    result = warscroll_list_use_case(repo)

    repo.list.assert_called_with()
    assert result == domain_warscrolls
