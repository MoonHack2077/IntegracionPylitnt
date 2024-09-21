"""
This module contains the controller for instructors

Contains the following functions:
    - get_instructors (async): Get all the instructors
    - get_instructor (sync): Get an instructor by it's id
    - create_instructor (async): Create a new instructor
    - update_instructor (async): Update an instructor
    - delete_instructor (async): Delete an instructor
"""
from models.instructor_model import Instructor
from starlette.exceptions import HTTPException
from config.database import InstructorModel
from peewee import DoesNotExist

async def get_instructors_service():
    """
    Get all the instructors
    """
    try:
        instructors = list(InstructorModel.select())
        return instructors
    except DoesNotExist as e:
        print(e)


def get_instructor_service(instructor_id: int):
    """
    Get an instructor by it's id
    """
    try:
        instructor = InstructorModel.get(InstructorModel.id == instructor_id)
        return instructor
    except DoesNotExist as exc:
        raise HTTPException(404, "instructor not found") from exc


async def create_instructor_service(instructor: Instructor):
    """
    Create a new instructor
    """
    try:
        InstructorModel.create(name=instructor.name, speciality=instructor.speciality)
        return instructor
    except DoesNotExist as e:
        print(e)


async def update_instructor_service(instructor_id: int, instructor: Instructor):
    """
    Update an instructor
    """
    return {"instructor_id": instructor_id, **instructor.dict()}


async def delete_instructor_service(instructor_id: int):
    """
    Delete an instructor
    """
    try:
        instructor = InstructorModel.delete().where(InstructorModel.id == instructor_id).execute()
        return instructor
    except DoesNotExist as exc:
        raise HTTPException(404, "instructor not found") from exc
