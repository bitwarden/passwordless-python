from passwordless.config import PasswordlessOptions

SECRET = "my_secret"
DEFAULT_URL = "https://v4.passwordless.dev"


def test_init_no_api_url_provided() -> None:
    passwordless_options = PasswordlessOptions(SECRET)
    assert passwordless_options.api_secret == SECRET
    assert passwordless_options.api_url == DEFAULT_URL


def test_init_custom_api_url_provided() -> None:
    passwordless_options = PasswordlessOptions(SECRET, "http://localhost:8123")
    assert passwordless_options.api_secret == SECRET
    assert passwordless_options.api_url == "http://localhost:8123"
