import json
import uuid

from army_builder.domain.unit import Unit
from army_builder.serializers.unit import UnitJsonEncoder


def test_serialize_domain_unit():
    code = uuid.uuid4()
    unit = Unit(code=code, name="test_unit", is_hero=False, is_general=False)

    expected_json = f"""
    {{
            "code": "{code}",
            "name": "test_unit",
            "is_hero": false,
            "is_general": false
        }}
    """

    json_unit = json.dumps(unit, cls=UnitJsonEncoder)

    assert json.loads(json_unit) == json.loads(expected_json)
