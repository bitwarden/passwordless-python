import uuid

import streamlit as st
from passwordless import (
    PasswordlessClientBuilder,
    PasswordlessOptions,
    RegisterToken,
    VerifySignIn,
)


def get_passwordless_client():
    options = PasswordlessOptions(api_url=st.secrets["passwordless_api_url"],
                                  api_secret=st.secrets["passwordless_api_secret"])
    return PasswordlessClientBuilder(options).build()


def register(username: str, alias: str):
    client = get_passwordless_client()

    register_token = RegisterToken(user_id=str(uuid.uuid4()),
                                   username=username,
                                   aliases=[alias] if alias != "" else [])
    print(register_token)

    registered_token = client.register_token(register_token)
    print(registered_token)

    return registered_token


def login(token: str):
    client = get_passwordless_client()

    verify_sign_in = VerifySignIn(token=token)
    print(verify_sign_in)

    verified_user = client.sign_in(verify_sign_in)
    print(verified_user)

    return verified_user
