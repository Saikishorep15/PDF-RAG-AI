from utils.gemini import generate_answer


def ask_question(question, vector_store):
    """
    Retrieve relevant chunks and return:
    - AI answer
    - Retrieved documents
    """

    docs = vector_store.similarity_search(
        query=question,
        k=4
    )

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    answer = generate_answer(
        context=context,
        question=question
    )

    return answer, docs