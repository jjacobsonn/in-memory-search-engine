#!/usr/bin/env python3
from src.trie import Trie
from src.init_data import load_demo_data, populate_trie

def main():
    trie = Trie()
    words = load_demo_data()  # Load realistic demo data
    populate_trie(trie, words)
    print("Autocomplete results for 'co':", trie.search("co"))
    print("Autocomplete results for 'de':", trie.search("de"))

if __name__ == "__main__":
    main()
