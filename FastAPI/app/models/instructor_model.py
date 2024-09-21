from pydantic import BaseModel

class instructor(BaseModel):
    id: int
    name: str
    speciality: str