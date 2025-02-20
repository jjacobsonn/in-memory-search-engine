import unittest
import requests

class TestAPI(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:8000"

    def test_autocomplete_found(self):
        # Using prefix "de" to match "debug" and "deployment"
        response = requests.get(f"{self.BASE_URL}/autocomplete?prefix=de")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        # Check that at least one expected value is in the results.
        self.assertTrue("debug" in data["results"] or "deployment" in data["results"])

    def test_autocomplete_not_found(self):
        # Use a prefix that doesn't match any data
        response = requests.get(f"{self.BASE_URL}/autocomplete?prefix=xyz")
        self.assertEqual(response.status_code, 404)

    def test_fuzzy_found(self):
        # Test fuzzy search: misspelled "comit" should reasonably match "commit"
        response = requests.get(f"{self.BASE_URL}/fuzzy?query=comit&max_distance=2")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("commit", data["results"])

    def test_fuzzy_not_found(self):
        # Using a query that doesn't match any realistic term
        response = requests.get(f"{self.BASE_URL}/fuzzy?query=abcde&max_distance=2")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
