# Passwordless Python SDK Example

Please read the documentation here: https://docs.passwordless.dev

## Getting Started

This example uses *StreamLit* and provides UI to interact with
the [Passwordless Python SDK][passwordless-python-sdk] to the *Passwordless API*.

Python 3.8 or newer is required to run the application.
For frontend, install Node.

Install [Poetry][poetry] if not already installed.

Activate shell: `poetry shell`

Install dependencies: `poetry install --with dev`

1. Get your own API keys here: https://admin.passwordless.dev/signup
2. Change the value of the Key and Secret in [.streamlit/secrets.toml file](.streamlit/secrets.toml)
    - (optional) In case of self-hosting, change the value of the Url with the base url where your *Passwordless API*
      instance is running.
3. Build the application:
   ```
   cd passwordless_auth/frontend
   npm install
   npm run build
   ```
4. Start the application `poetry run streamlit run app.py`
5. The application will now listen on port `8501` e.g. http://localhost:8501, where you can *Sign In* and *Register*
   users within your Application.

[passwordless-python-sdk]:https://github.com/passwordless/passwordless-python

[poetry]:https://python-poetry.org/docs/#installation