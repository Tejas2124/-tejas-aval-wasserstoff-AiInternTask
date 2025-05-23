import os 
import pinecone
from app.config import settings

from pinecone import Pinecone,ServerlessSpec

# Initialize Pinecone 
pc = Pinecone(api_key=settings.PINECONE_API_KEY)

if settings.INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=settings.INDEX_NAME,
        dimension=1536,  # Use your vector dimension here
        metric='cosine',  # or 'euclidean', 'dotproduct'
        spec=ServerlessSpec(
            cloud='aws',   # or 'gcp' depending on your setup
            region='us-east-1'  # your env, e.g. 'us-west1-gcp'
        )
    )




index = pc.Index(settings.INDEX_NAME)

def upsert_embedding(doc_id, chunk, embedding, metadata):
    index.upsert([
        {
            "id": f"{doc_id}_{metadata['chunk']}",
            "values": embedding,
            "metadata": metadata
        }
    ])

def query_embedding(embedding, top_k=5):
    res = index.query(vector=embedding, top_k=top_k, include_metadata=True)
    return res['matches']

# index_name = "quickstart"

# pc.create_index(
#     name=index_name,
#     dimension=, # Replace with your model dimensions
#     metric="cosine", # Replace with your model metric
#     spec=ServerlessSpec(
#         cloud="aws",
#         region="us-east-1"
#     ) 
# )