from passwordless import (
    PasswordlessClientBuilder,
    PasswordlessOptions,
    PasswordlessProblemDetails,
    PasswordlessProblemDetailsSchema,
)
from pytest_httpserver import HTTPServer
from werkzeug import Response

from .data_factory import SECRET, build_passwordless_options


def build_passwordless_options_http_server(
    httpserver: HTTPServer,
) -> PasswordlessOptions:
    url = httpserver.url_for("/")
    return build_passwordless_options(url)


def build_get_headers() -> dict:
    return {"ApiSecret": SECRET}


def build_post_headers() -> dict:
    return {
        "ApiSecret": SECRET,
        "Content-Type": "application/json; charset=UTF-8",
    }


def build_problem_details_response(
    problem_details: PasswordlessProblemDetails,
):
    schema = PasswordlessProblemDetailsSchema()
    return Response(
        response=schema.dumps(problem_details),
        status=problem_details.status,
        headers={"Content-Type": "application/problem+json; charset=UTF-8"},
    )


def build_passwordless_client(httpserver: HTTPServer):
    passwordless_options = build_passwordless_options_http_server(httpserver)

    builder = PasswordlessClientBuilder(passwordless_options)
    return builder.build()
