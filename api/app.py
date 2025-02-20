from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List
from src.trie import Trie
from src.fuzzy_search import fuzzy_search
import uvicorn

app = FastAPI(
    title="In-Memory Search Engine API",
    description=(
        "A high-performance in-memory search engine exposing endpoints for both autocomplete "
        "and fuzzy search. This API leverages trie-based structures and advanced fuzzy matching "
        "algorithms to provide near-real-time search assistance, similar to systems deployed in major tech companies."
    ),
    version="0.1.0"
)

# Response Models with technical documentation for each field
class SearchResponse(BaseModel):
    results: List[str] = Field(
        ...,
        example=["apple", "application", "apt"],
        description="A list of matched words based on the search query."
    )

# Initialize core search structures using a trie for fast prefix lookup.
trie = Trie()
# Example dataset; in a production system, this might be populated dynamically or pre-indexed.
words = ["apple", "application", "apt", "hello", "help", "helium", "applet", "apply", "approach", "aptitude"]
for word in words:
    trie.insert(word)

@app.get("/autocomplete", response_model=SearchResponse, summary="Advanced Autocomplete Search")
def autocomplete(
    prefix: str = Query(
        ...,
        example="appl",
        description="The prefix string for which the API returns autocomplete suggestions. "
                    "For instance, 'appl' may match 'apple', 'application', 'applet', etc."
    )
):
    """
    Autocomplete Endpoint

    This endpoint returns a list of words that start with the provided prefix. The trie-based index enables
    rapid lookup even in large datasets. If no words match the prefix, the API returns a 404 error.

    Example:
    - Request: /autocomplete?prefix=appl
    - Response: { "results": ["apple", "application", "applet", "apply"] }

    This endpoint is optimized for real-time search interfaces.
    """
    results = trie.search(prefix)
    if not results:
        raise HTTPException(status_code=404, detail="No matches found")
    return {"results": results}

@app.get("/fuzzy", response_model=SearchResponse, summary="Advanced Fuzzy Search")
def fuzzy(
    query: str = Query(
        ...,
        example="helo",
        description="The query string for fuzzy matching. Ideal for handling typos or approximate string matching. "
                    "This is processed using an optimized Levenshtein distance algorithm."
    ),
    max_distance: int = Query(
        2,
        example=2,
        ge=1,
        le=5,
        description="The maximum allowed edit distance for fuzzy matching. A smaller value indicates stricter matching."
    )
):
    """
    Fuzzy Search Endpoint

    This endpoint returns a list of words that are near-matches to the provided query string. It uses a dynamic
    programming implementation of the Levenshtein distance algorithm, with a fast fallback when available. This feature
    supports robust typo correction and approximate matching.

    Example:
    - Request: /fuzzy?query=helo&max_distance=2
    - Response: { "results": ["hello", "help"] }

    Use this endpoint to build user interfaces that can suggest corrections for misspelled terms.
    """
    results = fuzzy_search(query, max_distance, words)
    if not results:
        raise HTTPException(status_code=404, detail="No near matches found")
    return {"results": results}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
