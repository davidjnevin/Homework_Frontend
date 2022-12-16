from flet import TextField
from flet import AppBar, ElevatedButton, Text, View, colors


class LoginView:
    def login_view(e, page):
        """Login view."""

        txt_email = TextField(label="Your Email")
        txt_password = TextField(label="Your Password")

        login_response = Text(value="")

        def login_btn_click(e):
            view.clean()
            if not txt_email.value:
                txt_email.error_text = "Please enter your email"
                view.clean()
                page.update()
            if not txt_password.value:
                txt_password.error_text = "Please enter your password"
                view.clean()
                page.update()
            else:
                name = f"{txt_email.value} !"
                login_response = Text(f"Hello, {name}!")
                view.controls.append(login_response)
                page.update()
                page.go("/welcome")

        view = View(
            "/",
            [
                AppBar(title=Text("Login"), bgcolor=colors.SURFACE_VARIANT),
                txt_email,
                txt_password,
                ElevatedButton("Login", on_click=login_btn_click),
                login_response,
                ElevatedButton("Visit Welcome", on_click=lambda _: page.go("/welcome")),
            ],
        )

        return view
