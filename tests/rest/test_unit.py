import json
from unittest import mock

import web_application.rest.warscroll as APP_WARSCROLL
from army_builder.domain.warscroll import Warscroll

warscroll_dict = {
    "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
    "name": "Clanrats",
    "is_hero": False,
}

warscrolls = [Warscroll.from_dict(warscroll_dict)]


@mock.patch(f"{APP_WARSCROLL.__name__}.warscroll_list_use_case")
def test_get(mock_use_case, client):
    mock_use_case.return_value = warscrolls

    http_response = client.get("/warscrolls")

    assert json.loads(http_response.data.decode("UTF-8")) == [warscroll_dict]
    mock_use_case.assert_called()
    assert http_response.status_code == 200
    assert http_response.mimetype == "application/json"
