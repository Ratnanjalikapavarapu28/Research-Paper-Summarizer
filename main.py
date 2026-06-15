import streamlit as st
def load_css():
    with open("assets/style.css", "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()
from routes.upload import save_uploaded_files
from routes.summary import generate_summary_for_documents
from routes.chat import ask_question

from services.pdf_service import extract_text
from services.chunk_service import create_chunks
from services.embedding_service import load_embedding_model
from services.rag_service import store_chunks


st.set_page_config(
    page_title="Research Paper Summarizer",
    layout="wide"
)

st.markdown(
    '<div class="main-title">📄 Research Paper Summarizer</div>',
    unsafe_allow_html=True
)

uploaded_files = st.file_uploader(
    "Upload Research Papers",
    type=["pdf"],
    accept_multiple_files=True
)


# ---------------- SESSION STATE ----------------

if "documents" not in st.session_state:
    st.session_state.documents = []

if "chunks" not in st.session_state:
    st.session_state.chunks = []

if "vector_db" not in st.session_state:
    st.session_state.vector_db = None

if "embeddings" not in st.session_state:
    st.session_state.embeddings = None


# ---------------- FILE PROCESSING ----------------

if uploaded_files:

    st.info("Processing uploaded files...")

    saved_files = save_uploaded_files(uploaded_files)

    st.write("Files Uploaded:", len(saved_files))

    all_documents = []
    combined_text = ""

    for file_path in saved_files:

        text = extract_text(file_path)

        all_documents.append(
            {
                "name": file_path,
                "text": text
            }
        )

        combined_text += text + "\n"

    st.session_state.documents = all_documents

    st.subheader("Extracted Text Preview")

    st.write(combined_text[:1000])

    # ---------------- CHUNKING ----------------

    chunks = create_chunks(combined_text)

    st.session_state.chunks = chunks

    st.subheader("Chunk Information")

    st.write("Total Chunks:", len(chunks))

    if chunks:
        st.write(chunks[0])

    # ---------------- EMBEDDINGS ----------------

    embeddings = load_embedding_model()

    st.session_state.embeddings = embeddings

    vector_db = store_chunks(
        chunks,
        embeddings
    )

    st.session_state.vector_db = vector_db

    st.success("All PDFs processed successfully 🚀")


# ---------------- SUMMARY ----------------

if st.button("Generate Summary"):

    if not st.session_state.documents:

        st.error("Please upload PDF files first")

    else:

        st.info("Generating summary...")

        try:

            summary = generate_summary_for_documents(
                st.session_state.documents
            )

            st.subheader("Research Paper Summary")

            st.write(summary)

        except Exception as e:

            st.error(f"Summary Error: {str(e)}")


# ---------------- CHAT ----------------

st.subheader("Ask Questions from Your Research Papers")

question = st.text_input(
    "Enter your question"
)

if st.button("Ask"):

    if not st.session_state.vector_db:

        st.error("Please upload PDF files first")

    else:

        try:

            answer = ask_question(
                question,
                st.session_state.vector_db
            )

            st.subheader("Answer")

            st.write(answer)

        except Exception as e:

            st.error(f"Chat Error: {str(e)}")