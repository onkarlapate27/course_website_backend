# Course Management API

This project provides a FastAPI-based backend service to manage courses and their chapters.

## Tech Stack

- **FastAPI**: Web framework for building APIs.
- **MongoDB**: NoSQL database for storing course and chapter data.

## Features

- **Retrieve All Courses**: Get a list of all available courses, with support for sorting by title, date, or rating, and optional filtering by domain.
- **Course Overview**: Fetch detailed information about a specific course.
- **Chapter Information**: Access specific chapter details within a course.
- **Rate Chapters**: Users can rate chapters positively or negatively, and the overall course rating is updated accordingly.

### Key Files

- **app/main.py**: Entry point of the application.
- **app/models.py**: Defines data models using Pydantic.
- **app/database.py**: Database connection and setup.
- **app/crud.py**: CRUD operations for courses and chapters.
- **app/routes/**: API route definitions.
- **app/tests/**: Contains unit tests for the API.
- **helpers.py**: Contains helper functions.
- **courses.json**: Contains courses json data.
- **scripts/**: Contains scripts for various tasks like inserting data in mongoDB

## Running the Application

### 1. Local Development

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

2. **Running FastAPI App**:
    ```bash
    uvicorn app.main:app --reload

3. **Running the tests**:
    ```bash
    python -m unittest discover -s app/tests


### 2. Containerized Setup

1. **Build the Docker Image**:
    ```bash
    docker build -t course-api .

2. **Run the Application with Docker Compose:**:
    ```bash
    docker-compose up

2. **Access the API**:
    The API will be available at http://localhost:8000/courses.