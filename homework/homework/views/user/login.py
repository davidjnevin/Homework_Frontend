from email_validator import EmailNotValidError, validate_email
from flet import AppBar, ElevatedButton, Text, View, colors

from homework.components import FormFields as ffs
from homework.data import UserApiCalls as apicall
from homework.models.users import UserLoginModel


class LoginView:
    def login_view(e, page):
        """Login view."""

        txt_email = ffs.text_field("Your Email")
        txt_password = ffs.password_field("Your Password")
        api_error_notifcation = ffs.text_alert(
            "We cannot find a user for that email address and that password. Please try again."
        )

        def login_btn_click(e):
            api_error_notifcation.visible = False
            view.clean()
            view.update()
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
                    validation = validate_email(txt_email.value)
                    email = validation.email
                    login_data = UserLoginModel(
                        email=email, password=txt_password.value
                    )
                except EmailNotValidError as error:
                    txt_email.error_text = str(error)
                    login_data = False
                    page.update()

                if login_data:
                    try:
                        response = apicall.login_user(login_data)
                        if response.status_code == 200:
                            page.go("/welcome")
                        if response.status_code == 401:
                            print("Response in btn_click: ", response.status_code)
                            api_error_notifcation.visible = True
                            txt_email.error_text = ""
                            txt_password.error_text = ""
                            txt_email.value = ""
                            txt_password.value = ""
                            view.update()

                    except Exception as e:
                        api_connection_error_message = f'{str(e("There is a problem connecting to the server. Please try again in a few mintes."))}'
                        api_connection_error_notification = ffs.text_alert(
                            api_connection_error_message
                        )
                        api_connection_error_notification.visible = True
                        view.update()
            page.update()

        view = View(
            "/",
            controls=[
                AppBar(title=Text("Login"), bgcolor=colors.SURFACE_VARIANT),
                api_error_notifcation,
                txt_email,
                txt_password,
                ElevatedButton("Login", on_click=login_btn_click),
                ElevatedButton("Start", on_click=lambda _: page.go("/start")),
            ],
        )

        return view
