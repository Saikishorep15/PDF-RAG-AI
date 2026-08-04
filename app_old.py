import streamlit as st
from utils.pdf_loader import load_pdf
from utils.embedding import create_embeddings
from utils.vector_store import create_vector_store
from utils.rag import ask_question

st.set_page_config(
    page_title="PDF RAG AI",
    page_icon="📄",
    layout="wide"
)

st.title("📄 PDF RAG AI Assistant")
st.markdown("Upload a PDF and ask questions using Gemini AI.")

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

uploaded_pdf = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

if uploaded_pdf is not None:

    with st.spinner("Reading PDF..."):

        documents = load_pdf(uploaded_pdf)

        embeddings = create_embeddings()

        vector_store = create_vector_store(
            documents,
            embeddings
        )

        st.session_state.vector_store = vector_store

    st.success("✅ PDF processed successfully!")

st.divider()

question = st.text_input(
    "Ask your question"
)

if st.button("Ask"):

    if st.session_state.vector_store is None:
        st.warning("Upload a PDF first.")
    elif question == "":
        st.warning("Enter a question.")
    else:

        with st.spinner("Generating Answer..."):

            answer = ask_question(
                question,
                st.session_state.vector_store
            )

        st.markdown("## Answer")

        st.write(answer)