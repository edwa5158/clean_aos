import json
import uuid

from army_builder.domain.warscroll import Warscroll
from army_builder.serializers.warscroll import WarscrollJsonEncoder


def test_serialize_domain_warscroll():
    code = uuid.uuid4()
    warscroll = Warscroll(code=code, name="test_warscroll", is_hero=False)

    expected_json = f"""
    {{
            "code": "{code}",
            "name": "test_warscroll",
            "is_hero": false
        }}
    """

    json_warscroll = json.dumps(warscroll, cls=WarscrollJsonEncoder)

    assert json.loads(json_warscroll) == json.loads(expected_json)
