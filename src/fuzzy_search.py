"""
Fuzzy Search Module

This module implements fuzzy search capabilities to handle misspelled queries.
It uses the Levenshtein distance algorithm to suggest corrections and retrieve close matches.

Functions:
    fuzzy_search(query, max_distance): Returns words that are within max_distance from the query.
"""

from Levenshtein import distance

def levenshtein(s1, s2):
    # Compute Levenshtein distance using dynamic programming
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],    # Deletion
                                   dp[i][j-1],    # Insertion
                                   dp[i-1][j-1])  # Substitution
    return dp[m][n]

# Try to import the fast python-Levenshtein module.
try:
    import Levenshtein
    calc_distance = Levenshtein.distance
except ImportError:
    calc_distance = levenshtein

def fuzzy_search(query: str, max_distance: int, words: list) -> list:
    """
    Perform fuzzy search using Levenshtein distance.
    Returns a list of tuples (word, similarity_score).
    Score is calculated as 1 - (distance / max(len(query), len(word))).
    """
    matches = []
    for word in words:
        dist = distance(query.lower(), word.lower())
        if dist <= max_distance:
            # Calculate similarity score (1 is perfect match, 0 is completely different)
            max_len = max(len(query), len(word))
            similarity = 1 - (dist / max_len)
            matches.append((word, similarity))
    
    # Sort by similarity score (highest first)
    matches.sort(key=lambda x: x[1], reverse=True)
    return matches