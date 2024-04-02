import pytest
from pytest_httpserver import HTTPServer
from werkzeug import Response

from passwordless import PasswordlessError
from passwordless.models import ListResponse
from passwordless.serialization import (
    AliasListResponseSchema,
    CredentialListResponseSchema,
    DeleteCredentialSchema,
    DeleteUserSchema,
    GenerateAuthenticationTokenOptionsSchema,
    GeneratedAuthenticationTokenSchema,
    RegisteredTokenSchema,
    RegisterTokenSchema,
    SendMagicLinkOptionsSchema,
    SetAliasSchema,
    UpdateAppsFeatureSchema,
    UserSummaryListResponseSchema,
    VerifiedUserSchema,
    VerifySignInSchema,
)

from .data_factory import (
    USER_ID,
    build_alias_1,
    build_alias_2,
    build_credential_1,
    build_credential_2,
    build_delete_credential,
    build_delete_user,
    build_generate_authentication_token_options,
    build_generated_authentication_token,
    build_passwordless_problem_details_invalid_token,
    build_register_token,
    build_registered_token,
    build_send_magic_link_options_1,
    build_send_magic_link_options_2,
    build_set_alias,
    build_update_apps_feature,
    build_user_summary_1,
    build_user_summary_2,
    build_verified_user,
    build_verify_sign_in,
)
from .http_utils import (
    build_get_headers,
    build_passwordless_client,
    build_post_headers,
    build_problem_details_response,
)


def test_set_alias_error_response_exception(httpserver: HTTPServer):
    problem_details = build_passwordless_problem_details_invalid_token()

    set_alias = build_set_alias()

    httpserver.expect_oneshot_request(
        "/alias",
        method="POST",
        headers=build_post_headers(),
    ).respond_with_response(build_problem_details_response(problem_details))

    client = build_passwordless_client(httpserver)

    with pytest.raises(PasswordlessError) as ex_info:
        client.set_alias(set_alias)
    assert ex_info.value.problem_details == problem_details


def test_set_alias_valid_request_no_error(httpserver: HTTPServer):
    request_schema = SetAliasSchema()

    set_alias = build_set_alias()

    httpserver.expect_oneshot_request(
        "/alias",
        method="POST",
        headers=build_post_headers(),
        data=request_schema.dumps(set_alias),
    ).respond_with_response(Response())

    set_alias = build_set_alias()

    client = build_passwordless_client(httpserver)

    client.set_alias(set_alias)


def test_get_aliases_error_response_exception(httpserver: HTTPServer):
    problem_details = build_passwordless_problem_details_invalid_token()

    httpserver.expect_oneshot_request(
        "/alias/list",
        method="GET",
        query_string={"userId": USER_ID},
        headers=build_get_headers(),
    ).respond_with_response(build_problem_details_response(problem_details))

    client = build_passwordless_client(httpserver)

    with pytest.raises(PasswordlessError) as ex_info:
        client.get_aliases(USER_ID)
    assert ex_info.value.problem_details == problem_details


def test_get_aliases_valid_request_no_error(httpserver: HTTPServer):
    alias_1 = build_alias_1()
    alias_2 = build_alias_2()

    response_schema = AliasListResponseSchema()

    httpserver.expect_oneshot_request(
        "/alias/list",
        method="GET",
        query_string={"userId": USER_ID},
        headers=build_get_headers(),
    ).respond_with_data(
        response_schema.dumps(ListResponse([alias_1, alias_2]))
    )

    client = build_passwordless_client(httpserver)

    aliases = client.get_aliases(USER_ID)

    assert alias_1, alias_2 in aliases
    assert len(aliases) == 2


def test_update_apps_features_error_response_exception(httpserver: HTTPServer):
    problem_details = build_passwordless_problem_details_invalid_token()

    update_apps_feature = build_update_apps_feature()

    httpserver.expect_oneshot_request(
        "/apps/features",
        method="POST",
        headers=build_post_headers(),
    ).respond_with_response(build_problem_details_response(problem_details))

    client = build_passwordless_client(httpserver)

    with pytest.raises(PasswordlessError) as ex_info:
        client.update_apps_feature(update_apps_feature)
    assert ex_info.value.problem_details == problem_details


def test_update_apps_features_valid_request_no_error(httpserver: HTTPServer):
    request_schema = UpdateAppsFeatureSchema()

    update_apps_feature = build_update_apps_feature()

    httpserver.expect_oneshot_request(
        "/apps/features",
        method="POST",
        headers=build_post_headers(),
        data=request_schema.dumps(update_apps_feature),
    ).respond_with_response(Response())

    client = build_passwordless_client(httpserver)

    client.update_apps_feature(update_apps_feature)


def test_delete_credential_error_response_exception(httpserver: HTTPServer):
    problem_details = build_passwordless_problem_details_invalid_token()

    delete_credential = build_delete_credential()

    httpserver.expect_oneshot_request(
        "/credentials/delete",
        method="POST",
        headers=build_post_headers(),
    ).respond_with_response(build_problem_details_response(problem_details))

    client = build_passwordless_client(httpserver)

    with pytest.raises(PasswordlessError) as ex_info:
        client.delete_credential(delete_credential)
    assert ex_info.value.problem_details == problem_details


def test_delete_credential_valid_request_no_error(httpserver: HTTPServer):
    request_schema = DeleteCredentialSchema()

    delete_credential = build_delete_credential()

    httpserver.expect_oneshot_request(
        "/credentials/delete",
        method="POST",
        headers=build_post_headers(),
        data=request_schema.dumps(delete_credential),
    ).respond_with_response(Response())

    client = build_passwordless_client(httpserver)

    client.delete_credential(delete_credential)


def test_get_credentials_error_response_exception(httpserver: HTTPServer):
    problem_details = build_passwordless_problem_details_invalid_token()

    httpserver.expect_oneshot_request(
        "/credentials/list",
        method="GET",
        query_string={"userId": USER_ID},
        headers=build_get_headers(),
    ).respond_with_response(build_problem_details_response(problem_details))

    client = build_passwordless_client(httpserver)

    with pytest.raises(PasswordlessError) as ex_info:
        client.get_credentials(USER_ID)
    assert ex_info.value.problem_details == problem_details


def test_get_credentials_valid_request_no_error(httpserver: HTTPServer):
    credential_1 = build_credential_1()
    credential_2 = build_credential_2()

    response_schema = CredentialListResponseSchema()

    httpserver.expect_oneshot_request(
        "/credentials/list",
        method="GET",
        query_string={"userId": USER_ID},
        headers=build_get_headers(),
    ).respond_with_data(
        response_schema.dumps(ListResponse([credential_1, credential_2]))
    )

    client = build_passwordless_client(httpserver)

    credentials = client.get_credentials(USER_ID)

    assert credential_1, credential_2 in credentials
    assert len(credentials) == 2


def test_register_token_error_response_exception(httpserver: HTTPServer):
    problem_details = build_passwordless_problem_details_invalid_token()

    register_token = build_register_token()

    httpserver.expect_oneshot_request(
        "/register/token",
        method="POST",
        headers=build_post_headers(),
    ).respond_with_response(build_problem_details_response(problem_details))

    client = build_passwordless_client(httpserver)

    with pytest.raises(PasswordlessError) as ex_info:
        client.register_token(register_token)
    assert ex_info.value.problem_details == problem_details


def test_register_token_valid_request_no_error(httpserver: HTTPServer):
    request_schema = RegisterTokenSchema()
    response_schema = RegisteredTokenSchema()

    register_token = build_register_token()
    expected_registered_token = build_registered_token()

    httpserver.expect_oneshot_request(
        "/register/token",
        method="POST",
        headers=build_post_headers(),
        data=request_schema.dumps(register_token),
    ).respond_with_data(response_schema.dumps(expected_registered_token))

    client = build_passwordless_client(httpserver)

    registered_token = client.register_token(register_token)

    assert registered_token == expected_registered_token


def test_sign_in_error_response_exception(httpserver: HTTPServer):
    problem_details = build_passwordless_problem_details_invalid_token()

    verify_sign_in = build_verify_sign_in()

    httpserver.expect_oneshot_request(
        "/signin/verify",
        method="POST",
        headers=build_post_headers(),
    ).respond_with_response(build_problem_details_response(problem_details))

    client = build_passwordless_client(httpserver)

    with pytest.raises(PasswordlessError) as ex_info:
        client.sign_in(verify_sign_in)
    assert ex_info.value.problem_details == problem_details


def test_sign_in_valid_request_no_error(httpserver: HTTPServer):
    request_schema = VerifySignInSchema()
    response_schema = VerifiedUserSchema()

    verify_sign_in = build_verify_sign_in()
    expected_verified_user = build_verified_user()

    httpserver.expect_oneshot_request(
        "/signin/verify",
        method="POST",
        headers=build_post_headers(),
        data=request_schema.dumps(verify_sign_in),
    ).respond_with_data(response_schema.dumps(expected_verified_user))

    client = build_passwordless_client(httpserver)

    verified_user = client.sign_in(verify_sign_in)

    assert verified_user == expected_verified_user


def test_get_users_error_response_exception(httpserver: HTTPServer):
    problem_details = build_passwordless_problem_details_invalid_token()

    httpserver.expect_oneshot_request(
        "/users/list",
        method="GET",
        headers=build_get_headers(),
    ).respond_with_response(build_problem_details_response(problem_details))

    client = build_passwordless_client(httpserver)

    with pytest.raises(PasswordlessError) as ex_info:
        client.get_users()
    assert ex_info.value.problem_details == problem_details


def test_get_users_valid_request_no_error(httpserver: HTTPServer):
    user_summary_1 = build_user_summary_1()
    user_summary_2 = build_user_summary_2()

    response_schema = UserSummaryListResponseSchema()

    httpserver.expect_oneshot_request(
        "/users/list",
        method="GET",
        headers=build_get_headers(),
    ).respond_with_data(
        response_schema.dumps(ListResponse([user_summary_1, user_summary_2]))
    )

    client = build_passwordless_client(httpserver)

    users = client.get_users()

    assert user_summary_1, user_summary_2 in users
    assert len(users) == 2


def test_delete_user_error_response_exception(httpserver: HTTPServer):
    problem_details = build_passwordless_problem_details_invalid_token()

    delete_user = build_delete_user()

    httpserver.expect_oneshot_request(
        "/users/delete",
        method="POST",
        headers=build_post_headers(),
    ).respond_with_response(build_problem_details_response(problem_details))

    client = build_passwordless_client(httpserver)

    with pytest.raises(PasswordlessError) as ex_info:
        client.delete_user(delete_user)
    assert ex_info.value.problem_details == problem_details


def test_delete_user_valid_request_no_error(httpserver: HTTPServer):
    request_schema = DeleteUserSchema()

    delete_user = build_delete_user()

    httpserver.expect_oneshot_request(
        "/users/delete",
        method="POST",
        headers=build_post_headers(),
        data=request_schema.dumps(delete_user),
    ).respond_with_response(Response())

    client = build_passwordless_client(httpserver)

    client.delete_user(delete_user)


def test_send_magic_link_error_response_exception(httpserver: HTTPServer):
    problem_details = build_passwordless_problem_details_invalid_token()

    send_magic_link_request = build_send_magic_link_options_1()

    httpserver.expect_oneshot_request(
        "/magic-links/send",
        method="POST",
        headers=build_post_headers(),
    ).respond_with_response(build_problem_details_response(problem_details))

    client = build_passwordless_client(httpserver)

    with pytest.raises(PasswordlessError) as ex_info:
        client.send_magic_link(send_magic_link_request)
    assert ex_info.value.problem_details == problem_details


def test_send_magic_link_valid_request_no_error_1(httpserver: HTTPServer):
    request_schema = SendMagicLinkOptionsSchema()

    options = build_send_magic_link_options_1()

    httpserver.expect_oneshot_request(
        "/magic-links/send",
        method="POST",
        headers=build_post_headers(),
        data=request_schema.dumps(options),
    ).respond_with_response(Response())

    client = build_passwordless_client(httpserver)

    client.send_magic_link(options)


def test_send_magic_link_valid_request_no_error_2(httpserver: HTTPServer):
    request_schema = SendMagicLinkOptionsSchema()

    options = build_send_magic_link_options_2()

    httpserver.expect_oneshot_request(
        "/magic-links/send",
        method="POST",
        headers=build_post_headers(),
        data=request_schema.dumps(options),
    ).respond_with_response(Response())

    client = build_passwordless_client(httpserver)

    client.send_magic_link(options)


def test_generate_authentication_token_in_error_response_exception(
    httpserver: HTTPServer,
):
    problem_details = build_passwordless_problem_details_invalid_token()

    options = build_generate_authentication_token_options()

    httpserver.expect_oneshot_request(
        "/signin/generate-token",
        method="POST",
        headers=build_post_headers(),
    ).respond_with_response(build_problem_details_response(problem_details))

    client = build_passwordless_client(httpserver)

    with pytest.raises(PasswordlessError) as ex_info:
        client.generate_authentication_token(options)
    assert ex_info.value.problem_details == problem_details


def test_generate_authentication_token_valid_request_no_error(
    httpserver: HTTPServer,
):
    request_schema = GenerateAuthenticationTokenOptionsSchema()
    response_schema = GeneratedAuthenticationTokenSchema()

    options = build_verify_sign_in()
    expected_generated_authentication_token = (
        build_generated_authentication_token()
    )

    httpserver.expect_oneshot_request(
        "/signin/generate-token",
        method="POST",
        headers=build_post_headers(),
        data=request_schema.dumps(options),
    ).respond_with_data(
        response_schema.dumps(expected_generated_authentication_token)
    )

    client = build_passwordless_client(httpserver)

    actual = client.generate_authentication_token(options)

    assert actual == expected_generated_authentication_token
