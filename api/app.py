import time
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
        "software engineering tasks. The API provides both advanced autocomplete and fuzzy search endpoints, "
        "returning detailed metadata."
    ),
    version="0.1.0"
)

# Response Models with extended metadata
class AutocompleteResponse(BaseModel):
    query: str
    results: List[str]
    execution_time_ms: float = Field(..., description="Execution time in milliseconds")
    algorithm: str = Field("Trie Search", description="Search algorithm used")
    cache_used: bool = Field(False, description="Was the result served from cache?")

class FuzzyMatch(BaseModel):
    term: str
    score: float = Field(..., description="Similarity score (0-1) between query and term")

class FuzzyResponse(BaseModel):
    query: str
    results: List[FuzzyMatch]
    execution_time_ms: float = Field(..., description="Execution time in milliseconds")
    algorithm: str = Field("Levenshtein Distance", description="Search algorithm used")

# Initialize trie with demo data
trie = Trie()
demo_words = load_demo_data("./data/demo_data.json")
populate_trie(trie, demo_words)

@app.get("/autocomplete", response_model=AutocompleteResponse, summary="Advanced Autocomplete Search")
def autocomplete(
    prefix: str = Query(
        ...,
        example="co",
        description="A realistic prefix, e.g., 'co' might match 'commit', 'code review', etc."
    )
):
    start_time = time.time()
    results = trie.search(prefix)
    if not results:
        raise HTTPException(status_code=404, detail="No matches found")
    execution_time = (time.time() - start_time) * 1000  # Convert to ms
    return AutocompleteResponse(
        query=prefix,
        results=results,
        execution_time_ms=round(execution_time, 2)
    )

@app.get("/fuzzy", response_model=FuzzyResponse, summary="Advanced Fuzzy Search")
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
    start_time = time.time()
    # Assume fuzzy_search returns a list of tuples: (word, score)
    fuzzy_results = fuzzy_search(query, max_distance, demo_words)
    if not fuzzy_results:
        raise HTTPException(status_code=404, detail="No near matches found")
    execution_time = (time.time() - start_time) * 1000
    matches = [FuzzyMatch(term=term, score=round(score, 2)) for term, score in fuzzy_results]
    return FuzzyResponse(
        query=query,
        results=matches,
        execution_time_ms=round(execution_time, 2)
    )

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
          .examples-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 2rem;
            margin-top: 2rem;
          }
          .example-set {
            background: #f9f9f9;
            border: 1px solid var(--border-color);
            border-radius: 0.5rem;
            padding: 1.5rem;
          }
          .example-list {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
          }
          .example-item {
            background: #fff;
            padding: 1rem;
            border-radius: 0.375rem;
            border: 1px solid var (--border-color);
          }
          .example-item h3 {
            margin-top: 0;
            font-size: 1rem;
            color: var(--primary-color);
          }
          .example-desc {
            font-size: 0.875rem;
            color: #666;
            margin: 0.5rem 0;
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
            <a href="/docs" class="button" target="_blank">View API Documentation</a>
          </div>
          <div class="examples-grid">
            <div class="example-set">
              <h2>Autocomplete Examples</h2>
              <p>Try these examples to see prefix-based search in action:</p>
              <div class="example-list">
                <div class="example-item">
                  <h3>Development Terms</h3>
                  <pre class="code-block">/autocomplete?prefix=co</pre>
                  <p class="example-desc">Matches: commit, code review, container</p>
                  <a href="/autocomplete?prefix=co" class="button" target="_blank">Try it</a>
                </div>
                <div class="example-item">
                  <h3>Testing Related</h3>
                  <pre class="code-block">/autocomplete?prefix=test</pre>
                  <p class="example-desc">Matches: test, testing, test suite</p>
                  <a href="/autocomplete?prefix=test" class="button" target="_blank">Try it</a>
                </div>
                <div class="example-item">
                  <h3>DevOps Terms</h3>
                  <pre class="code-block">/autocomplete?prefix=de</pre>
                  <p class="example-desc">Matches: deploy, deployment, debug</p>
                  <a href="/autocomplete?prefix=de" class="button" target="_blank">Try it</a>
                </div>
                <div class="example-item">
                  <h3>Agile Terms</h3>
                  <pre class="code-block">/autocomplete?prefix=ag</pre>
                  <p class="example-desc">Matches: agile, agile sprint, agile planning</p>
                  <a href="/autocomplete?prefix=ag" class="button" target="_blank">Try it</a>
                </div>
              </div>
            </div>

            <div class="example-set">
              <h2>Fuzzy Search Examples</h2>
              <p>Explore these examples to see typo-tolerant searching:</p>
              <div class="example-list">
                <div class="example-item">
                  <h3>Basic Typo</h3>
                  <pre class="code-block">/fuzzy?query=comit&max_distance=1</pre>
                  <p class="example-desc">Finds: "commit" (1 character off)</p>
                  <a href="/fuzzy?query=comit&max_distance=1" class="button" target="_blank">Try it</a>
                </div>
                <div class="example-item">
                  <h3>Multiple Words</h3>
                  <pre class="code-block">/fuzzy?query=cod%20reviw&max_distance=2</pre>
                  <p class="example-desc">Finds: "code review" (2 characters off)</p>
                  <a href="/fuzzy?query=cod%20reviw&max_distance=2" class="button" target="_blank">Try it</a>
                </div>
                <div class="example-item">
                  <h3>Complex Match</h3>
                  <pre class="code-block">/fuzzy?query=depoymnt&max_distance=2</pre>
                  <p class="example-desc">Finds: "deployment" (2 characters off)</p>
                  <a href="/fuzzy?query=depoymnt&max_distance=2" class="button" target="_blank">Try it</a>
                </div>
                <div class="example-item">
                  <h3>Advanced Search</h3>
                  <pre class="code-block">/fuzzy?query=integation%20tst&max_distance=3</pre>
                  <p class="example-desc">Finds: "integration test" (3 characters off)</p>
                  <a href="/fuzzy?query=integation%20tst&max_distance=3" class="button" target="_blank">Try it</a>
                </div>
              </div>
            </div>
          </div>
        </main>
        <footer>
          &copy; 2025 In-Memory Search Engine. All rights reserved.
        </footer>
      </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
