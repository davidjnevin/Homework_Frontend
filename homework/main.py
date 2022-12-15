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
)

from flet import icons
from components.form_fields import FormFields
from datetime import datetime
from flet.radio import Radio

import requests
from views import RegisterView, LandingPageView, HealthCheckResultsView
from utils.register import RegisterService
from utils.login import LoginService
from utils.healthcheck import HealthCheckService
from content.home_content import HomeContent
from content.login_content import LoginContent

APP_NAME = "Homework"


home_content = HomeContent()
login_content = LoginContent()


def main(page: Page):
    page.title = "Homework"
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
                Tab(text="Assignments", content=login_content),
                Tab(text="Menu3", content=home_content),
                Tab(text="Menu4", content=home_content),
                Tab(text="Menu5", content=home_content),
            ],
        )
    )

    page.add(
        Row(
            height=20,
            vertical_alignment="end",
            controls=[
                Text(
                    "Made with ❤ by @davidjnevin ",
                    style="labelSmall",
                    weight="bold",
                    italic=True,
                    color=colors.BLACK,
                ),
            ],
        ),
    )


flet.app(target=main)
