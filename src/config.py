import os

SECRET_KEY = os.environ.get("SECRET_KEY", "SECRET_KEY")
APP_NAME = os.environ.get("APP_NAME", "currency_converter_api")
EXCHANGERATE_BASE_URL = os.environ.get("EXCHANGERATE_BASE_URL", "https://api.exchangerate.host")
