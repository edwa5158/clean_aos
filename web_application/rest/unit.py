import json

from flask import Blueprint, Response

from army_builder.repository.jsonrepo import JsonRepo
from army_builder.serializers.unit import UnitJsonEncoder
from army_builder.use_cases.unit_list import unit_list_use_case

blueprint = Blueprint("unit", __name__)

FILE_PATH = "./data_store/units.json"


@blueprint.route("/units", methods=["GET"])
def unit_list():
    repo = JsonRepo(FILE_PATH)
    result = unit_list_use_case(repo)

    return Response(
        json.dumps(result, cls=UnitJsonEncoder), mimetype="application/json", status=200
    )
