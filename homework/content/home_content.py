from flet import Column, Text, UserControl


class HomeContent(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return Column(
            [
                Text(
                    "Hello",
                ),
            ],
        )
