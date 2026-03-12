import json
import numpy as np
import faiss

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from sentence_transformers import SentenceTransformer
from openai import OpenAI


# -----------------------------
# CONFIG
# -----------------------------

DATA_FILE = "products.json"
TOP_K = 5

import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# -----------------------------
# FASTAPI APP
# -----------------------------

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# -----------------------------
# LOAD DATASET
# -----------------------------

with open(DATA_FILE, "r") as f:
    products = json.load(f)


# -----------------------------
# EMBEDDING MODEL
# -----------------------------

model = SentenceTransformer("all-MiniLM-L6-v2")


# -----------------------------
# CREATE TEXT FOR EMBEDDINGS
# -----------------------------

texts = [
    f"{p['name']} {p['category']} {p['description']}"
    for p in products
]


# -----------------------------
# GENERATE EMBEDDINGS
# -----------------------------

embeddings = model.encode(texts)

dimension = embeddings.shape[1]


# -----------------------------
# CREATE FAISS INDEX
# -----------------------------

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings).astype("float32"))


# -----------------------------
# REQUEST MODEL
# -----------------------------

class Query(BaseModel):
    query: str


# -----------------------------
# FRONTEND PAGE
# -----------------------------

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


# -----------------------------
# SEARCH API
# -----------------------------

@app.post("/search")
def search(query: Query):

    # Convert query → embedding
    q_embedding = model.encode([query.query])

    # Search FAISS
    D, I = index.search(
        np.array(q_embedding).astype("float32"),
        TOP_K
    )

    results = [products[i] for i in I[0]]

    # Build context for LLM
    context = "\n".join([
        f"{r['name']} | {r['category']} | {r['description']}"
        for r in results
    ])

    prompt = f"""
User query: {query.query}

Relevant products:
{context}

Recommend the best products and explain briefly.
"""

    # LLM generation
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    answer = response.choices[0].message.content

    return {
        "results": results,
        "recommendation": answer
    }