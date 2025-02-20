//// filepath: /Users/cjacobson/git/in-memory-se/docs/design.md
# In-Memory Search Engine Design Document

## 1. High-Level Architectural Overview
The system is divided into two main components:
- **Autocomplete:** Uses a trie data structure for quick prefix matching.
- **Fuzzy Search:** Uses Levenshtein distance to handle typos and find near-matches.

### System Diagram:
     +-----------------------+
     |      main.py          |
     +-----------+-----------+
                 |
      +----------v-----------+
      |   Trie (trie.py)     | <--- fast prefix matching
      +----------+-----------+
                 |
      +----------v-----------+
      | Fuzzy Search (fuzzy_search.py) | <--- typo corrections & suggestions
      +-----------------------+
                 |
           [Data Source: In-memory dataset]

## 2. Trie for Fast Autocomplete
- **Motivation:** A trie efficiently stores strings allowing O(m) lookup time, where m is the length of the prefix.
- **Implementation:** Each node in the trie contains children mapped by characters and a flag for end-of-word.
- **Pseudocode (Insertion):**