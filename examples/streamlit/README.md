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

### Preparing for production

1. Edit the `[browser]` section in the [config.toml](.streamlit%2Fconfig.toml) file:
    - Change `serverAddress` to your host name
    - Change `serverPort` to your port. For `https://` use 443.
2. To run the application with `https://` scheme:
    1. Put reverse proxy with SSL in front of the application.
    2. Provide the path to the certificate and key files, by modifying `sslCertFile` and `sslKeyFile` in the
       `[server]` section of the [config.toml](.streamlit%2Fconfig.toml) file

Note: WebAuthn will only work with `https://` scheme with a valid, trusted certificate.

[passwordless-python-sdk]:https://github.com/bitwarden/passwordless-python

[poetry]:https://python-poetry.org/docs/#installation