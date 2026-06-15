from services.llm_service import generate_answer


def generate_summary_for_documents(documents):

    if not documents:
        return "No documents found"

    document_summaries = []

    # Step 1: Generate summary for each PDF
    for doc in documents:

        file_name = doc["name"]
        text = doc["text"]

        # Limit context size for faster response
        context = text[:3000]

        question = f"""
        Summarize this document clearly.
        Mention the important topics covered.
        """

        summary = generate_answer(
            context,
            question
        )

        document_summaries.append(
            f"Document: {file_name}\n{summary}"
        )

    # Step 2: Combine all summaries
    combined_context = "\n\n".join(document_summaries)

    final_question = """
    Create one final summary covering ALL uploaded documents.

    Mention:
    - Main topics from each document
    - Key concepts
    - Overall understanding

    Keep the summary concise and easy to understand.
    """

    final_summary = generate_answer(
        combined_context,
        final_question
    )

    return final_summary