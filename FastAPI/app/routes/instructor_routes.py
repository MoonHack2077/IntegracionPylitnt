"""
This module contains the routes for instructors
"""

from fastapi import APIRouter
from models.instructor_model import Instructor
from services.instructor_controller import (
    get_instructor_service,
    get_instructors_service,
    create_instructor_service,
    delete_instructor_service,
)

instructors_route = APIRouter()


@instructors_route.get("/")
async def get_instructors():
    """Get all the instructors"""
    get_instructors_service()


@instructors_route.get("/{instructor_id}")
def get_instructor(instructor_id: int):
    """Get an instructor by it's id"""
    get_instructor_service(instructor_id)


@instructors_route.post("/")
async def create_instructor(instructor: Instructor):
    """Create a new instructor"""
    create_instructor_service(instructor)


@instructors_route.put("/{instructors_id}")
async def update_instructor(instructor_id: int, instructor: Instructor):
    """Update an instructor"""
    return {"instructor_id": instructor_id, **instructor.dict()}


@instructors_route.delete("/{instructor_id}")
async def delete_instructor(instructor_id: int):
    """Delete an instructor"""
    delete_instructor_service(instructor_id)
