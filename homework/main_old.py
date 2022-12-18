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
    AppBar,
    Icon,
    IconButton,
    PopupMenuButton,
    PopupMenuItem,
    colors,
)

from flet import icons
from homework.components import FormFields
from datetime import datetime
from flet.radio import Radio

import requests
from homework.views import RegisterView, LandingPageView, HealthCheckResultsView
from homework.utils.register import RegisterService
from homework.utils.login import LoginService
from homework.utils.healthcheck import HealthCheckService


def main(page: Page):
    page.title = "Routes Example"
    snack = SnackBar(
        Text("Registration successfull!"),
    )

    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    def req_healthcheck(e):
        client = requests.session()

        # Define the endpoint URL
        url = "http://127.0.0.1:8000/api/healthcheck"

        headers = {"accept": "*/*"}

        response = client.get(url, headers=headers)

        if response.status_code == 200:
            page.views.append(
                HealthCheckResultsView.healthcheck_results_view(response, page)
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

    def req_login(e, email, password):
        data = {
            "email": email,
            "password": password,
        }
        client = requests.session()
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
        email = FormFields.text_field("Email")
        password = FormFields.password_field("Password")
        first_name = FormFields.text_field("First Name")
        last_name_1 = FormFields.text_field("Last Name 1")
        last_name_2 = FormFields.text_field("Last Name 2")
        account_type = FormFields.account_type_field()

        page.views.clear()
        """ we will be working with views, each 'page' will be a seperate view, i..e login page, reg page, etc..

        """
        # Landing page is the home_page_view
        page.views.append(LandingPageView.landing_page_view(page))

        if page.route == "/register":
            page.views.append(
                RegisterView.register_view(
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
