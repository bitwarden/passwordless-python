import logging
import os

from src.passwordless import PasswordlessOptions, PasswordlessApiClientBuilder, CreateAlias, \
    UpdateAppsFeature, DeleteCredential, RegisterToken, VerifySignIn, DeleteUser


def main():
    print("Hello World!")


if __name__ == "__main__":
    logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

    apiUrl = os.environ['PASSWORDLESS_API_URL']
    apiSecret = os.environ['PASSWORDLESS_API_SECRET']

    options = PasswordlessOptions(apiUrl, apiSecret)
    client = PasswordlessApiClientBuilder(options).build()

    client.create_alias(CreateAlias('8b1c30ab-4446-4c8c-a0cc-210153b9b445', aliases=['Maciej']))
    logging.debug('Aliases: %s', client.get_aliases('8b1c30ab-4446-4c8c-a0cc-210153b9b445'))
    client.update_apps_feature(UpdateAppsFeature(10))
    client.delete_credential(DeleteCredential('123456'))
    logging.debug('Credentials: %s', client.get_credentials('8b1c30ab-4446-4c8c-a0cc-210153b9b445'))
    logging.debug('Registered token: %s', client.register_token(
        RegisterToken(user_id='8b1c30ab-4446-4c8c-a0cc-210153b9b445', username='Test', display_name='Test')))
    logging.debug('Sign In: %s', client.sign_in(VerifySignIn(token='verify_x')))
    logging.debug('Users: %s', client.get_users())
    client.delete_user(DeleteUser('8b1c30ab-4446-4c8c-a0cc-210153b9b445'))
