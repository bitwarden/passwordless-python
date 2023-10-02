class PasswordlessOptions:
    def __init__(self, api_secret: str):
        self.__init__('https://v4.passwordless.dev', api_secret)

    def __init__(self, api_url: str, api_secret: str):
        self.api_url = api_url
        self.api_secret = api_secret
