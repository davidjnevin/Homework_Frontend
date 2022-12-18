import time
from math import pi

import flet
from controls.menus.collapsible import Collapsible
from controls.menus.menu_button import MenuButton
from flet import Column, Icon, Page, Row, Text, icons


def main(page: Page):

    page.scroll = "auto"
    page.add(
        Column(
            [
                Collapsible(
                    "Buttons",
                    icon=Icon(icons.SMART_BUTTON),
                    content=Column(
                        [
                            MenuButton("Basic buttons"),
                            MenuButton("Floating action button"),
                            MenuButton("Popup menu button", selected=True),
                        ],
                        spacing=3,
                    ),
                ),
                Collapsible(
                    "Simple apps",
                    icon=Icon(icons.NEW_RELEASES),
                    content=Column(
                        [
                            MenuButton("Basic buttons"),
                            MenuButton("Floating action button"),
                            MenuButton("Popup menu button", selected=True),
                        ],
                        spacing=3,
                    ),
                ),
                Collapsible(
                    "Forms",
                    icon=Icon(icons.DYNAMIC_FORM),
                    content=Column(
                        [
                            MenuButton("Basic buttons"),
                            MenuButton("Floating action button"),
                            MenuButton("Popup menu button", selected=True),
                        ],
                        spacing=3,
                    ),
                ),
            ],
            spacing=3,
            width=930,
        )
    )


flet.app(port=8550, target=main, view=flet.WEB_BROWSER)
