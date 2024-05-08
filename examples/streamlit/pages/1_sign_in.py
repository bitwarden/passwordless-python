import passwordless_api
import streamlit as st
from passwordless_auth import passwordless_auth_component

st.set_page_config(page_title="Sign In")
st.title("Sign In")

st.text_input("Alias", key="alias")

if st.button("Login"):
    if "auth_error" in st.session_state:
        del st.session_state.auth_error
    st.session_state.login_init = True

if "login_init" in st.session_state:
    auth_result = passwordless_auth_component(
        "passwordless_auth_login",
        {
            "api_url": st.secrets["passwordless_api_url"],
            "api_key": st.secrets["passwordless_api_key"],
            "type": "login",
            "alias": st.session_state.alias,
        },
    )
    print(auth_result)

    if auth_result is not None:

        if "token" in auth_result:
            st.session_state.login_user = passwordless_api.login(
                auth_result["token"]
            )
        else:
            st.session_state.auth_error = auth_result

        del st.session_state.login_init

if "login_user" in st.session_state:
    st.write("## User: ", st.session_state.login_user)

if "auth_error" in st.session_state:
    st.write("## Error: ", st.session_state.auth_error)
