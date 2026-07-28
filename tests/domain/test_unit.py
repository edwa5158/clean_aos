import uuid

from army_builder.domain.warscroll import Warscroll


def test_warscroll_model_init():
    code = uuid.uuid4()
    warscroll = Warscroll(code=code, name="test_warscroll", is_hero=False)

    assert warscroll.code == code
    assert warscroll.name == "test_warscroll"
    assert warscroll.is_hero is False


def test_warscroll_model_from_dict():
    code = uuid.uuid4()
    init_dict = {
        "code": code,
        "name": "test_warscroll",
        "is_hero": False,
    }

    warscroll = Warscroll.from_dict(init_dict)
    assert warscroll.code == code
    assert warscroll.name == "test_warscroll"
    assert warscroll.is_hero is False


def test_warscroll_mode_to_dict():
    code = uuid.uuid4()
    init_dict = {
        "code": code,
        "name": "test_warscroll",
        "is_hero": False,
    }

    warscroll = Warscroll.from_dict(init_dict)
    assert warscroll.to_dict() == init_dict


def test_warscroll_model_equality():
    code = uuid.uuid4()
    init_dict = {
        "code": code,
        "name": "test_warscroll",
        "is_hero": False,
    }

    warscroll1 = Warscroll.from_dict(init_dict)
    warscroll2 = Warscroll.from_dict(init_dict)

    assert warscroll1 == warscroll2
