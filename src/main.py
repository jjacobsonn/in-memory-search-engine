#!/usr/bin/env python3
def main():
    # Initialize and test trie functionality.
    from trie import Trie
    from fuzzy_search import fuzzy_search
    trie = Trie()
    words = ["hello", "help", "helium"]
    for word in words:
        trie.insert(word)
    print("Autocomplete results for 'hel':", trie.search("hel"))
    
    # Demonstrate fuzzy search.
    query = "helo"
    results = fuzzy_search(query, max_distance=1, word_list=words)
    print("Fuzzy search results for 'helo':", results)

if __name__ == "__main__":
    main()
