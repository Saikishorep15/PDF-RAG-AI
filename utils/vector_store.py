from langchain_chroma import Chroma


def create_vector_store(documents, embeddings):
    """
    Create a Chroma vector database from the document chunks.
    """

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory="chroma_db",
    )

    return vector_store