from fastapi import APIRouter
from app.models import instructor_model
from app.services.instructor_controller import get_instructor, get_instructors, create_instructor, delete_instructor

instructors_route = APIRouter()

@instructors_route.get('/')
async def get_instructors():
    get_instructors()

@instructors_route.get("/{instructor_id}")
def get_instructor(instructor_id: int):
    get_instructor(instructor_id)

@instructors_route.post('/')
async def create_instructor(instructor: instructor_model):
    create_instructor(instructor)

@instructors_route.put('/{instructors_id}')
async def update_instructor(instructor_id: int, instructor: instructor_model):
    return {"instructor_id": instructor_id, **instructor.dict()}

@instructors_route.delete('/{instructor_id}')
async def delete_instructor(instructor_id: int):
    delete_instructor(instructor_id)