from passwordless import (
    PasswordlessClient,
    PasswordlessClientBuilder,
    PasswordlessOptions,
)

from flask import Blueprint, Flask

from .passwordless_api_config import PasswordlessApiConfig


class PasswordlessBlueprint(Blueprint):
    api_config: PasswordlessApiConfig

    def register(self, app: Flask, options: dict) -> None:
        self.api_config = PasswordlessApiConfig(
            app.config.get("PASSWORDLESS_API_URL"),
            app.config.get("PASSWORDLESS_API_KEY"),
            app.config.get("PASSWORDLESS_API_SECRET"),
        )

        super(PasswordlessBlueprint, self).register(app, options)


class PasswordlessApiBlueprint(PasswordlessBlueprint):
    api_client: PasswordlessClient

    def register(self, app: Flask, options: dict) -> None:
        super(PasswordlessApiBlueprint, self).register(app, options)

        passwordless_options = PasswordlessOptions(
            self.api_config.secret, self.api_config.url
        )

        self.api_client = PasswordlessClientBuilder(
            passwordless_options
        ).build()
