import requests

from homework.models.users import UserLoginModel
from homework.settings import API_BASE_URL


class UserApiCalls:
    def login_user(user: UserLoginModel):
        client = requests.session()
        url = f"{API_BASE_URL}/api/users/login"
        data = {
            "email": user.email,
            "password": user.password,
        }
        response = client.post(url, json=data, headers={"accept": "*/*"})
        print(response.status_code, response.content)

        return response
