import ollama

def generate_answer(context, question):

    # safety limit (VERY IMPORTANT for LLM stability)
    context = context[:3000]

    prompt = f"""
You are an AI assistant helping with research papers.

Use ONLY the context below to answer.

Context:
{context}

Question:
{question}

Answer clearly and concisely:
"""

    try:
        response = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"Error generating answer: {str(e)}"