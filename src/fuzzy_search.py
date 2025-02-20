"""
Fuzzy Search Module

This module implements fuzzy search capabilities to handle misspelled queries.
It uses the Levenshtein distance algorithm to suggest corrections and retrieve close matches.

Functions:
    fuzzy_search(query, max_distance): Returns words that are within max_distance from the query.
"""

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

def fuzzy_search(query, max_distance=2, word_list=None):
    # If no word_list is provided, assume calling context supplies words
    if word_list is None:
        return []  # or raise an error; depends on design
    results = []
    for word in word_list:
        if levenshtein(query, word) <= max_distance:
            results.append(word)
    return results