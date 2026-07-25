import uuid

from army_builder.domain.unit import Unit


def test_unit_model_init():
    code = uuid.uuid4()
    unit = Unit(code=code, name="test_unit", is_hero=False, is_general=False)

    assert unit.code == code
    assert unit.name == "test_unit"
    assert unit.is_hero is False
    assert unit.is_general is False


def test_unit_model_from_dict():
    code = uuid.uuid4()
    init_dict = {
        "code": code,
        "name": "test_unit",
        "is_hero": False,
        "is_general": False,
    }

    unit = Unit.from_dict(init_dict)
    assert unit.code == code
    assert unit.name == "test_unit"
    assert unit.is_hero is False
    assert unit.is_general is False


def test_unit_mode_to_dict():
    code = uuid.uuid4()
    init_dict = {
        "code": code,
        "name": "test_unit",
        "is_hero": False,
        "is_general": False,
    }

    unit = Unit.from_dict(init_dict)
    assert unit.to_dict() == init_dict


def test_unit_model_equality():
    code = uuid.uuid4()
    init_dict = {
        "code": code,
        "name": "test_unit",
        "is_hero": False,
        "is_general": False,
    }

    unit1 = Unit.from_dict(init_dict)
    unit2 = Unit.from_dict(init_dict)

    assert unit1 == unit2
