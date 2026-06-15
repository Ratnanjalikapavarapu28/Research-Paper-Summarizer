from langchain_chroma import Chroma


def store_chunks(chunks, embeddings):

    vector_db = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory="vector_store"
    )

    return vector_db


def retrieve_chunks(query, vector_db):

    docs = vector_db.similarity_search(
        query,
        k=3
    )

    return [doc.page_content for doc in docs]