"""
Course model

This module contains the model for courses
"""
from pydantic import BaseModel

class Course(BaseModel):
    """
    Model for courses
    """
    id: int
    name: str
    description: str
    id_instructor: int
