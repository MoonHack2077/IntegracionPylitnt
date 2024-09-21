""" This module contains the FastAPI application. """

from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI
from starlette.responses import RedirectResponse

# Base de datos
from config.database import database as connection

# routes
from routes.course_routes import courses_route
from routes.instructor_routes import instructors_route

# Apikey
from helpers.api_key_auth import get_api_key


# on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    FastAPI Lifespan: Connect to database if connection is closed on startup,
    and close connection when application is shutdown.
    """
    # Connects to the db if the connection is closed
    if connection.is_closed():
        connection.connect()
    try:
        yield  # Here the app will be executed
    finally:
        # Close the connection when the application is shutdown
        if not connection.is_closed():
            connection.close()


app = FastAPI(lifespan=lifespan)


# Docs
@app.get("/")
def read_root():
    """
    Redirects to the docs from API in the route /docs
    """
    return RedirectResponse("/docs")


# on routes
app.include_router(
    courses_route,
    prefix="/courses",
    tags=["courses"],
    dependencies=[Depends(get_api_key)],
)
app.include_router(
    instructors_route,
    prefix="/instructors",
    tags=["instructors"],
    dependencies=[Depends(get_api_key)],
)
