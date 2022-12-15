import requests
from datetime import datetime

from random import random


class RegisterService:
    # TODO change this to return values for redirect.
    def req_register(
        e,
        email,
        password,
        first_name,
        last_name_1,
        last_name_2,
        is_learner,
        is_guardian,
        snack,
        page,
    ):
        # we set the email and passord as a dict/json structure in order to pass it to the request

        client = requests.session()

        is_staff = False
        date_joined = datetime.now()
        random_int = random.randint(1, 1000)
        data = {
            "email": f"peter{random_int}@davidjnevin.com",
            "password": "Password10!",
            "first_name": first_name,
            "last_name_1": last_name_1,
            "last_name_2": last_name_2,
            "description": "",
            "is_learner": is_learner,
            "is_guardian": is_guardian,
            "is_staff": is_staff,
            "date_joined": "2022-10-28T23:23:23Z",
        }

        response = client.post(
            "http://127.0.0.1:8000/api/users/users",
            json=data,
            headers={"accept": "*/*"},
        )

        if response.status_code == 201:
            snack.content.value = "You are registered! Check your email."
            snack.open = True
            page.update()

        else:
            snack.content.value = f"The response was {response.status_code}, {response.content}  Try again."
            snack.open = True
            page.update()
