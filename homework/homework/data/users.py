import requests
from homework.settings import API_BASE_URL
from homework.models.users import UserLoginModel


class UserApiCalls:
    def login_user(user: UserLoginModel):
        client = requests.session()
        url = f"{API_BASE_URL}/api/users/login"
        print(user.email)
        print(user.password)
        print(url)
        data = {
            "email": user.email,
            "password": user.password,
        }
        response = client.post(url, json=data, headers={"accept": "*/*"})
        print(response.status_code, response.content)

        return response
