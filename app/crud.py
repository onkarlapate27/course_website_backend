from app.database import db
from app.helper import log_exception

def get_all_courses(sort_by, domain):
    try:
        sort_criteria = {
            'alphabetical': ('name', 1),
            'date': ('date', -1),
            'rating': ('total_rating.positive', -1)
        }
        query = {}
        if domain:
            query['domain'] = domain
        return list(db.courses.find(query).sort(*sort_criteria[sort_by]))
    except Exception as e:
        log_exception(e, "Failed to get all courses")
        raise

def get_course(course_name):
    try:
        return db.courses.find_one({"name": course_name})
    except Exception as e:
        log_exception(e, f"Failed to get course with name: {course_name}")
        raise

def get_chapter(course_name, chapter_name):
    try:
        course = db.courses.find_one({"name": course_name}, {"chapters": 1, "_id": 0})
        if not course:
            return None
        return next((ch for ch in course['chapters'] if ch['name'] == chapter_name), None)
    except Exception as e:
        log_exception(e, f"Failed to get chapter {chapter_name} from course {course_name}")
        raise

def rate_chapter(course_name, chapter_name, rating):
    try:
        course = db.courses.find_one({"name": course_name})
        if not course:
            return None
        chapter = next((ch for ch in course['chapters'] if ch['name'] == chapter_name), None)
        if not chapter:
            return None
        
        if 'rating' not in chapter:
            chapter['rating'] = {'positive': 0, 'negative': 0}
        if 'total_rating' not in course:
            course['total_rating'] = {'positive': 0, 'negative': 0}

        chapter['rating']['positive'] += rating['positive']
        chapter['rating']['negative'] += rating['negative']
        course['total_rating']['positive'] += rating['positive']
        course['total_rating']['negative'] += rating['negative']
        db.courses.update_one(
            {"name": course_name, "chapters.name": chapter_name},
            {"$set": {
                "chapters.$.rating": chapter['rating'],
                "total_rating": course['total_rating']
            }}
        )
        return True
    except Exception as e:
        log_exception(e, f"Failed to rate chapter {chapter_name} in course {course_name}")
        raise