# Passwordless Python SDK Example

Please read the documentation here: https://docs.passwordless.dev

## Getting Started

This example uses *Flask* and provides UI and REST interfaces to interact with
the [Passwordless Python SDK][passwordless-python-sdk] to the *Passwordless API*.

Python 3.9 or newer is required to run the application.
Install [Poetry][poetry] if not already installed.

Install dependencies: `poetry install`

1. Get your own API keys here: https://admin.passwordless.dev/signup
2. Change the value of the `FLASK_PASSWORDLESS_API_KEY` and `FLASK_PASSWORDLESS_API_SECRET`
   in [.env file](.env.example) with your API Key and Secret and rename to `.env`
3. (optional) In case of self-hosting, change the value of the `FLASK_PASSWORDLESS_API_URL`
   with the base url where your *Passwordless API* instance is running.
4. Start the application `flask --app flaskr run --host=localhost`
5. The application will now listen on port `5000` e.g. http://localhost:5000, where you can *Sign In* and *Register*
   users within your Application. (
   1. *NOTE*: Be sure to navigate to http://localhost:5000, using http://127.0.0.1:5000 will lead 
      to a RPID mismatch and will fail to create/get credentials.
6. For all Passwordless API functionalities supported by Python SDK, navigate to http://localhost:5000/apidocs
7. See [Example Passwordless REST Api requests and responses](example-rest-requests/passwordless-api.http)

[passwordless-python-sdk]:https://github.com/passwordless/passwordless-python

[poetry]:https://python-poetry.org/docs/#installation