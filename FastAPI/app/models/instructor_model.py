"""
This module contains the model for instructors

Contains the following class:
    - instructor (pydantic model)
"""

from pydantic import BaseModel


class Instructor(BaseModel):
    """
    Model for instructors
    """

    id: int
    name: str
    speciality: str
