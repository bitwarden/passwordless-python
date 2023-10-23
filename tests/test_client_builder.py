import requests
from pytest_httpserver import HTTPServer
from werkzeug import Response

from passwordless import (
    DeleteCredential,
    PasswordlessClient,
    PasswordlessClientBuilder,
)

from .http_utils import (
    build_passwordless_options_http_server,
    build_post_headers,
)


def validate_delete_credential(
    httpserver: HTTPServer, client: PasswordlessClient
):
    httpserver.expect_oneshot_request(
        "/credentials/delete",
        method="POST",
        headers=build_post_headers(),
        json={"credentialId": "test_1"},
    ).respond_with_response(Response())

    client.delete_credential(DeleteCredential("test_1"))


def test_default_can_make_requests(httpserver: HTTPServer):
    passwordless_options = build_passwordless_options_http_server(httpserver)

    builder = PasswordlessClientBuilder(passwordless_options)
    client = builder.build()

    validate_delete_credential(httpserver, client)


def test_custom_session_can_make_requests(httpserver: HTTPServer):
    passwordless_options = build_passwordless_options_http_server(httpserver)

    responses = []

    def track_response(r, *args, **kwargs):
        responses.append(r)

    session = requests.Session()
    session.hooks["response"].append(track_response)
    builder = PasswordlessClientBuilder(passwordless_options, session)
    client = builder.build()

    validate_delete_credential(httpserver, client)

    assert len(responses) == 1
