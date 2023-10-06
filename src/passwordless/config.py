class PasswordlessOptions:
    def __init__(
        self, api_secret: str, api_url: str = "https://v4.passwordless.dev"
    ):
        self.api_url = api_url
        self.api_secret = api_secret
