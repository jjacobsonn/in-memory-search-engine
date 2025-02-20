import pytest
from src.fuzzy_search import fuzzy_search

@pytest.fixture(scope="module")
def test_words():
    """Fixture to provide test data."""
    return ["hello", "help", "world", "fuzzy"]

def test_fuzzy_exact_match(test_words):
    """Verify exact matches return perfect similarity scores."""
    results = fuzzy_search("hello", max_distance=0, words=test_words)
    assert len(results) == 1, "Expected exactly one exact match"
    word, score = results[0]
    assert word == "hello"
    assert score == 1.0, "Exact match should have similarity score of 1.0"

def test_fuzzy_near_match(test_words):
    """Verify near matches are found with appropriate similarity scores."""
    results = fuzzy_search("helo", max_distance=1, words=test_words)
    assert results, "Expected at least one near match"
    # Check if "hello" is the best match
    best_match, score = results[0]
    assert best_match == "hello", "Expected 'hello' as best match for 'helo'"
    assert score > 0.7, "Expected high similarity score for near match"

def test_fuzzy_no_matches(test_words):
    """Verify no matches are returned when edit distance is too large."""
    results = fuzzy_search("zzzzz", max_distance=1, words=test_words)
    assert results == [], "Expected no matches for dissimilar string"

def test_fuzzy_multiple_matches(test_words):
    """Verify multiple matches are returned in order of similarity."""
    results = fuzzy_search("hel", max_distance=2, words=test_words)
    assert len(results) >= 2, "Expected multiple matches"
    scores = [score for _, score in results]
    assert sorted(scores, reverse=True) == scores, "Results should be sorted by descending similarity"
