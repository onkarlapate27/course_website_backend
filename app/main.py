from fastapi import FastAPI
from app.routes import courses, chapters


app = FastAPI()

app.include_router(courses.router, prefix="/courses", tags=["courses"])
app.include_router(chapters.router, prefix="/courses/{course_name}/chapters", tags=["chapters"])