from pydantic import BaseModel, ValidatonError, validator, EmailStr
from datetime import datetime
import re


class LoginModel(BaseModel):
    email: EmailStr
    password: str


class UserInModel(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name_1: str
    last_name_2: str
    description: str
    date_joined: datetime
    is_staff: bool
    is_learner: bool
    is_guardian: bool

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


class UserModel(BaseModel):
    email: EmailStr
    first_name: str
    last_name_1: str
    last_name_2: str
    description: str
    is_staff: bool
    is_learner: bool
    is_guardian: bool
