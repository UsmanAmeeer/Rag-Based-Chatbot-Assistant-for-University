# Rag-Based-Chatbot-Assistant-for-University
 Students struggle to find admission details (deadlines, eligibility) quickly.  So i made a solution,  A chatbot that answers questions 24/7 using official university documents
# PDF + Web RAG Chatbot with Flask, LangChain, FAISS, and React Frontend

This project is a **Retrieval-Augmented Generation (RAG) chatbot** powered by **Flask**, **LangChain**, **OpenAI GPT models**, and **FAISS**.  
It processes data from **PDF documents** and **web pages** to answer user queries with **context awareness** and **chat history**.  
A **React-based frontend** is provided for an interactive user experience.

---

## 🚀 Features

- 📄 Load and process **PDF files**.
- 🌐 Scrape and process **web pages**.
- 🔍 Store embeddings in **FAISS vector database** for fast retrieval.
- 🧠 Maintain **chat history** with `ConversationBufferMemory`.
- 💬 Serve a **REST API** using Flask (`/chat` endpoint).
- ⚡ Uses **OpenAI GPT-4o-mini** for responses.
- 🖥 Interactive **React frontend** with real-time chat.
- 🔁 Automatically rebuilds FAISS index if not found locally.

---

## 📂 Project Structure

```
project/
│-- backend/
│   │-- app.py               # Main Flask app with LangChain integration
│   │-- .env                  # Store your OpenAI API key
│   │-- faiss_index/          # FAISS vector store directory (auto-created)
│   │-- data/
│   │   └── data.pdf          # PDF file to be processed
│
│-- frontend/
│   │-- package.json          # React dependencies
│   │-- src/                  # React components and pages
│   │-- public/               # Static files
```

---

## 📦 Backend Installation (Flask API)

1. **Navigate to backend folder**
```bash
cd backend
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

5. **Run Flask API**
```bash
python app.py
```
Backend will be available at:
```
http://localhost:5000
```

---

## 💻 Frontend Installation (React UI)

1. **Navigate to frontend folder**
```bash
cd frontend
```

2. **Install dependencies**
```bash
npm install
```

3. **Start development server**
```bash
npm run dev
```
Frontend will be available at:
```
http://localhost:3000
```

4. **Build for production**
```bash
npm run build
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

## 🛠 Backend Dependencies

Add this to your `requirements.txt`:

```
flask
python-dotenv
langchain
faiss-cpu
openai
```

---

## 🧠 How It Works

1. **Data Loading**  
   - PDFs via `PyPDFLoader`
   - Web pages via `WebBaseLoader`

2. **Text Splitting**  
   - `RecursiveCharacterTextSplitter` (`chunk_size=1000`, `chunk_overlap=200`)

3. **Embeddings & Storage**  
   - `OpenAIEmbeddings` for vectorization
   - FAISS for fast retrieval

4. **Query Handling**  
   - Retrieve relevant chunks
   - Generate answers using `ChatOpenAI`
   - Maintain chat history with `ConversationBufferMemory`

5. **Frontend Communication**  
   - React frontend sends queries to Flask API
   - Displays responses and sources in real-time

---

## 📌 Notes

- First run will build FAISS index; subsequent runs will load it.
- Replace example URLs and PDF with your own data.
- For production, consider deploying Flask API and React frontend separately.

---

## 📜 License

This project is for educational and development purposes.  
Feel free to modify and use in your own projects.
