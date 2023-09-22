# Passwordless Java SDK

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

Customize `PasswordlessOptions` by providing `apiPrivateKey` with your Application's Private API Key.
You can also change the `apiUrl` if you prefer to self-host.

Customize `PasswordlessClientBuilder` by providing `session` [requests Session][requests] instance.

### Examples

See [Passwordless Python Example](https://github.com/passwordless/passwordless-python-example) for Flash Web application
using this library.

## Documentation

For a comprehensive list of examples, check out the [API
documentation][api-docs].

## Contributing

This library is compatible with Python 3 and requires minimum Python 3.7 installed.

Setup venv:
```shell
python3 -m venv env
source env/bin/activate
```

Install dependencies:

```shell
python3 -m pip install flit flake8 wemake-python-styleguide
```

Build with flit: 
```shell
python3 -m flit build
```

[api-docs]:https://docs.passwordless.dev/guide/get-started.html

[requests]:https://requests.readthedocs.io/en/latest/

[marshmallow]:https://marshmallow.readthedocs.io/en/stable/
