import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestCourses(unittest.TestCase):

    def test_get_courses(self):
        response = client.get("/courses")
        self.assertEqual(response.status_code, 200)

    def test_get_course(self):
        response = client.get("/courses/Highlights of Calculus")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Highlights of Calculus", response.json()['name'])
        
if __name__ == '__main__':
    unittest.main()