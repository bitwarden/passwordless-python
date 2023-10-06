# Passwordless Python SDK

The official [Bitwarden Passwordless.dev](https://passwordless.dev/) Python library, for Python 3+.

## Installation

Install with `python -m pip install passwordless`.

### Dependencies

- [Requests][requests] for HTTP API
- [marshmallow][marshmallow] for JSON (de)serialization

## Getting Started

Follow the [Get started guide][api-docs].

[//]: # (TODO)

### Create `PasswordlessClient` instance:

```python
# TODO
```

### Register a passkey

```python
# TODO
```

### Verify user

```python
# TODO
```

### Customization

Customize `PasswordlessOptions` by providing `api_secret` with your Application's Api Secret.
You can also change the `api_url` if you prefer to self-host.

Customize `PasswordlessApiClientBuilder` by providing `session` [requests Session][requests] instance.

### Examples

See [Passwordless Python Example](https://github.com/passwordless/passwordless-python-example) for Flash Web application
using this library.

## Documentation

For a comprehensive list of examples, check out the [API
documentation][api-docs].

## Contributing

This library is compatible with Python 3 and requires minimum Python 3.8 installed.
[Poetry][poetry] needs to be installed too.

Activate shell: `poetry shell`

Install dependencies: `poetry install`

Build: `poetry build`

[api-docs]:https://docs.passwordless.dev/guide/get-started.html

[poetry]:https://python-poetry.org/docs/#installation

[requests]:https://requests.readthedocs.io/en/latest/

[marshmallow]:https://marshmallow.readthedocs.io/en/stable/
