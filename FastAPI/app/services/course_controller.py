"""
This module contains the controller for courses

Contains the following functions:
    - get_courses (async): Get all the courses
    - get_course (sync): Get a course by it's id
    - create_course (async): Create a new course
    - update_course (async): Update a course
    - delete_course (async): Delete a course
"""
from models.course_model import Course
from starlette.exceptions import HTTPException
from config.database import CourseModel

async def get_courses_service():
    """
    Get all the courses
    """
    try:
        courses = list(CourseModel.select())
        return courses
    except Exception as e:
        print(e)

def get_course_service(course_id: int):
    """
    Get a course by it's id
    """
    try:
        course = CourseModel.get(CourseModel.id == course_id)
        return course
    except CourseModel.DoesNotExist:
        raise HTTPException(404, "course not found")

async def create_course_service(course: course_model):
    """
    Create a new course
    """
    try:
        CourseModel.create(name=course.name, description=course.description, id_instructor=course.id_instructor)
        return course
    except Exception as e:
        print(e)

async def update_course_service(course_id: int, course: course_model):
    """
    Update a course
    """
    return {"course_id": course_id, **course.dict()}

async def delete_course_service(course_id: int):
    """
    Delete a course
    """
    try:
        course = CourseModel.Delete(CourseModel.id == course_id)
        return course
    except CourseModel.DoesNotExist:
        raise HTTPException(404, "course not found")
