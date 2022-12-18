import os

from decouple import config


API_BASE_URL = config("API_BASE_URL", default="http://127.0.0.1:8000")  # No trailing /
PROJECT_NAME = config("PROJECT_NAME", default="Homework")
