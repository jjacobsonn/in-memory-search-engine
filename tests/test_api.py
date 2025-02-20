import unittest
import requests

class TestAPI(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:8000"

    def test_autocomplete(self):
        """Test autocomplete endpoint."""
        response = requests.get(f"{self.BASE_URL}/autocomplete?prefix=hel")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("results", data)
        self.assertTrue(len(data["results"]) >= 1)

    def test_fuzzy(self):
        """Test fuzzy search endpoint."""
        response = requests.get(f"{self.BASE_URL}/fuzzy?query=helo&max_distance=1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("results", data)
        self.assertTrue(len(data["results"]) >= 1)

if __name__ == "__main__":
    unittest.main()
