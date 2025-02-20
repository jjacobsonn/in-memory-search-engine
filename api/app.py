from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List
from src.trie import Trie
from src.fuzzy_search import fuzzy_search
from src.init_data import load_demo_data, populate_trie
import uvicorn

app = FastAPI(
    title="In-Memory Search Engine API",
    description=(
        "A high-performance in-memory search engine using realistic search data inspired by daily "
        "software engineering tasks. The API provides both autocomplete and fuzzy search endpoints."
    ),
    version="0.1.0"
)

# Response Model
class SearchResponse(BaseModel):
    results: List[str] = Field(
        ...,
        example=["commit", "code review", "CI/CD"],
        description="A list of matched search terms based on the query."
    )

# Initialize trie with demo data
trie = Trie()
demo_words = load_demo_data("./data/demo_data.json")
populate_trie(trie, demo_words)

@app.get("/autocomplete", response_model=SearchResponse, summary="Advanced Autocomplete Search")
def autocomplete(
    prefix: str = Query(
        ...,
        example="co",
        description="A realistic prefix, e.g., 'co' might match 'commit', 'code review', etc."
    )
):
    """
    Autocomplete Endpoint

    Returns a list of search terms that begin with the provided prefix based on realistic demo data.
    """
    results = trie.search(prefix)
    if not results:
        raise HTTPException(status_code=404, detail="No matches found")
    return {"results": results}

@app.get("/fuzzy", response_model=SearchResponse, summary="Advanced Fuzzy Search")
def fuzzy(
    query: str = Query(
        ...,
        example="cod revie",
        description="A realistic, possibly misspelled query. For example, 'cod revie' could match 'code review'."
    ),
    max_distance: int = Query(
        2,
        example=2,
        ge=1,
        le=5,
        description="Maximum allowed edit distance for fuzzy matching."
    )
):
    """
    Fuzzy Search Endpoint

    Returns near-matching search terms for typos in the query string using a Levenshtein algorithm.
    """
    results = fuzzy_search(query, max_distance, demo_words)
    if not results:
        raise HTTPException(status_code=404, detail="No near matches found")
    return {"results": results}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
