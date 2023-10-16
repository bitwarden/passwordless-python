from flask import make_response, request
from flaskr.passwordless_bp import PasswordlessApiBlueprint

from passwordless import (
    AliasSchema,
    CredentialSchema,
    DeleteCredentialSchema,
    DeleteUserSchema,
    PasswordlessError,
    PasswordlessProblemDetailsSchema,
    RegisteredTokenSchema,
    RegisterTokenSchema,
    SetAliasSchema,
    UpdateAppsFeatureSchema,
    UserSummarySchema,
    VerifiedUserSchema,
    VerifySignInSchema,
)

api_bp = PasswordlessApiBlueprint(
    "passwordless-api", __name__, url_prefix="/api"
)


@api_bp.route("/login", methods=["POST"])
def login():
    request_data = VerifySignInSchema().load(request.get_json())

    response_data = api_bp.api_client.sign_in(request_data)

    return VerifiedUserSchema().dump(response_data)


@api_bp.route("/register", methods=["POST"])
def register():
    request_data = RegisterTokenSchema().load(request.get_json())

    response_data = api_bp.api_client.register_token(request_data)

    return RegisteredTokenSchema().dump(response_data)


@api_bp.errorhandler(PasswordlessError)
def handle_passwordless_exception(e: PasswordlessError):
    schema = PasswordlessProblemDetailsSchema()
    response = make_response()
    response.data = schema.dumps(e.problem_details)
    response.content_type = "application/json"
    return response


@api_bp.route("/alias", methods=["POST"])
def set_alias():
    request_data = SetAliasSchema().load(request.get_json())

    api_bp.api_client.set_alias(request_data)

    return ""


@api_bp.route("/alias/<user_id>", methods=["GET"])
def get_aliases(user_id: str):
    response_data = api_bp.api_client.get_aliases(user_id)

    return AliasSchema(many=True).dump(response_data)


@api_bp.route("/apps/feature", methods=["PUT"])
def set_apps_feature():
    request_data = UpdateAppsFeatureSchema().load(request.get_json())

    api_bp.api_client.update_apps_feature(request_data)

    return ""


@api_bp.route("/credentials/<user_id>", methods=["GET"])
def get_credentials(user_id: str):
    response_data = api_bp.api_client.get_credentials(user_id)

    return CredentialSchema(many=True).dump(response_data)


@api_bp.route("/credentials", methods=["DELETE"])
def delete_credentials():
    request_data = DeleteCredentialSchema().load(request.get_json())

    api_bp.api_client.delete_credential(request_data)

    return ""


@api_bp.route("/users", methods=["GET"])
def get_users():
    response_data = api_bp.api_client.get_users()

    return UserSummarySchema(many=True).dump(response_data)


@api_bp.route("/users", methods=["DELETE"])
def delete_users():
    request_data = DeleteUserSchema().load(request.get_json())

    api_bp.api_client.delete_user(request_data)

    return ""
