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
    AppBar,
    colors,
    ElevatedButton,
)


class LandingPageView:
    def landing_page_view(page):
        """Landing Page view."""
        view = View(
            "/welcome",
            [
                AppBar(title=Text("Welcome"), bgcolor=colors.SURFACE_VARIANT),
                ElevatedButton("Login", on_click=lambda _: page.go("/login")),
                ElevatedButton("Register", on_click=lambda _: page.go("/register")),
            ],
        )
        return view
