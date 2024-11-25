from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import faiss
import pickle
import numpy as np
import json
from fastapi.middleware.cors import CORSMiddleware

# Load data from the JSON file
with open('data.json', 'r') as f:
    loaded_data = json.load(f)

# Initialize the FastAPI app
app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods like POST, GET, etc.
    allow_headers=["*"],  # Allow all headers
)


# Load the SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load FAISS index and IDs
faiss_index = faiss.read_index('faiss_index.bin')
with open('data_ids.pkl', 'rb') as f:
    ids = pickle.load(f)

# Define the request data structure
class QueryInput(BaseModel):
    query: str

@app.get("/search/")
def search_query(query: str = Query(..., description="Search query text")):
    """
    Process the query string parameter and return relevant articles.
    """
    try:
        # Print query for debugging
        print(f"Received query: {query}")
        # Embed the query
        query_embedding = model.encode(query).reshape(1, -1)

        # Search for the top 5 most relevant articles
        distances, indices = faiss_index.search(query_embedding, k=5)

        relevant_articles = {}
        for idx in indices[0]:
            if idx < len(ids):
                article_id = ids[idx]
                #print(f"artcle id: {article_id}")
                article_details = loaded_data.get(str(article_id))
                if article_details:
                    relevant_articles[article_id] = article_details

        if relevant_articles:
            #print(f"return: {relevant_articles}")
            return {"query": query, "results": relevant_articles}
        else:
            return {"query":query, "message": "No relevant articles found",'r':article_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/")
def home():
    """Basic health check for the API."""
    return {"message": "Semantic Search API is running!"}
