from fastapi import APIRouter, Query, HTTPException
from typing import List
from app.crud import get_all_courses, get_course
from app.helper import log_exception
from app.models import Course

router = APIRouter()

@router.get("/", response_model=List[Course])
def read_courses(
    sort_by: str = Query('alphabetical', regex='^(alphabetical|date|rating)$'),
    domain: str = None
):
    try:
        courses = get_all_courses(sort_by, domain)
        return courses
    except Exception as e:
        log_exception(e, "Error occurred while reading courses")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{course_name}", response_model=Course)
def read_course(course_name: str):
    try:
        course = get_course(course_name)
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")
        return course
    except Exception as e:
        log_exception(e, f"Error occurred while reading course with name: {course_name}")
        raise HTTPException(status_code=500, detail="Internal Server Error")