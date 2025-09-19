
import unittest
from unittest.mock import patch, MagicMock
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello, world!")

    @patch("app.client.models.generate_content")
    def test_ai_route_post(self, mock_generate_content):
        # Create a mock response object with a .text attribute
        mock_response = MagicMock()
        mock_response.text = "mocked gemini response"
        mock_generate_content.return_value = mock_response

        response = self.app.post("/ai", json={"query": "test"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "mocked gemini response")

if __name__ == "__main__":
    unittest.main()
