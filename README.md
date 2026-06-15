# 📄 Research Paper Summarizer

An AI-powered **Retrieval-Augmented Generation (RAG)** application built using **Streamlit**, **LangChain**, **ChromaDB**, **Hugging Face Embeddings**, and **Ollama**.

The application enables users to upload one or multiple research papers in PDF format, generate concise summaries, and ask context-aware questions based on the uploaded documents.

---

# ✨ Features

* 📂 Upload one or multiple PDF research papers
* 📑 Automatic text extraction from PDF documents
* ✂️ Intelligent text chunking using LangChain
* 🧠 Semantic embeddings with Hugging Face
* 🗄️ Vector storage using ChromaDB
* 📚 AI-powered research paper summarization
* 💬 Context-aware Question Answering (RAG)
* ⚡ Fast local inference using Ollama (Llama 3.2)
* 🎨 Clean and user-friendly Streamlit interface

---

# 🛠️ Tech Stack

* 🐍 Python
* 🎈 Streamlit
* 🔗 LangChain
* 🗄️ ChromaDB
* 🤗 Hugging Face Embeddings
* 🦙 Ollama
* 🧠 Llama 3.2
* 📄 PyPDF2

---

# 📁 Project Structure

```text
app/
│
├── assets/
├── database/
├── routes/
├── services/
├── uploads/
├── utils/
├── main.py
├── requirements.txt
└── README.md
```

---

# 🔄 Workflow

1. 📤 Upload one or more PDF documents.
2. 📖 Extract text from the uploaded PDFs.
3. ✂️ Split the text into manageable chunks.
4. 🤗 Generate embeddings using Hugging Face.
5. 🗄️ Store embeddings in ChromaDB.
6. 📝 Generate concise summaries.
7. 💬 Ask questions about the uploaded documents.
8. 🎯 Retrieve relevant document chunks and generate accurate answers using Ollama.

---

# ⚙️ Installation

### 📥 Clone the Repository

```bash
git clone https://github.com/Ratnanjalikapavarapu28/Research-Paper-Summarizer.git
```

### 📂 Navigate to the Project

```bash
cd Research-Paper-Summarizer
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

### 🚀 Start the Ollama Server

```bash
ollama serve
```

### 📥 Download the Llama 3.2 Model (First Time Only)

```bash
ollama pull llama3.2:3b
```

### 🎈 Launch the Streamlit Application

```bash
streamlit run main.py
```

---

# 📋 Requirements

* 🐍 Python 3.10+
* 🦙 Ollama
* 🧠 Llama 3.2 (3B Model)

---

# 🚀 Future Enhancements

* 💬 Chat history support
* 🧠 Conversation memory
* 📚 Source citation support
* 📤 Export summaries as PDF
* 🌍 Multi-language support
* ☁️ Cloud deployment

---

# 📜 License

This project is intended for **educational and learning purposes**.

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!
