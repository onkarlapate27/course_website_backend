from pydantic import BaseModel
from typing import List

class Rating(BaseModel):
    positive: int = 0
    negative: int = 0

class Chapter(BaseModel):
    name: str
    text: str
    rating: Rating = Rating()

class Course(BaseModel):
    name: str
    date: int
    description: str
    domain: List[str]
    chapters: List[Chapter]
    total_rating: Rating = Rating()