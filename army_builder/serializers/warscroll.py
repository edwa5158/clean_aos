import json

from army_builder.domain.warscroll import Warscroll


class WarscrollJsonEncoder(json.JSONEncoder):
    def default(self, o: Warscroll):
        try:
            to_serialize = o.to_dict()
            for key in ["code"]:
                to_serialize[key] = str(to_serialize[key])

            return to_serialize
        except AttributeError:
            return super().default(o)
