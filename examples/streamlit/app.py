import streamlit as st

st.set_page_config(page_title="Passwordless StreamLit example")
st.title("Bitwarden Passwordless.dev - Python")

st.write(
    "[Documentation](https://docs.passwordless.dev) - [Get your API keys]("
    "https://admin.passwordless.dev/signup)"
)

if (
    "passwordless_api_key" not in st.secrets
    or "passwordless_api_secret" not in st.secrets
    or "passwordless_api_url" not in st.secrets
    or st.secrets["passwordless_api_key"] == ""
    or st.secrets["passwordless_api_secret"] == ""
    or st.secrets["passwordless_api_url"] == ""
):
    st.write(
        "To run this example you must first specify yor API Key "
        "and API Secret in _.streamlit/secrets.toml_ file."
    )

if "login_user" in st.session_state:
    st.write("## Logged in User: ", st.session_state.login_user)
else:
    st.write("## Sign in to your account or register new account")
