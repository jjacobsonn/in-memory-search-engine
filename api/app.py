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

# Updated landing page with a modern, animated, and professional feel.
@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
      <head>
        <meta charset="UTF-8">
        <title>In-Memory Search Engine</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
        <style>
          body {
            margin: 0;
            padding: 0;
            font-family: 'Roboto', sans-serif;
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: #f1f1f1;
          }
          .container {
            max-width: 900px;
            margin: 80px auto;
            background-color: rgba(0, 0, 0, 0.5);
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.37);
            backdrop-filter: blur(8px);
            text-align: center;
          }
          .logo {
            width: 80px;
            margin-bottom: 20px;
          }
          h1 {
            font-size: 2.8em;
            margin-bottom: 0.2em;
            animation: fadeInDown 1.5s;
          }
          p {
            font-size: 1.2em;
            line-height: 1.6;
            margin-bottom: 30px;
            color: #d1d1d1;
          }
          .button {
            background-color: #ff9800;
            color: #fff;
            padding: 12px 30px;
            border-radius: 50px;
            text-decoration: none;
            font-size: 1em;
            font-weight: bold;
            transition: background-color 0.3s ease;
            display: inline-block;
            margin: 10px;
          }
          .button:hover {
            background-color: #e68900;
          }
          .examples {
            margin-top: 40px;
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
          }
          .example {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 8px;
            width: 40%;
            margin: 10px;
            transition: transform 0.4s;
          }
          .example:hover {
            transform: scale(1.05);
          }
          @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
          }
          @media (max-width: 768px) {
            .example { width: 80%; }
          }
        </style>
      </head>
      <body>
        <div class="container">
            <!-- Optional logo; ensure /static/logo.png exists -->
            <img src="/static/logo.png" alt="Logo" class="logo">
            <h1 class="animate__animated animate__fadeInDown">In-Memory Search Engine</h1>
            <p>Experience a blazing-fast search solution, built with modern technical standards and designed to impress.</p>
            <a href="/docs" class="button animate__animated animate__pulse animate__infinite">API Documentation</a>
            <div class="examples">
                <div class="example animate__animated animate__fadeInLeft">
                    <h3>Autocomplete</h3>
                    <p>Example: <em>/autocomplete?prefix=commit</em></p>
                    <a href="/autocomplete?prefix=commit" class="button">Try Autocomplete</a>
                </div>
                <div class="example animate__animated animate__fadeInRight">
                    <h3>Fuzzy Search</h3>
                    <p>Example: <em>/fuzzy?query=cod%20revie&max_distance=2</em></p>
                    <a href="/fuzzy?query=cod%20revie&max_distance=2" class="button">Try Fuzzy Search</a>
                </div>
            </div>
        </div>
      </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
