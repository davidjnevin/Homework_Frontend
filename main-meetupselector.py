""" these are the modules needed"""
import flet
from flet import (
    Page,
    Text,
    View,
    Column,
    Container,
    LinearGradient,
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

import requests


def main(page: Page):
    page.title = "Routes Example"
    snack = SnackBar(
        Text("Registration successfull!"),
    )

    def GradientGenerator(start, end):
        ColorGradient = LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=[
                start,
                end,
            ],
        )

        return ColorGradient

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

    def req_login(e, email, password):
        data = {
            "email": email,
            "password": password,
        }
        client = requests.session()
        # Define the endpoint URL
        url = "http://127.0.0.1:8000/api/users/login"

        response = client.get(url)

        # todo How to get csrf token from api?

        response = client.post(
            url,
            json={"email": email, "password": password},
            # headers={"accept": "*/*", "X-CSRFToken": csrf_token},
        )

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
                                    f"Login Information:\nEmail: {email}\nPassword: {password}",
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
            snack.content.value = f"Could not log in! response was {response.status_code}, {response.content}."
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
            View(
                "/register",
                horizontal_alignment="end",
                vertical_alignment="center",
                padding=padding.only(right=160),
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
                                    gradient=GradientGenerator("#000000", "#111111"),
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
                                            Container(padding=padding.only(bottom=20)),
                                            email,
                                            Container(padding=padding.only(bottom=10)),
                                            password,
                                            Container(padding=padding.only(bottom=20)),
                                            Row(
                                                alignment="center",
                                                spacing=20,
                                                controls=[
                                                    # the UI above can be replicated, but most importnatly is here:
                                                    # we pass the email and password values to the req_register function
                                                    # FilledButton(
                                                    # content=Text(
                                                    # "Register",
                                                    # weight="w700",
                                                    # ),
                                                    # width=160,
                                                    # height=40,
                                                    # # pass the input values to the function that sends HTTP requests
                                                    # on_click=lambda e: req_registter(
                                                    # e,
                                                    # email.value,
                                                    # password.value,
                                                    # ),
                                                    # ),
                                                    FilledButton(
                                                        content=Text(
                                                            "Login",
                                                            weight="w700",
                                                        ),
                                                        width=160,
                                                        height=40,
                                                        on_click=lambda __: page.go(
                                                            "/login"
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
                                        gradient=GradientGenerator("#000", "#111"),
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
                                                        # FilledButton(
                                                        # content=Text(
                                                        # "Register",
                                                        # weight="w700",
                                                        # ),
                                                        # width=160,
                                                        # height=40,
                                                        # on_click=lambda e: req_register(
                                                        # e,
                                                        # email.value,
                                                        # password.value,
                                                        # ),
                                                        # ),
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


# we can now test this using the web browser
flet.app(target=main, host="localhost", port=9999, view=flet.WEB_BROWSER)
