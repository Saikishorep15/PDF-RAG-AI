import os
import streamlit as st

from utils.export import export_as_txt, export_as_markdown
from utils.pdf_loader import load_pdf
from utils.embedding import create_embeddings
from utils.vector_store import create_vector_store
from utils.rag import ask_question
from utils.statistics import get_pdf_statistics
from utils.summary import generate_summary


# -------------------------------------------------
# Page Config
# -------------------------------------------------

st.set_page_config(
    page_title="PDF RAG AI Assistant",
    page_icon="📄",
    layout="wide"
)

# -------------------------------------------------
# Session State
# -------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "pdf_name" not in st.session_state:
    st.session_state.pdf_name = None

if "documents" not in st.session_state:
    st.session_state.documents = None

if "pdf_stats" not in st.session_state:
    st.session_state.pdf_stats = None

# -------------------------------------------------
# Sidebar
# -------------------------------------------------

with st.sidebar:

    st.title("📄 PDF RAG AI")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        if st.session_state.pdf_name != uploaded_file.name:

            os.makedirs("uploads", exist_ok=True)

            pdf_path = os.path.join(
                "uploads",
                uploaded_file.name
            )

            with open(pdf_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            with st.spinner("📚 Processing PDF..."):

                documents = load_pdf(pdf_path)

                st.session_state.documents = documents

                embeddings = create_embeddings()

                st.session_state.vector_store = create_vector_store(
                    documents,
                    embeddings
                )

                st.session_state.pdf_stats = get_pdf_statistics(
                    pdf_path,
                    documents
                )

            st.session_state.pdf_name = uploaded_file.name

            st.success("✅ PDF processed successfully!")

    st.divider()

    st.subheader("Current PDF")

    if st.session_state.pdf_name:
        st.success(st.session_state.pdf_name)
    else:
        st.info("No PDF Uploaded")

    # -------------------------------------
    # Statistics
    # -------------------------------------

    if st.session_state.pdf_stats:

        stats = st.session_state.pdf_stats

        st.divider()

        st.subheader("📊 PDF Statistics")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Pages", stats["pages"])
            st.metric("Chunks", stats["chunks"])
            st.metric("Words", stats["words"])

        with col2:
            st.metric("Size (KB)", stats["size"])
            st.metric("Vector DB", stats["vector_db"])
            st.metric("AI Model", stats["ai_model"])

    st.divider()

    # -------------------------------------
    # Summary
    # -------------------------------------

    if st.button(
        "📝 Generate PDF Summary",
        use_container_width=True
    ):

        if st.session_state.documents:

            with st.spinner("Generating summary..."):

                summary = generate_summary(
                    st.session_state.documents
                )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": "## 📄 PDF Summary\n\n" + str(summary)
                }
            )

            st.rerun()

    # -------------------------------------
    # Export Chat
    # -------------------------------------

    st.divider()

    st.subheader("📥 Export Chat")

    if st.session_state.messages:

        txt_data = export_as_txt(
            st.session_state.messages
        )

        md_data = export_as_markdown(
            st.session_state.messages
        )

        st.download_button(
            "⬇ Download TXT",
            txt_data,
            "pdf_rag_chat.txt",
            "text/plain",
            use_container_width=True
        )

        st.download_button(
            "⬇ Download Markdown",
            md_data,
            "pdf_rag_chat.md",
            "text/markdown",
            use_container_width=True
        )

    st.divider()

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()

# -------------------------------------------------
# Main Screen
# -------------------------------------------------
st.title("🤖 PDF RAG AI Assistant")

st.caption(
    "Chat with your PDF using Retrieval-Augmented Generation (RAG) powered by Gemini."
)

# -------------------------------------------------
# Display Previous Chat
# -------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# -------------------------------------------------
# Chat Input
# -------------------------------------------------

question = st.chat_input(
    "Ask anything about your PDF..."
)

if question:

    if st.session_state.vector_store is None:

        st.warning("⚠ Please upload a PDF first.")

    else:

        # -------------------------
        # User Message
        # -------------------------

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):

            st.markdown(question)

        # -------------------------
        # Assistant Message
        # -------------------------

        with st.chat_message("assistant"):

            with st.spinner("🤖 Thinking..."):

                answer, docs = ask_question(
                    question,
                    st.session_state.vector_store
                )

                if isinstance(answer, list):

                    final_answer = ""

                    for item in answer:

                        if isinstance(item, dict):

                            final_answer += item.get("text", "")

                        elif hasattr(item, "text"):

                            final_answer += item.text

                        else:

                            final_answer += str(item)

                else:

                    final_answer = str(answer)

                st.markdown(final_answer)

                                # ---------------------------------
                # Sources Used
                # ---------------------------------

                with st.expander("📄 Sources Used"):

                    for i, doc in enumerate(docs, start=1):

                        st.markdown(f"### Source {i}")

                        st.write(doc.page_content)

                        if "page" in doc.metadata:

                            st.caption(
                                f"📄 Page {doc.metadata['page'] + 1}"
                            )

                        st.divider()

        # ---------------------------------
        # Save Assistant Response
        # ---------------------------------

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": final_answer
            }
        )
