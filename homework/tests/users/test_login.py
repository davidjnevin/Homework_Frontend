from http import HTTPStatus

import pytest
import requests
from hamcrest import (assert_that, contains_string, empty, equal_to,
                      has_length, is_, is_not)
from homework.settings import API_BASE_URL


class TestLogin:
    def test_bad_credentials_login(self):
        # TODO add create user/ UserBuilder or mock for this test
        email = "content@davidjneivn.com"
        password = "aaa"

        bad_password = "bbb"
        assert_that(password, is_not(equal_to(bad_password)))

        client = requests.session()
        url = f"{API_BASE_URL}/api/users/login"
        data = {
            "email": email,
            "password": password,
        }
        response = client.post(url, json=data, headers={"accept": "*/*"})

        assert_that(response.status_code, equal_to(HTTPStatus.UNAUTHORIZED))

    def test_succesful_login(self):
        # TODO add create user/ UserBuilder or mock for this test

        email = "content@davidjnevin.com"
        password = "Password10!"

        client = requests.session()
        url = f"{API_BASE_URL}/api/users/login"
        data = {
            "email": email,
            "password": password,
        }
        assert_that(client.cookies, empty())

        response = client.post(url, json=data, headers={"accept": "*/*"})

        assert_that(client.cookies, is_not(empty()))
        assert_that(response.status_code, equal_to(HTTPStatus.OK))

    def test_bad_connection(self):
        # TODO add create user/ UserBuilder or mock for this test

        email = "content@davidjnevin.com"
        password = "Password10!"

        client = requests.session()
        bad_url = "http://localhost/"
        data = {
            "email": email,
            "password": password,
        }
        assert_that(client.cookies, empty())
        with pytest.raises(Exception) as error:
            response = client.post(bad_url, json=data, headers={"accept": "*/*"})
        assert_that(str(error), contains_string("Failed to establish a new connection"))
