import gettext as gt
import random
import flet
from flet import (
    Page,
    RadioGroup,
    Text,
    View,
    Column,
    Container,
    alignment,
    border_radius,
    json,
    padding,
    Row,
    Card,
    TextField,
    FilledButton,
    SnackBar,
)

from datetime import datetime
from flet.radio import Radio

import requests
from views.register_view import PageViews as pgvs
from services.register import RegisterService


def main(page: Page):
    page.title = "Routes Example"
    snack = SnackBar(
        Text("Registration successfull!"),
    )

    def req_healthcheck(e):
        client = requests.session()

        # Define the endpoint URL
        url = "http://127.0.0.1:8000/api/healthcheck"

        headers = {"accept": "*/*"}

        response = client.get(url, headers=headers)

        if response.status_code == 200:

            page.views.append(
                View(
                    f"/{response.status_code}",
                    horizontal_alignment="center",
                    vertical_alignment="center",
                    controls=[
                        Column(
                            alignment="center",
                            horizontal_alignment="center",
                            controls=[
                                Text(
                                    "response was 200!",
                                    size=44,
                                    weight="w700",
                                    text_align="center",
                                ),
                                Text(
                                    # We can show the user info by using the string
                                    f"Health Check  {response.json()}",
                                    size=32,
                                    weight="w500",
                                    text_align="center",
                                ),
                            ],
                        ),
                    ],
                )
            )

        else:
            snack.content.value = f"Health check response was {response.status_code}."
            snack.open = True
            page.update()

        page.update()

    def req_register(
        e,
        email,
        password,
        first_name,
        last_name_1,
        last_name_2,
        is_learner,
        is_guardian,
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
            "description": description,
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

        print(response.content)

        if response.status_code == 201:
            snack.content.value = "You are registered! Check your email."
            snack.open = True
            page.update()

        else:
            snack.content.value = f"The response was {response.status_code}, {response.content}  Try again."
            snack.open = True
            page.update()

    def req_login(e, email, password):
        data = {
            "email": email,
            "password": password,
        }
        client = requests.session()
        # Define the endpoint URL
        url = "http://127.0.0.1:8000/api/users/login"

        response = client.post(url, json=data, headers={"accept": "*/*"})

        if response.status_code == 200:

            page.views.append(
                View(
                    f"/{email}",
                    horizontal_alignment="center",
                    vertical_alignment="center",
                    controls=[
                        Column(
                            alignment="center",
                            horizontal_alignment="center",
                            controls=[
                                Text(
                                    "Succssesfuly Logged in!",
                                    size=44,
                                    weight="w700",
                                    text_align="center",
                                ),
                                Text(
                                    # We can show the user info by using the string
                                    f"Login Information:\nEmail: {email}",
                                    size=32,
                                    weight="w500",
                                    text_align="center",
                                ),
                            ],
                        ),
                    ],
                )
            )

        else:
            snack.content.value = (
                f"Could not log in! response was {response.status_code}."
            )
            snack.open = True
            page.update()

        page.update()

    def route_change(route):
        email = TextField(
            label="Email",
            border="underline",
            width=320,
            text_size=14,
        )
        first_name = TextField(
            label="First name",
            border="underline",
            width=320,
            text_size=14,
        )

        last_name_1 = TextField(
            label="Last Name 1",
            border="underline",
            width=320,
            text_size=14,
        )
        last_name_2 = TextField(
            label="Last name 2",
            border="underline",
            width=320,
            text_size=14,
        )
        account_type = RadioGroup(
            content=Row(
                [
                    Radio(value="is_learner", label="Student"),
                    Radio(value="is_guardian", label="Guardian"),
                ]
            )
        )
        password = TextField(
            label="Password",
            border="underline",
            width=320,
            text_size=14,
            password=True,
            can_reveal_password=True,
        )

        page.views.clear()
        """ we will be working with views, each 'page' will be a seperate view, i..e login page, reg page, etc..

        """

        # start with the registration page
        page.views.append(
            pgvs.register_view(
                page,
                email,
                first_name,
                password,
                last_name_1,
                last_name_2,
                account_type,
                snack,
            )
        )

        if page.route == "/login":
            page.views.append(
                View(
                    "/login",
                    horizontal_alignment="center",
                    vertical_alignment="center",
                    controls=[
                        Column(
                            alignment="center",
                            controls=[
                                Card(
                                    elevation=15,
                                    content=Container(
                                        width=550,
                                        height=550,
                                        padding=padding.all(30),
                                        border_radius=border_radius.all(12),
                                        content=Column(
                                            horizontal_alignment="center",
                                            alignment="start",
                                            controls=[
                                                Text(
                                                    "Homework Helper",
                                                    size=32,
                                                    weight="w700",
                                                    text_align="center",
                                                ),
                                                Container(
                                                    padding=padding.only(bottom=20)
                                                ),
                                                email,
                                                Container(
                                                    padding=padding.only(bottom=10)
                                                ),
                                                password,
                                                Container(
                                                    padding=padding.only(bottom=20)
                                                ),
                                                Row(
                                                    alignment="center",
                                                    spacing=20,
                                                    controls=[
                                                        FilledButton(
                                                            content=Text(
                                                                "Login",
                                                                weight="w700",
                                                            ),
                                                            width=160,
                                                            height=40,
                                                            # Now, if we want to login, we also need to send some info back to the server and check if the credentials are correct or if they even exists.
                                                            on_click=lambda e: req_login(
                                                                e,
                                                                email.value,
                                                                password.value,
                                                            ),
                                                        ),
                                                        FilledButton(
                                                            content=Text(
                                                                "healthcheck",
                                                                weight="w700",
                                                            ),
                                                            width=160,
                                                            height=40,
                                                            on_click=lambda e: req_healthcheck(
                                                                e,
                                                            ),
                                                        ),
                                                        snack,
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ),
                                )
                            ],
                        )
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


flet.app(target=main, host="localhost", port=9999, view=flet.WEB_BROWSER)
