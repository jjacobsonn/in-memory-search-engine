from trie import Trie
from fuzzy_search import fuzzy_search

def main():
    # Build trie with sample words
    words = ["hello", "help", "helmet", "hero", "heron"]
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    # Autocomplete sample: search by prefix
    prefix = "he"
    autocomplete_results = trie.search(prefix)
    print("Autocomplete results for '{}':".format(prefix), autocomplete_results)
    
    # Fuzzy search sample: assuming user may type a misspelled word
    query = "hela"
    fuzzy_results = fuzzy_search(query, max_distance=1, word_list=words)
    print("Fuzzy search results for '{}':".format(query), fuzzy_results)

if __name__ == "__main__":
    main()
