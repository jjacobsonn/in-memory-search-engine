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
            <link rel="stylesheet" 
              href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
            <style>
                body {
                    background-color: #ECEFF1;
                    margin: 0;
                    padding: 0;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                }
                .container {
                    max-width: 800px;
                    margin: 50px auto;
                    background-color: #fff;
                    border-radius: 10px;
                    box-shadow: 0px 20px 40px rgba(0,0,0,0.1);
                    overflow: hidden;
                }
                .header {
                    background: #1976d2;
                    color: #fff;
                    padding: 20px;
                    text-align: center;
                }
                .header img {
                    height: 50px;
                }
                .header h1 {
                    margin: 10px 0 0;
                    font-size: 2.2em;
                }
                .content {
                    padding: 30px;
                    text-align: center;
                }
                .button {
                    background: #1976d2;
                    color: #fff;
                    text-decoration: none;
                    padding: 15px 30px;
                    border-radius: 50px;
                    margin: 20px;
                    display: inline-block;
                    transition: background 0.3s ease;
                }
                .button:hover {
                    background: #1565c0;
                }
                .animated-button {
                    animation: pulse 2s infinite;
                }
                @keyframes pulse {
                    0% { transform: scale(1); }
                    50% { transform: scale(1.05); }
                    100% { transform: scale(1); }
                }
                .examples {
                    display: flex;
                    justify-content: space-around;
                    flex-wrap: wrap;
                    margin-top: 30px;
                }
                .example {
                    background: #f2f2f2;
                    border-radius: 10px;
                    padding: 20px;
                    width: 40%;
                    margin: 10px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <img src="/static/logo.png" alt="Logo">
                    <h1>In-Memory Search Engine</h1>
                    <p>Your cutting-edge search solution</p>
                </div>
                <div class="content">
                    <a class="button animated-button" href="/docs">API Documentation</a>
                    <div class="examples">
                        <div class="example animate__animated animate__fadeInLeft">
                            <h3>Autocomplete</h3>
                            <p>Try: <em>/autocomplete?prefix=commit</em></p>
                            <a class="button" href="/autocomplete?prefix=commit">Test Autocomplete</a>
                        </div>
                        <div class="example animate__animated animate__fadeInRight">
                            <h3>Fuzzy Search</h3>
                            <p>Try: <em>/fuzzy?query=cod%20revie&max_distance=2</em></p>
                            <a class="button" href="/fuzzy?query=cod%20revie&max_distance=2">Test Fuzzy Search</a>
                        </div>
                    </div>
                </div>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
