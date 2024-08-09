import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestChapters(unittest.TestCase):

    def test_get_chapter(self):
        response = client.get("/courses/Highlights of Calculus/chapters/Big Picture of Calculus")
        self.assertEqual(response.status_code, 200)

    def test_rate_chapter(self):
        rating = {"positive": 1, "negative": 0}
        response = client.post("/courses/Highlights of Calculus/chapters/Big Picture of Calculus/rate", json=rating)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], "Rating updated successfully")

if __name__ == '__main__':
    unittest.main()