import flet
from flet import Container, ElevatedButton, Page, Stack


def main(page: Page):

    c1 = Container(width=50, height=50, bgcolor="red", animate_position=1000)

    c2 = Container(
        width=50, height=50, bgcolor="green", top=60, left=0, animate_position=500
    )

    c3 = Container(
        width=50, height=50, bgcolor="blue", top=120, left=0, animate_position=1000
    )

    def animate_container(e):
        c1.top = 20
        c1.left = 200
        c2.top = 100
        c2.left = 40
        c3.top = 180
        c3.left = 100
        page.update()

    page.add(
        Stack([c1, c2, c3], height=400),
        ElevatedButton("Animate!", on_click=animate_container),
    )


flet.app(target=main)
