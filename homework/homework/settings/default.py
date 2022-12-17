import os

from decouple import config


API_BASE_URL = config("API_BASE_URL", default="127.0.0.1/")
PROJECT_NAME = config("PROJECT_NAME", default="Homework")
