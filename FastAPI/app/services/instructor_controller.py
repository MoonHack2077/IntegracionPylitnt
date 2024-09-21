from app.models import instructor_model
from starlette.exceptions import HTTPException
from config.database import InstructorModel

async def get_instructors():
    try:
        instructors = list(InstructorModel.select())
        return instructors
    except Exception as e:
        print(e)

def get_instructor(instructor_id: int):
    try:
        instructor = InstructorModel.get(InstructorModel.id == instructor_id)
        return instructor
    except InstructorModel.DoesNotExist:
        raise HTTPException(404, "instructor not found")

async def create_instructor(instructor: instructor_model):
    try:
        InstructorModel.create(name=instructor.name, species=instructor.species, age=instructor.age, weight=instructor.weight)
        return instructor
    except Exception as e:
        print(e)

async def update_instructor(instructor_id: int, instructor: instructor_model):
    return {"instructor_id": instructor_id, **instructor.dict()}

async def delete_instructor(instructor_id: int):
    try:
        instructor = InstructorModel.Delete(InstructorModel.id == instructor_id)
        return instructor
    except InstructorModel.DoesNotExist:
        raise HTTPException(404, "instructor not found")