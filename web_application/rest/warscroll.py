import json

from flask import Blueprint, Response

from army_builder.repository.jsonrepo import JsonRepo
from army_builder.serializers.warscroll import WarscrollJsonEncoder
from army_builder.use_cases.warscroll_list import warscroll_list_use_case

blueprint = Blueprint("warscroll", __name__)

FILE_PATH = "./data_store/warscrolls.json"


@blueprint.route("/warscrolls", methods=["GET"])
def warscroll_list() -> Response:
    repo = JsonRepo(FILE_PATH)
    result = warscroll_list_use_case(repo)

    return Response(
        json.dumps(result, cls=WarscrollJsonEncoder),
        mimetype="application/json",
        status=200,
    )
