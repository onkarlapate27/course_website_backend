from fastapi import APIRouter, HTTPException
from app.crud import get_chapter, rate_chapter
from app.helper import log_exception
from app.models import Chapter, Rating

router = APIRouter()

@router.get("/{chapter_name}", response_model=Chapter)
def read_chapter(course_name: str, chapter_name: str):
    try:
        chapter = get_chapter(course_name, chapter_name)
        if not chapter:
            raise HTTPException(status_code=404, detail="Chapter not found")
        return chapter
    except Exception as e:
        log_exception(e, f"Error occurred while reading chapter {chapter_name} in course {course_name}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/{chapter_name}/rate")
def rate_chapter_endpoint(course_name: str, chapter_name: str, rating: Rating):
    try:
        result = rate_chapter(course_name, chapter_name, rating.dict())
        if not result:
            raise HTTPException(status_code=404, detail="Course or chapter not found")
        return {"message": "Rating updated successfully"}
    except Exception as e:
        log_exception(e, f"Error occurred while rating chapter {chapter_name} in course {course_name}")
        raise HTTPException(status_code=500, detail="Internal Server Error")