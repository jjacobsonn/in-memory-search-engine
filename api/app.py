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

# Professional, modern landing page using semantic HTML and lightweight design.
@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html lang="en">
      <head>
        <meta charset="UTF-8">
        <title>In-Memory Search Engine</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
        <style>
          :root {
            --primary-color: #0a74da;
            --primary-hover: #075ea8;
            --bg-color: #ffffff;
            --text-color: #333;
            --accent-color: #ff9800;
            --border-color: #e0e0e0;
            --box-shadow: 0 2px 8px rgba(0,0,0,0.1);
          }
          body {
            margin: 0;
            padding: 0;
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
          }
          header {
            background: var(--primary-color);
            color: #fff;
            padding: 2rem 0;
            text-align: center;
          }
          header h1 {
            margin: 0;
            font-size: 2.5rem;
          }
          header p {
            margin: 0.5rem 0 0;
            font-size: 1.125rem;
          }
          main {
            max-width: 800px;
            margin: 2rem auto;
            padding: 0 1rem;
          }
          .cta {
            text-align: center;
            margin: 2rem 0;
          }
          .button {
            background: var(--primary-color);
            color: #fff;
            padding: 0.75rem 1.5rem;
            border-radius: 0.375rem;
            text-decoration: none;
            font-weight: 600;
            transition: background-color 0.3s, transform 0.2s;
            display: inline-block;
          }
          .button:hover {
            background: var(--primary-hover);
            transform: translateY(-2px);
          }
          section.examples {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
            margin-top: 2rem;
          }
          .example {
            background: #f9f9f9;
            border: 1px solid var(--border-color);
            border-radius: 0.5rem;
            padding: 1rem;
            transition: transform 0.3s, box-shadow 0.3s;
          }
          .example:hover {
            transform: translateY(-4px);
            box-shadow: var(--box-shadow);
          }
          .example h2 {
            margin-top: 0;
            font-size: 1.25rem;
            font-weight: 600;
          }
          .code-block {
            display: block;
            background: #f0f0f0;
            padding: 0.5rem;
            border-radius: 0.375rem;
            font-family: monospace;
            font-size: 0.875rem;
            overflow-x: auto;
            margin: 0.5rem 0;
          }
          footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.875rem;
            color: #777;
          }
          @media (max-width: 640px) {
            section.examples {
              grid-template-columns: 1fr;
            }
          }
        </style>
      </head>
      <body>
        <header>
          <h1>In-Memory Search Engine</h1>
          <p>Efficient. Dynamic. Innovative.</p>
        </header>
        <main>
          <div class="cta">
            <a href="/docs" class="button">View API Documentation</a>
          </div>
          <section class="examples">
            <div class="example">
              <h2>Autocomplete</h2>
              <p>Endpoint:</p>
              <pre class="code-block">/autocomplete?prefix=commit</pre>
              <div style="text-align:center; margin-top: 1rem;">
                <a href="/autocomplete?prefix=commit" class="button">Test Autocomplete</a>
              </div>
            </div>
            <div class="example">
              <h2>Fuzzy Search</h2>
              <p>Endpoint:</p>
              <pre class="code-block">/fuzzy?query=cod%20revie&amp;max_distance=2</pre>
              <div style="text-align:center; margin-top: 1rem;">
                <a href="/fuzzy?query=cod%20revie&amp;max_distance=2" class="button">Test Fuzzy Search</a>
              </div>
            </div>
          </section>
        </main>
        <footer>
          &copy; 2025 In-Memory Search Engine. All rights reserved.
        </footer>
      </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
