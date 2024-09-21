"""
This module contains the routes for courses
"""
from fastapi import APIRouter
from models.course_model import Course
from services.course_controller import (get_course_service,
                                        get_courses_service,
                                        create_course_service,
                                        delete_course_service)

courses_route = APIRouter()

@courses_route.get('/')
async def get_courses() -> list[Course]:
    """Get all the courses"""
    return get_courses_service()


@courses_route.get("/{course_id}")
def get_course(course_id: int) -> Course:
    """Get a course by it's id"""
    return get_course_service(course_id)


@courses_route.post('/')
async def create_course(course: Course) -> Course:
    """Create a new course"""
    return create_course_service(course)


@courses_route.put('/{courses_id}')
async def update_course(course_id: int, course: Course) -> dict[str, any]:
    """Update a course"""
    return {"course_id": course_id, **course.dict()}


@courses_route.delete('/{course_id}')
async def delete_course(course_id: int) -> None:
    """Delete a course"""
    delete_course_service(course_id)
