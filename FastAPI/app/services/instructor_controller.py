"""
This module contains the controller for instructors

Contains the following functions:
    - get_instructors (async): Get all the instructors
    - get_instructor (sync): Get an instructor by it's id
    - create_instructor (async): Create a new instructor
    - update_instructor (async): Update an instructor
    - delete_instructor (async): Delete an instructor
"""
from app.models import instructor_model
from starlette.exceptions import HTTPException
from config.database import InstructorModel

async def get_instructors_service():
    try:
        instructors = list(InstructorModel.select())
        return instructors
    except Exception as e:
        print(e)

def get_instructor_service(instructor_id: int):
    try:
        instructor = InstructorModel.get(InstructorModel.id == instructor_id)
        return instructor
    except InstructorModel.DoesNotExist:
        raise HTTPException(404, "instructor not found")

async def create_instructor_service(instructor: instructor_model):
    try:
        InstructorModel.create(name=instructor.name, speciality=instructor.speciality)
        return instructor
    except Exception as e:
        print(e)

async def update_instructor_service(instructor_id: int, instructor: instructor_model):
    return {"instructor_id": instructor_id, **instructor.dict()}

async def delete_instructor_service(instructor_id: int):
    try:
        instructor = InstructorModel.Delete(InstructorModel.id == instructor_id)
        return instructor
    except InstructorModel.DoesNotExist:
        raise HTTPException(404, "instructor not found")
