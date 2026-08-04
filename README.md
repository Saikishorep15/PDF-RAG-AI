# 📄 PDF-RAG-AI

An AI-powered PDF Question Answering Assistant built using **Streamlit**, **LangChain**, **Google Gemini**, **ChromaDB**, and **Hugging Face Embeddings**.

The application allows users to upload PDF documents, ask natural language questions, retrieve relevant information using Retrieval-Augmented Generation (RAG), generate document summaries, and export chat conversations.

---

## 🚀 Features

- 📄 Upload PDF documents
- 🤖 Ask questions using Google Gemini AI
- 🔍 Semantic search with ChromaDB
- 🧠 Retrieval-Augmented Generation (RAG)
- 📚 Hugging Face Embeddings
- 📑 AI-generated PDF Summary
- 📊 PDF Statistics
- 💬 Chat Interface
- 📄 View Source References
- 💾 Export Chat as TXT
- 📝 Export Chat as Markdown

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | Web Application |
| LangChain | RAG Pipeline |
| Google Gemini | Large Language Model |
| Hugging Face Embeddings | Text Embeddings |
| ChromaDB | Vector Database |
| PyMuPDF | PDF Text Extraction |

---

## 📂 Project Structure

```text
PDF-RAG-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── assets/
│   ├── logo.png
│   └── styles.css
│
├── downloads/
├── uploads/
├── chroma_db/
│
└── utils/
    ├── embedding.py
    ├── export.py
    ├── gemini.py
    ├── pdf_loader.py
    ├── rag.py
    ├── search.py
    ├── statistics.py
    ├── summary.py
    ├── ui.py
    └── vector_store.py
```

---

## ⚙️ Installation

Clone the repository.

```bash
git clone https://github.com/Saikishorep15/PDF-RAG-AI.git
```

Move into the project folder.

```bash
cd PDF-RAG-AI
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the virtual environment.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install the dependencies.

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📖 How It Works

1. Upload a PDF document.
2. Extract text using PyMuPDF.
3. Split the text into chunks.
4. Generate embeddings using Hugging Face.
5. Store embeddings in ChromaDB.
6. Retrieve the most relevant chunks.
7. Send the context to Google Gemini.
8. Display the generated answer with source references.

---

## 📸 Screenshots

### Home Page

_Add screenshot here_

### Chat Interface

_Add screenshot here_

### PDF Statistics

_Add screenshot here_

---

## 📌 Future Improvements

- Multiple PDF Support
- PDF Export
- Dark Mode
- Chat History
- Keyword Highlighting
- Voice Input
- OCR Support
- User Authentication

---

## 👨‍💻 Author

**SaiKishore P**

GitHub:
https://github.com/Saikishorep15

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub.

---

## 📄 License

This project is licensed under the MIT License.