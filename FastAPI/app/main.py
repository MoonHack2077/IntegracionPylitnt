from fastapi import FastAPI
from starlette.responses import RedirectResponse

#routes
from routes.course_routes import courses_route
from routes.instructor_routes import instructors_route

# Base de datos
from config.database import database as connection
from contextlib import asynccontextmanager


#on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Conectar a la base de datos si la conexión está cerrada
    if connection.is_closed():
        connection.connect()
    try:
        yield  # Aquí es donde se ejecutará la aplicación
    finally:
        # Cerrar la conexión cuando la aplicación se detenga
        if not connection.is_closed():
            connection.close()


app = FastAPI(lifespan=lifespan)

#on shutdown

#Docs
@app.get('/')
def read_root():
    return RedirectResponse('/docs')

#on routes
app.include_router(courses_route, prefix="/courses", tags=["courses"])
app.include_router(instructors_route, prefix="/instructors", tags=["instructors"])
