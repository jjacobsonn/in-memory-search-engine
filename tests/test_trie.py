import unittest
from src.trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        for word in ["apple", "app", "application", "apt"]:
            self.trie.insert(word)

    def test_search_found(self):
        # Test autocomplete returns complete words for given prefix.
        self.assertIn("app", self.trie.search("app"))
        self.assertIn("apple", self.trie.search("app"))
    
    def test_search_not_found(self):
        # Test returning empty list for unmatched prefix.
        self.assertEqual(self.trie.search("xyz"), [])

if __name__ == "__main__":
    unittest.main()
