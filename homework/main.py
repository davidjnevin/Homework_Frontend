import gettext as gt
import random
import time
import flet
from flet import (
    Page,
    ProgressBar,
    RadioGroup,
    Tab,
    Tabs,
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
    ButtonStyle,
    icons,
)

from homework.components.form_fields import FormFields
from datetime import datetime
from flet.radio import Radio

import requests
from homework.views import (
    RegisterView,
    LandingPageView,
    HealthCheckResultsView,
    LoginView,
)
from homework.utils.register import RegisterService
from homework.utils.login import LoginService
from homework.utils.healthcheck import HealthCheckService

from homework.views.views import PageViews as pgvs

from homework.content.home_content import HomeContent
from homework.content.login_content import LoginContent
from homework.content.footer_content import FooterContent

APP_NAME = "Homework"


home_content = HomeContent()
login_content = LoginContent()
footer_content = FooterContent()


def main(page: Page):
    page.title = f"{APP_NAME}"
    page.theme_mode = "light"
    page.splash = ProgressBar(visible=False)
    page.vertical_alignment = "start"

    page.window_width = 572
    page.window_height = 720

    def change_theme(e):
        """
        Changes the app's theme_mode, from dark to light or light to dark. A splash(progress bar) is also shown.
        :param e: The event that triggered the function
        :type e: ControlEvent
        """
        page.splash.visible = True
        page.update()
        page.theme_mode = (
            "light" if page.theme_mode == "dark" else "dark"
        )  # changes the page's theme_mode
        page.splash.visible = False
        theme_icon_button.selected = not theme_icon_button.selected  # changes the icon
        time.sleep(
            0.2
        )  # shows the progress bar for a second indicating that work is being done..
        page.update()

    theme_icon_button = IconButton(
        icons.DARK_MODE,
        selected=False,
        selected_icon=icons.LIGHT_MODE,
        icon_size=35,
        tooltip="change theme",
        on_click=change_theme,
        style=ButtonStyle(
            color={"": colors.WHITE, "selected": colors.WHITE},
        ),
    )

    page.appbar = AppBar(
        title=Text(f"{ APP_NAME }", color="white"),
        center_title=True,
        bgcolor=colors.DEEP_PURPLE,
        actions=[theme_icon_button],
    )

    page.add(
        Tabs(
            expand=True,
            selected_index=5,
            tabs=[
                Tab(text="Home", content=home_content),
                Tab(text="Menu2", content=home_content),
                Tab(text="Menu3", content=home_content),
                Tab(text="Menu4", content=home_content),
                Tab(text="Menu5", content=home_content),
            ],
        )
    )

    page.add(footer_content)

    def route_change(e):
        page.views.clear()

        # First View is landing page
        page.views.append(LandingPageView.landing_page_view(page))

        if page.route == "/register":
            page.views.append(pgvs.register_view(e, page))

        if page.route == "/check_email":
            page.views.append(pgvs.check_email_view(e, page))
        if page.route == "/login":
            page.views.append(LoginView.login_view(e, page))

        # Main App View for Learners
        if page.route == "/learner":
            page.views.append(pgvs.learner_view(e, page))
        page.update()

        # Main App View for Guardians
        if page.route == "/guardian":
            page.views.append(pgvs.guardian_view(e, page))
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)


flet.app(target=main)
