from pydantic import UUID4, BaseModel, ValidationError, validator, EmailStr
from datetime import datetime
import re
from dataclasses import dataclass

from email_validator import validate_email, EmailNotValidError


class UserLoginModel(BaseModel):
    email: EmailStr
    password: str

    # @validator("email")
    # def login_email_validator(cls, email: str):
    # try:
    # validation = validate_email(email, check_deliverability=False)

    # email = validation.email
    # except Exception:
    # print("validate_email exception: ", str(Exception))
    # except ValidationError as e:
    # raise EmailNotValidError
    # return email


class UserInModel(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name_1: str
    last_name_2: str
    description: str
    date_joined: datetime
    is_learner: bool
    is_guardian: bool

    @validator("email")
    def user_in_email_validator(cls, value: str) -> str:
        try:
            validation = validate_email(value)
            email = validation.value
        except EmailNotValidError as e:
            raise e
        return email

    @validator("password")
    def password_validator(cls, value: str) -> str:
        msg_error = (
            "password requirements: min. length of 8 chars, "
            "one uppercase char, one lowercase char, one digit, "
            "one special char (not letter, not number)"
        )
        patterns = (".{8}", "[A-Z]", "[a-z]", "[0-9]", "[^a-zA-Z0-9]")
        for pattern in patterns:
            if re.search(pattern, value) is None:
                raise ValueError(msg_error)

        return value


@dataclass
class UserOutModel:
    id: UUID4
    email: EmailStr
    first_name: str
    last_name_1: str
    last_name_2: str
    description: str
    date_joined: datetime
    is_learner: bool
    is_guardian: bool
