from flet import (
    AppBar,
    Card,
    Column,
    Container,
    ElevatedButton,
    FilledButton,
    Row,
    Text,
    View,
    alignment,
    border_radius,
    colors,
    padding,
)


class LandingPageView:
    def landing_page_view(page):
        """Landing Page view."""
        view = View(
            "/welcome",
            [
                AppBar(title=Text("Homework Welcome"), bgcolor=colors.SURFACE_VARIANT),
                Column(
                    [
                        ElevatedButton("Login", on_click=lambda _: page.go("/login")),
                        # ElevatedButton("Register", on_click=lambda _: page.go("/register")),
                    ]
                ),
            ],
        )
        return view
