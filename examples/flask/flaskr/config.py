from os import environ

from dotenv import load_dotenv

DEBUG = True

load_dotenv()

PASSWORDLESS_API_URL = environ.get("FLASK_PASSWORDLESS_API_URL")
PASSWORDLESS_API_KEY = environ.get("FLASK_PASSWORDLESS_API_KEY")
PASSWORDLESS_API_SECRET = environ.get("FLASK_PASSWORDLESS_API_SECRET")
