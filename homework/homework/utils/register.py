import requests
from datetime import datetime
from homework.models.users import UserInModel
from random import random
from homework.settings import API_BASE_URL

BASE_URL = API_BASE_URL


class RegisterService:
    # TODO change this to return values for redirect.
    def req_register(e, user_in: UserInModel):
        # we set the email and passord as a dict/json structure in order to pass it to the request

        client = requests.session()

        # temporary values for testing.
        random_int = random.randint(1, 1000)
        user_in.email = f"peter{random_int}@davidjnevin.com"
        user_in.password = "Password10!"
        user_in.date_joined = datetime.now()

        data = {
            "email": user_in.email,
            "password": user_in.password,
            "first_name": user_in.first_name,
            "last_name_1": user_in.last_name_1,
            "last_name_2": user_in.last_name_2,
            "description": user_in.description,
            "is_learner": user_in.is_learner,
            "is_guardian": user_in.is_guardian,
            "date_joined": user_in.date_joined.strftime("%Y-%m-%dT%H:%M:%SZ"),
        }

        response = client.post(
            f"{BASE_URL}/api/users/users",
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
