# Rag-Based-Chatbot-Assistant-for-University
 Students struggle to find admission details (deadlines, eligibility) quickly.  So i made a solution,  A chatbot that answers questions 24/7 using official university documents

# PDF + Web RAG Chatbot with Flask, LangChain, and FAISS

This project is a **Retrieval-Augmented Generation (RAG) chatbot** built with Flask, LangChain, OpenAI's GPT models, and FAISS.  
It can answer questions based on **PDF documents** and **web pages** with **chat history** and **conversation memory**.

---

## 🚀 Features

- 📄 Load and process **PDF files**.
- 🌐 Scrape and process **web pages**.
- 🔍 Store embeddings in **FAISS vector database** for fast retrieval.
- 🧠 Maintain **chat history** with `ConversationBufferMemory`.
- 💬 Serve a **REST API** using Flask (`/chat` endpoint).
- ⚡ Uses **OpenAI GPT-4o-mini** for responses.
- 🔁 Automatically rebuilds FAISS index if not found locally.

---

## 📂 Project Structure

```
project/
│-- app.py                # Main Flask app with LangChain integration
│-- .env                   # Store your OpenAI API key
│-- faiss_index/           # FAISS vector store directory (auto-created)
│-- data/
│   └── data.pdf           # PDF file to be processed
```

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/Rag-Based-Chatbot-Assistant-for-University.git
cd rag-chatbot
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create `.env` file**
```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

## ⚙️ Configuration

Update these variables inside `app.py`:

```python
pdf_path = r"D:\path\to\data.pdf"  # Path to your PDF
hardcoded_urls = [
    "https://www.example.com/",
    "https://www.example.com/page"
]
faiss_index_dir = "faiss_index"    # Folder for FAISS storage
```

---

## ▶️ Running the App

```bash
python app.py
```

Server will run at:
```
http://0.0.0.0:5000
```

---

## 📡 API Usage

### **POST** `/chat`

**Request Body:**
```json
{
  "session_id": "user1",
  "query": "What is mentioned in the vice chancellor's message?"
}
```

**Response Example:**
```json
{
  "answer": "The vice chancellor emphasizes academic excellence...",
  "sources": [
    "D:/Projects/data/data.pdf",
    "https://www.iub.edu.pk/vice-chancellor-message"
  ]
}
```

---

## 🛠 Dependencies

Add this to your `requirements.txt`:

```
flask
python-dotenv
langchain
faiss-cpu
openai
```

Install them via:
```bash
pip install -r requirements.txt
```

---

## 🧠 How It Works

1. **Load Data**  
   - PDF loaded via `PyPDFLoader`
   - Web pages loaded via `WebBaseLoader`

2. **Split Text**  
   - Uses `RecursiveCharacterTextSplitter` with `chunk_size=1000` and `chunk_overlap=200`

3. **Create Embeddings**  
   - Generates OpenAI embeddings with `OpenAIEmbeddings`

4. **Vector Store**  
   - Stores chunks in FAISS for fast semantic search
   - Saves to `faiss_index` folder

5. **Query Handling**  
   - On `/chat` request, retrieves relevant chunks
   - Feeds them into `ChatOpenAI` (GPT-4o-mini)
   - Maintains session-based memory

---

## 📌 Notes

- First run will take longer to process PDF and URLs and save FAISS index.
- For production, you can deploy on **Docker**, **Railway**, **Render**, or **AWS**.
- Replace sample URLs and PDF with your own data.

---

## 📜 License

This project is for educational and development purposes.  
Feel free to modify and use in your own projects.
