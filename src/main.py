
import logging

from src.passwordless import PasswordlessOptions, PasswordlessApiClientBuilder, UserSummary, CreateAlias, \
    UpdateAppsFeature


def main():
    print("Hello World!")


if __name__ == "__main__":
    logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

    options = PasswordlessOptions('API', 'SECRET')
    client = PasswordlessApiClientBuilder(options).build()

    logging.debug('Users: %s', client.get_users())
    client.create_alias(CreateAlias('8b1c30ab-4446-4c8c-a0cc-210153b9b445', aliases=['Maciej']))
    logging.debug('Aliases: %s', client.get_aliases('8b1c30ab-4446-4c8c-a0cc-210153b9b445'))
    client.update_apps_feature(UpdateAppsFeature(10))
