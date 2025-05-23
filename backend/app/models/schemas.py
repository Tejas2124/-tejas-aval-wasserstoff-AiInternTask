from pydantic import BaseModel
from typing import List

class QueryRequest(BaseModel):
    question: str

class Citation(BaseModel):
    doc_id: str
    page: int
    paragraph: int
    snippet: str

class QueryResponse(BaseModel):
    answer: str
    citations: List[Citation]