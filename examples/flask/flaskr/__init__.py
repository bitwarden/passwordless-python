import logging

from flasgger import Swagger
from flask_marshmallow import Marshmallow

from flask import Flask

from . import passwordless

logging.basicConfig(encoding="utf-8", level=logging.DEBUG)


def create_app():
    app = Flask(__name__, static_url_path="/")
    app.config.from_prefixed_env()
    app.debug = True

    Marshmallow(app)

    Swagger(
        app,
        template_file="passwordless_api.json",
        merge=True,
        config={
            "openapi": "3.0.1",
        },
    )

    with app.app_context():
        app.register_blueprint(passwordless.bp)
        app.add_url_rule("/", "index", passwordless.index)

    return app
