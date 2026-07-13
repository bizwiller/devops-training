from fastapi import FastAPI
import uuid
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = FastAPI(title=os.getenv("APP_NAME", "url-shortener"))

# In-memory database (for learning)
db = {}

@app.post("/shorten")
def shorten(url: str):
    code = uuid.uuid4().hex[:6]
    db[code] = url
    return {"short_url": f"http://localhost/{code}"}

@app.get("/{code}")
def redirect(code: str):
    url = db.get(code)
    if url:
        return {"redirect_to": url}
    return {"error": "not-found"}
