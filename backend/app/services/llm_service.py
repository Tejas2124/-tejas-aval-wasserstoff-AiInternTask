import openai
from app.services.embedding_service import get_embedding
from app.core.vector_store import query_embedding
from app.models.schemas import QueryResponse, Citation
from app.config import settings

async def answer_query_with_context(question: str) -> QueryResponse:
    query_vector = get_embedding(question)
    results = query_embedding(query_vector)

    context = ""
    citations = []
    for match in results:
        metadata = match["metadata"]
        context += f"[Doc {metadata['doc_id']} Pg {metadata['page']} ¶{metadata['chunk']}]\n"
        context += match["metadata"]["text"] + "\n\n"
        citations.append(Citation(
            doc_id=metadata["doc_id"],
            page=metadata["page"],
            paragraph=metadata["chunk"],
            snippet=metadata["text"][:200]
        ))

    prompt = f"""
    Given the following legal document context, answer the user query:

    Context:
    {context}

    Question: {question}
    Provide a cited and grounded answer.
    """

    openai.api_key = settings.OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-4.1-nano",
        messages=[
            {"role": "system", "content": "You are a helpful legal assistant."},
            {"role": "user", "content": prompt},
        ]
    )

    answer_text = response["choices"][0]["message"]["content"]
    return QueryResponse(answer=answer_text, citations=citations)
