#!/usr/bin/python3
"""
This module defines the User class, which inherits from BaseModel.

"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    The User class inherits from BaseModel and
    defines attributes/methods specific to User objects.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
