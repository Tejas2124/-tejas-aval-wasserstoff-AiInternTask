from fastapi import APIRouter, UploadFile, File
from app.models.schemas import QueryRequest, QueryResponse
from app.services.processor import process_pdf
from app.services.llm_service import answer_query_with_context

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    doc_id = await process_pdf(file)
    return {"status": "success", "doc_id": doc_id}

@router.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    response = await answer_query_with_context(request.question)
    return response
