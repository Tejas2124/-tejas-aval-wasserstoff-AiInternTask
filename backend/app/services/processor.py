from uuid import uuid4
from app.services.ocr_service import extract_text_from_pdf_bytes
from app.services.chunk_service import chunk_text
from app.services.embedding_service import get_embedding
import time
from app.core.vector_store import upsert_embedding

async def process_pdf(file):
    pdf_bytes = await file.read()
    doc_id = str(uuid4())[:8]
    text = extract_text_from_pdf_bytes(pdf_bytes)
    chunks = chunk_text(text)
    for idx, chunk in enumerate(chunks):
        time.sleep(5)
        embedding = get_embedding(chunk)
        time.sleep(5)
        metadata = {"doc_id": doc_id, "page": idx+1, "chunk": idx+1, "text": chunk}
        time.sleep(5)
        upsert_embedding(doc_id, chunk, embedding, metadata)
        time.sleep(5)
    return doc_id