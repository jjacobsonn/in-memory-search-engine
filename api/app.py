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
    results = fuzzy_search(query, max_distance, demo_words)
    if not results:
        raise HTTPException(status_code=404, detail="No near matches found")
    return {"results": results}

# Updated landing page with minimal, professional styling and styled endpoint examples.
@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
      <head>
        <meta charset="UTF-8">
        <title>In-Memory Search Engine</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
        <style>
          body {
            margin: 0;
            padding: 0;
            font-family: 'Roboto', sans-serif;
            background-color: #fafafa;
            color: #333;
          }
          .container {
            max-width: 900px;
            margin: 50px auto;
            background-color: #fff;
            padding: 40px;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
          }
          .header {
            text-align: center;
            margin-bottom: 30px;
          }
          .header img {
            max-width: 100px;
            margin-bottom: 10px;
          }
          h1 {
            font-size: 2.2em;
            margin: 0;
          }
          .button {
            background-color: #007acc;
            color: #fff;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 4px;
            display: inline-block;
            margin: 10px 0;
          }
          .examples {
            margin-top: 30px;
          }
          .example {
            background-color: #f5f5f5;
            border-radius: 4px;
            padding: 15px;
            margin-bottom: 20px;
          }
          .example h3 {
            margin-top: 0;
            font-size: 1.2em;
          }
          .code-block {
            background-color: #eee;
            color: #c7254e;
            padding: 5px 10px;
            border-radius: 4px;
            font-family: monospace;
            font-size: 0.9em;
            overflow-x: auto;
            display: inline-block;
          }
        </style>
      </head>
      <body>
        <div class="container">
          <div class="header">
            <img src="https://via.placeholder.com/100?text=Logo" alt="Logo">
            <h1>In-Memory Search Engine</h1>
            <p>A cutting-edge search solution designed for modern software engineering challenges.</p>
          </div>
          <div style="text-align: center;">
            <a class="button" href="/docs">View API Documentation</a>
          </div>
          <div class="examples">
            <div class="example">
              <h3>Autocomplete Example</h3>
              <p>Endpoint:</p>
              <pre class="code-block">/autocomplete?prefix=commit</pre>
              <a class="button" href="/autocomplete?prefix=commit">Test Autocomplete</a>
            </div>
            <div class="example">
              <h3>Fuzzy Search Example</h3>
              <p>Endpoint:</p>
              <pre class="code-block">/fuzzy?query=cod%20revie&amp;max_distance=2</pre>
              <a class="button" href="/fuzzy?query=cod%20revie&amp;max_distance=2">Test Fuzzy Search</a>
            </div>
          </div>
        </div>
      </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
