import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def generate_answer(context, question):
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0,
    )

    prompt = f"""
You are a helpful PDF assistant.

Answer ONLY using the information from the context.

If the answer is not in the context, reply:
"I couldn't find that information in the PDF."

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    # Latest Gemini returns a list of content blocks
    if isinstance(response.content, list):
        text = ""

        for item in response.content:
            if isinstance(item, dict):
                text += item.get("text", "")
            elif hasattr(item, "text"):
                text += item.text

        return text.strip()

    return str(response.content).strip()