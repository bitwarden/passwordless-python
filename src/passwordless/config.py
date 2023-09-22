
class PasswordlessOptions:
    def __init__(self, api_private_key: str):
        self.__init__('https://v4.passwordless.dev', api_private_key)

    def __init__(self, api_url: str, api_private_key: str):
        self.api_url = api_url
        self.api_private_key = api_private_key
