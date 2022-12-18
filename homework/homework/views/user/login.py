from datetime import datetime
from flet import AppBar, ElevatedButton, Text, View, colors
from pydantic import ValidationError
from homework.models.users import UserLoginModel

from email_validator import EmailNotValidError
import ast
from homework.components import FormFields
from homework.data import UserApiCalls as apicall


class LoginView:
    def login_view(e, page):
        """Login view."""

        txt_email = FormFields.text_field("Your Email")
        txt_password = FormFields.password_field("Your Password")

        def login_btn_click(e):
            view.clean()
            if not txt_email.value:
                txt_email.error_text = "Please enter an email address."
            else:
                txt_email.error_text = ""
            if not txt_password.value:
                txt_password.error_text = "Please enter your password."
            else:
                txt_password.error_text = ""
            page.update()

            if txt_email.value and txt_password.value:
                try:
                    login_data = UserLoginModel(
                        email=txt_email.value, password=txt_password.value
                    )
                except ValidationError as error:
                    error_text = ast.literal_eval(error.json())[0]["msg"]
                    txt_email.error_text = error_text
                    login_data = False
                    page.update()

                if login_data:
                    try:
                        response = apicall.login_user(login_data)
                        if response.status_code == 200:
                            page.go("/welcome")
                        else:
                            api_connection_error = FormFields.text_field(
                                response.content
                            )
                            page.controls.append(api_connection_error)
                    except Exception as e:
                        api_connection_error = FormFields.text_field(
                            f'{str(Exception("There is a problem connecting to the server. Please try again in a few mintes."))}'
                        )
                        view.controls.append(api_connection_error)

            page.update()

        view = View(
            "/",
            controls=[
                AppBar(title=Text("Login"), bgcolor=colors.SURFACE_VARIANT),
                txt_email,
                txt_password,
                ElevatedButton("Login", on_click=login_btn_click),
                ElevatedButton("Visit Welcome", on_click=lambda _: page.go("/welcome")),
            ],
        )

        return view
