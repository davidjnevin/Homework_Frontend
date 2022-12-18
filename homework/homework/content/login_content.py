from flet import (
    Card,
    Column,
    Container,
    FilledButton,
    Row,
    Text,
    UserControl,
    border_radius,
    padding,
)

from homework.components import FormFields

email = FormFields.text_field("Email")
password = FormFields.password_field("Password")


class LoginContent(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return Column(
            [
                Column(
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
                                                            # on_click=lambda e: req_login(
                                                            # e,
                                                            # email.value,
                                                            # password.value,
                                                            # ),
                                                        ),
                                                        FilledButton(
                                                            content=Text(
                                                                "healthcheck",
                                                                weight="w700",
                                                            ),
                                                            width=160,
                                                            height=40,
                                                            # on_click=lambda e: req_healthcheck(
                                                            # e,
                                                            # ),
                                                        ),
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
            ],
        )
