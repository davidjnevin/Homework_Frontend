import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors, TextField
from views.views import PageViews as pgvs


def main(page: Page):
    page.title = "Homework Helper"

    def route_change(e):
        page.views.clear()
        page.views.append(pgvs.login_view(e, page))
        if page.route == "/welcome":
            page.views.append(pgvs.welcome_view(e, page))
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)


flet.app(target=main, view=flet.WEB_BROWSER)
