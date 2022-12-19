from datetime import datetime

import pytest
from email_validator import EmailNotValidError, validate_email
from freezegun import freeze_time
from hamcrest import assert_that, contains_string
from homework.models import UserInModel, UserLoginModel, UserOutModel


class TestUserModels:
    def test_login_model(self):
        sut = UserLoginModel(email="email@admin.com", password="Password10!")

        assert sut.email == "email@admin.com"
        assert sut.password == "Password10!"

    @pytest.mark.parametrize(
        "email,password,expected_error",
        [
            ("wrong_email", "Valid_P4ssw@rd", "The email address is not valid."),
            (
                "wrong_email@",
                "Valid_P4ssw@rd",
                "There must be something after the @-sign.",
            ),
            (
                "wrong_email@asdasd",
                "Valid_P4ssw@rd",
                "It should have a period",
            ),
        ],
        ids=[
            "no @ symbol",
            "nothing after @ symbol.",
            "It should have a period",
        ],
    )
    def test_login_model_bad_email_should_fail(self, email, password, expected_error):
        with pytest.raises(EmailNotValidError) as e_info:
            sut = validate_email(email, check_deliverability=False)
        assert_that(str(e_info), contains_string(expected_error))

    @freeze_time("2022-12-17 23:23:23")
    def test_user_in_model(self):

        email = "email@admin.com"
        password = "Password10!"
        first_name = "David"
        last_name_1 = "Nevin"
        last_name_2 = "Kelly"
        description = ""
        date_joined = datetime.now()
        is_learner = True
        is_guardian = False

        sut = UserInModel(
            email=email,
            password=password,
            first_name=first_name,
            last_name_1=last_name_1,
            last_name_2=last_name_2,
            description=description,
            date_joined=date_joined,
            is_learner=is_learner,
            is_guardian=is_guardian,
        )

        assert sut.email == "email@admin.com"
        assert sut.password == "Password10!"
        assert sut.first_name == "David"
        assert sut.last_name_1 == "Nevin"
        assert sut.last_name_2 == "Kelly"
        assert sut.description == ""
        assert sut.date_joined == datetime.now()
        assert sut.is_learner is True
        assert sut.is_guardian is False

    def test_user_out_model(self):
        id = "asdf"
        email = "email@admin.com"
        first_name = "David"
        last_name_1 = "Nevin"
        last_name_2 = "Kelly"
        description = ""
        date_joined = datetime.now()
        is_learner = True
        is_guardian = False

        sut = UserOutModel(
            id,
            email,
            first_name,
            last_name_1,
            last_name_2,
            description,
            date_joined,
            is_learner,
            is_guardian,
        )

        assert sut.id == "asdf"
        assert sut.email == "email@admin.com"
        assert sut.first_name == "David"
        assert sut.last_name_1 == "Nevin"
        assert sut.last_name_2 == "Kelly"
        assert sut.description == ""
        assert sut.date_joined == date_joined
        assert sut.is_learner is True
        assert sut.is_guardian is False
