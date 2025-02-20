"""
Trie Data Structure for Autocomplete and Fuzzy Search

This module implements a trie data structure that supports fast insertion, deletion,
and lookup operations. It is used for the autocomplete functionality of our search engine.

Functions:
    insert(word): Inserts a new word into the trie.
    search(prefix): Returns all words in the trie that start with the given prefix.
"""

class TrieNode:
    def __init__(self):
        # Each node stores children in a dictionary and a flag indicating end-of-word.
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        # Insert each character; create new node if necessary
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, prefix):
        # Traverse to end of prefix
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []  # Prefix not in trie
            node = node.children[char]
        results = []

        def dfs(current, path):
            # If word end, add to results
            if current.is_end_of_word:
                results.append(path)
            # Traverse children recursively
            for ch, child in current.children.items():
                dfs(child, path + ch)

        dfs(node, prefix)
        return results
