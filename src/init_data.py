import json
from src.trie import Trie

def load_demo_data(filepath: str = "./data/demo_data.json"):
    with open(filepath, "r") as f:
        return json.load(f)

def populate_trie(trie: Trie, words):
    for word in words:
        trie.insert(word)
