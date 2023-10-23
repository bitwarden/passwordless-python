from flask import render_template

from .passwordless_api import api_bp
from .passwordless_bp import PasswordlessBlueprint

bp = PasswordlessBlueprint(
    "passwordless", __name__, url_prefix="/passwordless"
)

bp.register_blueprint(api_bp)


@bp.route("/")
def index():
    return render_template(
        "passwordless.html",
        passwordless_api_url=bp.api_config.url,
        passwordless_api_key=bp.api_config.key,
    )
