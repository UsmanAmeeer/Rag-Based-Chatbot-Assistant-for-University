import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from langchain.document_loaders import PyPDFLoader, WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.memory import ConversationBufferMemory
# Removed LangServe as it is not available
import faiss

# Load .env
load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("Missing OPENAI_API_KEY in environment. Please set it in your .env file.")

# Configuration
pdf_path = r"D:\Usman Ameer\Projects\Langchain\Ibrahim FYP\data\data.pdf"
hardcoded_urls = [
    "https://www.iub.edu.pk/",
    "https://www.iub.edu.pk/vice-chancellor-message",
]
faiss_index_dir = "faiss_index"

# Embeddings & splitter
embeddings = OpenAIEmbeddings()
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# Build or load FAISS vector store
def load_vector_store():
    if os.path.exists(faiss_index_dir):
        return FAISS.load_local(faiss_index_dir, embeddings)
    docs = []
    docs.extend(splitter.split_documents(PyPDFLoader(pdf_path).load()))
    docs.extend(splitter.split_documents(WebBaseLoader(hardcoded_urls).load()))
    vs = FAISS.from_documents(docs, embeddings)
    vs.save_local(faiss_index_dir)
    return vs

vector_store = load_vector_store()

# App and LangServe
app = Flask(__name__)
# Directly use Flask app without LangServe
serve = app

# In-memory session store for memory
session_memories = {}

# Create QA chain per session with memory
def get_chain(session_id: str):
    memory = session_memories.get(session_id)
    if not memory:
        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        session_memories[session_id] = memory
    return RetrievalQAWithSourcesChain.from_chain_type(
        llm=ChatOpenAI(model_name="gpt-4o-mini", temperature=0),
        chain_type="stuff",
        retriever=vector_store.as_retriever(search_kwargs={"k": 4}),
        memory=memory,
        return_source_documents=True
    )

# Chat endpoint with history and memory
def chat_logic(data):
    session_id = data.get("session_id", "default")
    query = data.get("query", "")
    chain = get_chain(session_id)
    # run chain: returns dict with 'answer' and 'source_documents'
    result = chain({"question": query})
    # format sources
    sources = [doc.metadata.get("source") for doc in result.get("source_documents", [])]
    return {"answer": result.get("answer"), "sources": sources}

@serve.route("/chat", methods=["POST"])
def chat_endpoint(req):
    data = req.json or {}
    response = chat_logic(data)
    return jsonify(response)

    # Use Flask's run method to start the server
    app.run(host="0.0.0.0", port=5000)
    serve.serve()
