from flet import Text, UserControl, colors, Row


class FooterContent(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return Row(
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
        )
