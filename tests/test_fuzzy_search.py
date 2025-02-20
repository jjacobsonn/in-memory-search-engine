import unittest
from src.fuzzy_search import fuzzy_search

class TestFuzzySearch(unittest.TestCase):
    def test_fuzzy_exact(self):
        # Exact match should return the word.
        words = ["hello", "world"]
        results = fuzzy_search("hello", max_distance=0, word_list=words)
        self.assertEqual(results, ["hello"])
    
    def test_fuzzy_near_match(self):
        # A one-letter mistyped query should be caught.
        words = ["hello", "help", "shell"]
        results = fuzzy_search("helo", max_distance=1, word_list=words)
        self.assertIn("hello", results)

if __name__ == "__main__":
    unittest.main()
