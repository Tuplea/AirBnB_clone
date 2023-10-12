#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review  class"""

    place_id = ""
    user_id = ""
    text = ""
