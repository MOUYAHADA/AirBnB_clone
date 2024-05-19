#!/usr/bin/python3
"""User class that inherits from BaseModel Class"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class for creating a user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
