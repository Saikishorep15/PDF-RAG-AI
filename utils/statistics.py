import os
import fitz


def get_pdf_statistics(pdf_path, documents):
    """
    Returns statistics about the uploaded PDF.
    """

    pdf = fitz.open(pdf_path)

    total_pages = len(pdf)

    total_chunks = len(documents)

    total_words = sum(
        len(doc.page_content.split())
        for doc in documents
    )

    file_size = round(
        os.path.getsize(pdf_path) / 1024,
        2
    )

    pdf.close()

    return {
        "pages": total_pages,
        "chunks": total_chunks,
        "words": total_words,
        "size": file_size,
        "embedding_model": "all-MiniLM-L6-v2",
        "vector_db": "ChromaDB",
        "ai_model": "Gemini"
    }