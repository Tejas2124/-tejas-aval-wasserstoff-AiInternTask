import openai
from app.config import settings
import time 
openai.api_key = settings.OPENAI_API_KEY

def get_embedding(text):
    time.sleep(7)
    response = openai.Embedding.create(input=text, model="text-embedding-3-small")
    time.sleep(7)
    return response["data"][0]["embedding"]
