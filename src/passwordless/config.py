class PasswordlessOptions:
    """Represents all the options you can use to configure a backend
    Passwordless system."""

    def __init__(
        self, api_secret: str, api_url: str = "https://v4.passwordless.dev"
    ):
        """Constructor.

        :param api_secret: Secret key used to authenticate with the
            Passwordless API.
        :param api_url: Url to use for Passwordless API operations.
        """
        self.api_url = api_url
        self.api_secret = api_secret
