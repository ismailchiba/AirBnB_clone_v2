#!/usr/bin/python3
"""
This module defines the Amenity class, which inherits from BaseModel.

"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class for representing amenities in the AirBnB clone project.

    Attributes:
        name (str): Name of the amenity.
    """

    name = ""
