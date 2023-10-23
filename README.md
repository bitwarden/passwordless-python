# Passwordless Python SDK

The official [Bitwarden Passwordless.dev](https://passwordless.dev/) Python library, for Python 3+.

## Installation

Install with `python -m pip install passwordless`.

### Dependencies

- [Requests][requests] for HTTP API
- [marshmallow][marshmallow] for JSON (de)serialization

## Getting Started

Follow the [Get started guide][api-docs].

### Create `PasswordlessClient` instance:

```python
from passwordless import (
    PasswordlessClient,
    PasswordlessClientBuilder,
    PasswordlessOptions,
)


class PasswordlessPythonSdkExample:
    client: PasswordlessClient

    def __init__(self):
        options = PasswordlessOptions("your_api_secret")

        self.client = PasswordlessClientBuilder(options).build()

```

### Register a passkey

```python
import uuid
from passwordless import PasswordlessClient, RegisterToken, RegisteredToken


class PasswordlessPythonSdkExample:
    client: PasswordlessClient

    def get_register_token(self, alias: str) -> str:
        # Get existing userid from session or create a new user.
        user_id = str(uuid.uuid4())

        # Options to give the Api
        register_token = RegisterToken(
            user_id=user_id,  # your user id
            username=alias,  # e.g. user email, is shown in browser ui
            aliases=[alias]  # Optional: Link this userid to an alias (e.g. email)
        )

        response: RegisteredToken = self.client.register_token(register_token)

        # return this token
        return response.token
```

### Verify user

```python
from passwordless import PasswordlessClient, VerifySignIn, VerifiedUser


class PasswordlessPythonSdkExample:
    client: PasswordlessClient

    def verify_sign_in_token(self, token: str) -> VerifiedUser:
        verify_sign_in = VerifySignIn(token)

        # Sign the user in, set a cookie, etc,
        return self.client.sign_in(verify_sign_in)
```

### Customization

Customize `PasswordlessOptions` by providing `api_secret` with your Application's Api Secret.
You can also change the `api_url` if you prefer to self-host.

Customize `PasswordlessClientBuilder` by providing `session` [requests Session][requests] instance.

### Examples

See [Passwordless Python Example](examples/flask) for Flash Web application.

## Documentation

For a comprehensive list of examples, check out the [API documentation][api-docs].

## Contributing

This library is compatible with Python 3 and requires minimum Python 3.8 installed.
Install [Poetry][poetry] if not already installed.

Activate shell: `poetry shell`

Install dependencies: `poetry install --with dev,test`

Build: `poetry build`

[api-docs]:https://docs.passwordless.dev/guide/get-started.html

[poetry]:https://python-poetry.org/docs/#installation

[requests]:https://requests.readthedocs.io/en/latest/

[marshmallow]:https://marshmallow.readthedocs.io/en/stable/
