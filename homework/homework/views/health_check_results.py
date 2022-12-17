from http.client import HTTPResponse
from flet import View, Text, Column, ElevatedButton


class HealthCheckResultsView:
    def healthcheck_results_view(response: HTTPResponse, page):
        return View(
            f"/{response.status_code}",
            horizontal_alignment="center",
            vertical_alignment="center",
            controls=[
                Column(
                    alignment="center",
                    horizontal_alignment="center",
                    controls=[
                        Text(
                            f"response was {response.status_code}!",
                            size=44,
                            weight="w700",
                            text_align="center",
                        ),
                        Text(
                            # We can show the user info by using the string
                            f"Health Check  {response.json()}",
                            size=32,
                            weight="w500",
                            text_align="center",
                        ),
                        ElevatedButton(
                            "Visit Welcome",
                            on_click=lambda _: page.go("/welcome"),
                        ),
                        ElevatedButton(
                            "Visit Welcome", on_click=lambda _: page.go("/welcome")
                        ),
                    ],
                ),
            ],
        )
