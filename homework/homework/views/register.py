from flet import (
    Text,
    View,
    Column,
    Container,
    border_radius,
    padding,
    Row,
    Card,
    FilledButton,
)


class RegisterView:
    def register_view(
        page,
        email,
        password,
        first_name,
        last_name_1,
        last_name_2,
        account_type,
        snack,
    ):
        register_view = View(
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
                                        Container(padding=padding.only(bottom=20)),
                                        email,
                                        Container(padding=padding.only(bottom=10)),
                                        password,
                                        Container(padding=padding.only(bottom=20)),
                                        first_name,
                                        Container(padding=padding.only(bottom=20)),
                                        last_name_1,
                                        Container(padding=padding.only(bottom=20)),
                                        last_name_2,
                                        Container(padding=padding.only(bottom=20)),
                                        Row(
                                            alignment="center",
                                            spacing=20,
                                            controls=[
                                                account_type,
                                                Container(
                                                    padding=padding.only(bottom=20)
                                                ),
                                            ],
                                        ),
                                        Row(
                                            alignment="center",
                                            spacing=20,
                                            controls=[
                                                # the UI above can be replicated, but most importnatly is here:
                                                # we pass the email and password values to the req_register function
                                                FilledButton(
                                                    content=Text(
                                                        "Register",
                                                        weight="w700",
                                                    ),
                                                    width=160,
                                                    height=40,
                                                    # pass the input values to the function that sends HTTP requests
                                                    on_click=lambda e: req_register(
                                                        e,
                                                        email.value,
                                                        password.value,
                                                        first_name.vale,
                                                        last_name_1.value,
                                                        last_name_2.value,
                                                        account_type.value,
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

        return register_view
