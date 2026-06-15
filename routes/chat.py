from services.rag_service import retrieve_chunks
from services.llm_service import generate_answer


def ask_question(query, vector_db):

    chunks = retrieve_chunks(query, vector_db)

    if not chunks:
        return "No relevant information found"

    context = " ".join(chunks[:3])

    return generate_answer(context, query)