from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List
from src.trie import Trie
from src.fuzzy_search import fuzzy_search
from src.init_data import load_demo_data, populate_trie
import uvicorn
from fastapi.responses import HTMLResponse

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

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <meta charset="UTF-8">
            <title>In-Memory Search Engine</title>
            <style>
                body { font-family: "Helvetica Neue", Arial, sans-serif; background-color: #f5f5f5; margin: 0; padding: 0; }
                .container { max-width: 800px; margin: 50px auto; background: #fff; padding: 40px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
                h1 { color: #2c3e50; }
                p { line-height: 1.6; color: #555; }
                a { color: #007acc; text-decoration: none; }
                a:hover { text-decoration: underline; }
                .button { display: inline-block; padding: 10px 20px; margin: 10px 0; background: #007acc; color: #fff; border-radius: 5px; text-decoration: none; font-weight: bold; }
                ul { list-style-type: none; padding: 0; }
                li { margin: 8px 0; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>In-Memory Search Engine</h1>
                <p>
                    Welcome to a cutting-edge search engine designed for modern software engineering challenges.
                    Explore our powerful autocomplete and fuzzy search APIs, built for high-performance scenarios.
                </p>
                <p>
                    <a class="button" href="/docs">View API Documentation</a>
                </p>
                <h2>Try It Out</h2>
                <ul>
                    <li><a href="/autocomplete?prefix=commit">Autocomplete Example</a></li>
                    <li><a href="/fuzzy?query=cod%20revie&max_distance=2">Fuzzy Search Example</a></li>
                </ul>
                <p>
                    Discover how seamlessly our endpoints respond with real search terms and elevate your projects with innovative search capabilities.
                </p>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
