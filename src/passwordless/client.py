import logging
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from requests import Request, Response, Session

from .config import PasswordlessOptions
from .errors import PasswordlessError, PasswordlessProblemDetails
from .models import (
    Alias,
    Credential,
    DeleteCredential,
    DeleteUser,
    GenerateAuthenticationTokenOptions,
    GeneratedAuthenticationToken,
    ListResponse,
    RegisteredToken,
    RegisterToken,
    SendMagicLinkOptions,
    SetAlias,
    UpdateAppsFeature,
    UserSummary,
    VerifiedUser,
    VerifySignIn,
)
from .serialization import (
    AliasListResponseSchema,
    CredentialListResponseSchema,
    DeleteCredentialSchema,
    DeleteUserSchema,
    GenerateAuthenticationTokenOptionsSchema,
    GeneratedAuthenticationTokenSchema,
    PasswordlessProblemDetailsSchema,
    RegisteredTokenSchema,
    RegisterTokenSchema,
    SendMagicLinkOptionsSchema,
    SetAliasSchema,
    UpdateAppsFeatureSchema,
    UserSummaryListResponseSchema,
    VerifiedUserSchema,
    VerifySignInSchema,
)


class PasswordlessClient:
    """Provides APIs that help you interact with Passwordless.dev.

    Create new instance of the client with `PasswordlessClientBuilder`.
    """

    @abstractmethod
    def set_alias(self, create_alias: SetAlias) -> None:
        """Creates or replaces existing aliases for a given user.

        :param create_alias: `SetAlias` containing details about the aliases
            for a user.
        :raises PasswordlessError: If the Passwordless Api responds with
            an error.
        """
        pass

    @abstractmethod
    def get_aliases(self, user_id: str) -> List[Alias]:
        """List all aliases for a given user.

        :param user_id: The userId of the user for which the aliases
            will be returned.
        :return: List of aliases
        :raises PasswordlessError: If the Passwordless Api responds with
            an error.
        """
        pass

    @abstractmethod
    def update_apps_feature(
        self, update_apps_feature: UpdateAppsFeature
    ) -> None:
        """Updates application features for the account associated with
        your ApiSecret.

        :param update_apps_feature: `UpdateAppsFeature` containing details
            about the updatable features for an application.
        :raises PasswordlessError: If the Passwordless Api responds with
            an error.
        """
        pass

    @abstractmethod
    def delete_credential(self, delete_credential: DeleteCredential) -> None:
        """Attempts to delete a credential.

        :param delete_credential: `DeleteCredential` containing details
            about the credential id to be deleted.
        :raises PasswordlessError: If the Passwordless Api responds with
            an error.
        """
        pass

    @abstractmethod
    def get_credentials(self, user_id: str) -> List[Credential]:
        """List all credentials for a given user.

        :param user_id: The userId of the user for which the credentials
            will be returned.
        :return: List of credentials
        :raises PasswordlessError: If the Passwordless Api responds with
            an error.
        """
        pass

    @abstractmethod
    def register_token(self, register_token: RegisterToken) -> RegisteredToken:
        """Creates a register token which will be used by your frontend
        to negotiate the creation of a WebAuth credential.

        :param register_token: `RegisterToken` containing details about
            the registration of the token.
        :return: Registered token
        :raises PasswordlessError: If the Passwordless Api responds with
            an error.
        """
        pass

    @abstractmethod
    def sign_in(self, verify_sign_in: VerifySignIn) -> VerifiedUser:
        """Verifies that the given token is valid and returns
        information packed into it. The token should have been generated
        via calling a `signInWith` method from your frontend code.

        :param verify_sign_in: `VerifySignIn` containing details about the
            token to verify.
        :return: User token details upon successful verification of the
            token.
        :raises PasswordlessError: If the Passwordless Api responds with
            an error.
        """
        pass

    @abstractmethod
    def get_users(self) -> List[UserSummary[Any]]:
        """List all users for the account associated with your
        ApiSecret.

        :return: List of user summaries.
        :raises PasswordlessError: If the Passwordless Api responds with
            an error.
        """
        pass

    @abstractmethod
    def delete_user(self, delete_user: DeleteUser) -> None:
        """Deletes a user.

        :param delete_user: `DeleteUser` containing details about the user
            to delete.
        :raises PasswordlessError: If the Passwordless Api responds with
            an error.
        """
        pass

    @abstractmethod
    def send_magic_link(self, options: SendMagicLinkOptions) -> None:
        """Sends a magic link.

        :param options: `SendMagicLinkOptions` containing details about the
            magic link to send.
        :raises PasswordlessError: If the Passwordless Api responds with
            an error.
        """
        pass

    @abstractmethod
    def generate_authentication_token(
        self, options: GenerateAuthenticationTokenOptions
    ) -> GeneratedAuthenticationToken:
        """Can be used to implement a "magic link"-style login and other
        similar scenarios.

        :param options: The options to generate an authentication token.
        :return: User token details upon successful generation of the
            token.
        :raises PasswordlessError: If the Passwordless Api responds with
            an error.
        """
        pass


def handle_response_error(response: Response) -> None:
    problem_details = None
    if "Content-Type" in response.headers and response.headers[
        "Content-Type"
    ].startswith("application/problem+json"):
        problem_details_schema = PasswordlessProblemDetailsSchema()
        problem_details = problem_details_schema.loads(response.text)

    if problem_details is None:
        logging.debug("Problem details fallback")

        problem_details = PasswordlessProblemDetails(
            type="https://docs.passwordless.dev/guide/errors.html",
            status=response.status_code,
            title="Unexpected error",
            detail=response.text,
        )

    logging.debug("Problem details %s", problem_details)

    raise PasswordlessError(problem_details)


class PasswordlessClientImpl(PasswordlessClient, ABC):
    def __init__(self, options: PasswordlessOptions, session: Session):
        self.options = options
        self.session = session

    def set_alias(self, create_alias: SetAlias) -> None:
        schema = SetAliasSchema()
        request_data = schema.dumps(create_alias)

        request = self.__build_post_request("/alias", request_data)

        self.__send_request(request)

    def get_aliases(self, user_id: str) -> List[Alias]:
        request = self.__build_get_request("/alias/list", {"userId": user_id})
        response = self.__send_request(request)

        schema = AliasListResponseSchema()
        list_response: ListResponse[Alias] = schema.loads(response.text)

        return list_response.values

    def update_apps_feature(
        self, update_apps_feature: UpdateAppsFeature
    ) -> None:
        schema = UpdateAppsFeatureSchema()
        request_data = schema.dumps(update_apps_feature)

        request = self.__build_post_request("/apps/features", request_data)

        self.__send_request(request)

    def delete_credential(self, delete_credential: DeleteCredential) -> None:
        schema = DeleteCredentialSchema()
        request_data = schema.dumps(delete_credential)

        request = self.__build_post_request(
            "/credentials/delete", request_data
        )

        self.__send_request(request)

    def get_credentials(self, user_id: str) -> List[Credential]:
        request = self.__build_get_request(
            "/credentials/list", {"userId": user_id}
        )
        response = self.__send_request(request)

        schema = CredentialListResponseSchema()
        list_response: ListResponse[Credential] = schema.loads(response.text)

        return list_response.values

    def register_token(self, register_token: RegisterToken) -> RegisteredToken:
        request_schema = RegisterTokenSchema()
        request_data = request_schema.dumps(register_token)

        request = self.__build_post_request("/register/token", request_data)

        response = self.__send_request(request)

        response_schema = RegisteredTokenSchema()
        registered_token: RegisteredToken = response_schema.loads(
            response.text
        )
        return registered_token

    def sign_in(self, verify_sign_in: VerifySignIn) -> VerifiedUser:
        request_schema = VerifySignInSchema()
        request_data = request_schema.dumps(verify_sign_in)

        request = self.__build_post_request("/signin/verify", request_data)

        response = self.__send_request(request)

        response_schema = VerifiedUserSchema()
        verified_user: VerifiedUser = response_schema.loads(response.text)
        return verified_user

    def get_users(self) -> List[UserSummary[Any]]:
        request = self.__build_get_request("/users/list")
        response = self.__send_request(request)

        schema = UserSummaryListResponseSchema()
        list_response: ListResponse[UserSummary[Any]] = schema.loads(
            response.text
        )

        return list_response.values

    def delete_user(self, delete_user: DeleteUser) -> None:
        schema = DeleteUserSchema()
        request_data = schema.dumps(delete_user)

        request = self.__build_post_request("/users/delete", request_data)

        self.__send_request(request)

    def send_magic_link(self, options: SendMagicLinkOptions) -> None:
        request_schema = SendMagicLinkOptionsSchema()
        request_data = request_schema.dumps(options)

        request = self.__build_post_request("/magic-links/send", request_data)

        self.__send_request(request)

    def generate_authentication_token(
        self, options: GenerateAuthenticationTokenOptions
    ) -> GeneratedAuthenticationToken:
        schema = GenerateAuthenticationTokenOptionsSchema()
        request_data = schema.dumps(options)

        request = self.__build_post_request(
            "/signin/generate-token", request_data
        )

        response = self.__send_request(request)

        response_schema = GeneratedAuthenticationTokenSchema()
        response_data: GeneratedAuthenticationToken = response_schema.loads(
            response.text
        )

        return response_data

    def __build_get_request(
        self,
        path: str,
        query_params: Optional[Dict[str, str]] = None,
    ) -> Request:
        if query_params is None:
            query_params = {}

        url = self.__build_url(path)
        headers = self.__build_headers()

        return Request(
            method="GET", url=url, headers=headers, params=query_params
        )

    def __build_post_request(self, path: str, data: str) -> Request:
        url = self.__build_url(path)
        headers = self.__build_headers(post=True)

        return Request(method="POST", url=url, headers=headers, data=data)

    def __send_request(self, request: Request) -> Response:
        logging.debug(
            "Sending request method %s url %s headers %s params %s data %s",
            request.method,
            request.url,
            request.headers,
            request.params,
            request.data,
        )

        prepped_request = self.session.prepare_request(request)

        response = self.session.send(
            prepped_request, allow_redirects=True, timeout=30
        )

        logging.debug(
            "Response code %s headers %s data %s",
            response.status_code,
            response.headers,
            response.text,
        )

        if response.status_code >= 400:
            handle_response_error(response)

        return response

    def __build_url(self, path: str) -> str:
        return self.options.api_url + path

    def __build_headers(self, post: bool = False) -> Dict[str, str]:
        headers = {"ApiSecret": self.options.api_secret}
        if post:
            headers["Content-Type"] = "application/json; charset=UTF-8"
        return headers


class PasswordlessClientBuilder:
    """The `PasswordlessClient` builder, which provides APIs that help
    you interact with Passwordless.dev.

    Example::

        passwordless_options = PasswordlessOptions(api_secret='...')
        client = PasswordlessClientBuilder(passwordless_options).build()
    """

    def __init__(
        self,
        options: PasswordlessOptions,
        session: Optional[Session] = None,
    ):
        """Creates the builder for given passwordless configuration
        options.

        :param options: Configuration options for Passwordless Api.
        :param session: (Optional) Configures with custom `requests.Session`.
        """
        self.options = options
        if session is None:
            session = Session()
        self.session = session

    def build(self) -> PasswordlessClient:
        """Builds the Passwordless client.

        :return: The `PasswordlessClient` object.
        """
        return PasswordlessClientImpl(self.options, self.session)
