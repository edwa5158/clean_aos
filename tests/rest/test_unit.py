import json
from unittest import mock

import web_application.rest.unit as APP_UNIT
from army_builder.domain.unit import Unit

unit_dict = {
    "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
    "name": "Clanrats",
    "is_hero": False,
}

units = [Unit.from_dict(unit_dict)]


@mock.patch(f"{APP_UNIT.__name__}.unit_list_use_case")
def test_get(mock_use_case, client):
    mock_use_case.return_value = units

    http_response = client.get("/units")

    assert json.loads(http_response.data.decode("UTF-8")) == [unit_dict]
    mock_use_case.assert_called()
    assert http_response.status_code == 200
    assert http_response.mimetype == "application/json"
