from flet import Container, TextField, RadioGroup, Radio, Row, Text, colors

TEXT_SIZE = 14
FIELD_WIDTH = 320


class FormFields:
    def text_field(name: str):
        return TextField(
            label=f"{name}",
            # border="underline",
            # width=FIELD_WIDTH,
            text_size=TEXT_SIZE,
        )

    def account_type_field():
        return RadioGroup(
            content=Row(
                [
                    Radio(value="is_learner", label="Student"),
                    Radio(value="is_guardian", label="Guardian"),
                ]
            )
        )

    def password_field(display_text):
        return TextField(
            label=f"{display_text}",
            # border="underline",
            # width=FIELD_WIDTH,
            text_size=TEXT_SIZE,
            password=True,
            can_reveal_password=True,
        )

    def text_alert(text):
        return Container(
            content=Text(
                size=TEXT_SIZE,
                value=text,
            ),
            visible=False,
            bgcolor=colors.RED,
        )
