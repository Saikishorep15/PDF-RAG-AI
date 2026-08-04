import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def generate_answer(context, question):
    """
    Generate an answer using Google Gemini.
    """

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY not found. Please configure it in your .env file or Streamlit Secrets."
        )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=api_key,
        temperature=0,
    )

    prompt = f"""
You are a helpful PDF assistant.

Use ONLY the information provided in the context.

If the answer is not available in the context, reply exactly:

"I couldn't find that information in the PDF."

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    if hasattr(response, "content"):
        return str(response.content).strip()

    return str(response).strip()