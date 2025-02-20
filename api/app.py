from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List
from src.trie import Trie
from src.fuzzy_search import fuzzy_search
import uvicorn

app = FastAPI(
    title="In-Memory Search Engine API",
    description="Provides autocomplete and fuzzy search endpoints for in-memory search capabilities.",
    version="0.1.0"
)

# Response Models
class SearchResponse(BaseModel):
    results: List[str]

# Initialize search structures.
trie = Trie()
words = ["apple", "application", "apt", "hello", "help", "helium"]
for word in words:
    trie.insert(word)

@app.get("/autocomplete", response_model=SearchResponse, summary="Autocomplete Search")
def autocomplete(
    prefix: str = Query(..., example="hel", description="The prefix string to search for autocomplete suggestions")
):
    """
    Returns a list of words that begin with the given prefix.
    """
    results = trie.search(prefix)
    if not results:
        raise HTTPException(status_code=404, detail="No matches found")
    return {"results": results}

@app.get("/fuzzy", response_model=SearchResponse, summary="Fuzzy Search")
def fuzzy(
    query: str = Query(..., example="helo", description="The query string for fuzzy matching"),
    max_distance: int = Query(2, example=1, description="Maximum allowed edit distance for fuzzy matching")
):
    """
    Returns a list of near-matching words based on the query string using fuzzy search.
    """
    results = fuzzy_search(query, max_distance, words)
    if not results:
        raise HTTPException(status_code=404, detail="No near matches found")
    return {"results": results}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
