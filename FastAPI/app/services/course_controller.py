from app.models import course_model
from starlette.exceptions import HTTPException
from config.database import CourseModel

async def get_courses():
    try:
        courses = list(CourseModel.select())
        return courses
    except Exception as e:
        print(e)


def get_course(course_id: int):
    try:
        course = CourseModel.get(CourseModel.id == course_id)
        return course
    except CourseModel.DoesNotExist:
        raise HTTPException(404, "course not found")

async def create_course(course: course_model):
    try:
        CourseModel.create(name=course.name, species=course.species, age=course.age, weight=course.weight)
        return course
    except Exception as e:
        print(e)

async def update_course(course_id: int, course: course_model):
    return {"course_id": course_id, **course.dict()}

async def delete_course(course_id: int):
    try:
        course = CourseModel.Delete(CourseModel.id == course_id)
        return course
    except CourseModel.DoesNotExist:
        raise HTTPException(404, "course not found")