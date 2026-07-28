from flask import Flask

import web_application.config as APP_CONFIG
from web_application.rest import warscroll


def create_app(config_name: str) -> Flask:

    app = Flask(__name__)

    config_module = f"{APP_CONFIG.__name__}.{config_name.capitalize()}Config"

    app.config.from_object(config_module)

    app.register_blueprint(warscroll.blueprint)

    return app
