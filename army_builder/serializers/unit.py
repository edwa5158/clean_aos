import json

from army_builder.domain.unit import Unit


class UnitJsonEncoder(json.JSONEncoder):
    def default(self, o: Unit):
        try:
            to_serialize = o.to_dict()
            for key in ["code"]:
                to_serialize[key] = str(to_serialize[key])

            return to_serialize
        except AttributeError:
            return super().default(o)
