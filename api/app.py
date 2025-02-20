from fastapi import FastAPI, HTTPException
from src.trie import Trie
from src.fuzzy_search import fuzzy_search
import uvicorn

app = FastAPI(title="In-Memory Search Engine API")

# Initialize search structures.
trie = Trie()
words = ["apple", "application", "apt", "hello", "help", "helium"]
for word in words:
    trie.insert(word)

@app.get("/autocomplete")
def autocomplete(prefix: str):
    results = trie.search(prefix)
    if not results:
        raise HTTPException(status_code=404, detail="No matches found")
    return {"results": results}

@app.get("/fuzzy")
def fuzzy(query: str, max_distance: int = 2):
    results = fuzzy_search(query, max_distance, words)
    if not results:
        raise HTTPException(status_code=404, detail="No near matches found")
    return {"results": results}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
