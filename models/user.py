#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""
from models.base_model import BaseModel


class User(BaseModel):
    """This is the User class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
