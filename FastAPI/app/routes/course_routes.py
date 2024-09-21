from fastapi import APIRouter
from app.models import course_model
from app.services.course_controller import get_course, get_courses, create_course, delete_course

courses_route = APIRouter()

@courses_route.get('/')
async def get_courses():
    get_courses()

@courses_route.get("/{course_id}")
def get_course(course_id: int):
    get_course(course_id)

@courses_route.post('/')
async def create_course(course: course_model):
    create_course(course)

@courses_route.put('/{courses_id}')
async def update_course(course_id: int, course: course_model):
    return {"course_id": course_id, **course.dict()}

@courses_route.delete('/{course_id}')
async def delete_course(course_id: int):
    delete_course(course_id)