# TALLER IMPLEMENTACIÓN PYLINT Y BLACK

## FastAPI Application

This project is a FastAPI-based application that provides endpoints to manage courses and its instructors.

## Prerequisites

Make sure you have the following software installed:

- [Docker](https://www.docker.com/)
- [Python 3.8+](https://www.python.org/downloads/)

## Initial Setup

1. Clone the repository:
    bash
    git clone <https://github.com/MoonHack2077/IntegracionPylitnt.git>
    cd <https://github.com/MoonHack2077/IntegracionPylitnt.git>
    

2. Install the Python dependencies:
    bash
    pip install -r requirements.txt
    

## Starting the Database with Docker

To start the database using Docker, follow these steps:

1. Make sure you are in the root directory of the project, then run the following command:
    bash
    docker-compose up -d
    

This command will start the containers defined in the docker-compose.yml file, including the database configured for your project. The -d option runs the containers in the background.

2. To verify that the containers are running, use:
    bash
    docker ps
    

## Running the Application

1. Start the FastAPI application by running:
    bash
    uvicorn FastAPI.app.main:app --reload --host 0.0.0.0 --port 8000
    

This will start the FastAPI development server. By default, the application will be available at http://127.0.0.1:8000.

2. Access the interactive API documentation at:
    - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Analyzing the Code with Pylint

To analyze the code using Pylint, follow these steps:

1. Install Pylint if you haven't already:
    bash
    pip install pylint
    

2. Run Pylint using the provided configuration file:
    bash
    pylint --rcfile=pylint.yml <path to the file or directory you want to analyze>
    

For example, to analyze the entire project:
   bash
   pylint --rcfile=pylint.yml .
   
## Shutting Down the Database and Application

1. To stop the Docker containers, use:
    bash
    docker-compose down
    
2. To stop the FastAPI application, press Ctrl + C in the terminal where uvicorn is running.