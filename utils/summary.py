from utils.gemini import generate_answer


def generate_summary(documents):
    """
    Generate an AI summary of the PDF.
    """

    context = "\n\n".join(
        doc.page_content
        for doc in documents[:15]
    )

    prompt = """
Summarize this PDF.

Include:

• Main topic

• Important points

• Key people

• Key numbers

• Conclusion

Keep it under 300 words.
"""

    return generate_answer(
        context=context,
        question=prompt
    )