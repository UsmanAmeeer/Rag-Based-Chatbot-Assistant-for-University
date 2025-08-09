# AI Chatbot with Flask Backend & React Frontend

This project is a **full-stack AI chatbot** powered by:
- **Flask** + **LangChain** + **FAISS** for backend document retrieval and conversational memory
- **React** + **Vite** + **Tailwind CSS** for the frontend UI

It allows users to query PDF and website data using OpenAI's GPT models, with conversation history maintained per session.

---

## 🚀 Tech Stack
**Backend:**
- Python 3.10+
- Flask
- LangChain
- FAISS (Vector Store)
- OpenAI GPT-4o-mini
- dotenv for environment variables

**Frontend:**
- React (Vite)
- Tailwind CSS
- Axios (API calls to backend)

---

## 📂 Folder Structure
```
project-root/
│
├── backend/               # Flask backend code
│   ├── app.py              # Main backend entry
│   ├── requirements.txt    # Python dependencies
│   ├── faiss_index/        # FAISS vector store (generated)
│   └── data/               # PDFs or source files
│
├── src/                    # React frontend source code
│   ├── components/         # UI components
│   ├── pages/              # React pages
│   ├── App.jsx             # Main React app
│   └── main.jsx
│
├── package.json            # Frontend dependencies
├── tailwind.config.js      # Tailwind configuration
├── vite.config.js          # Vite config
├── .gitignore              # Ignore sensitive files
├── README.md               # This file
└── .env                    # Environment variables (NOT committed)
```

---

## 🔑 Environment Variables
Create a `.env` file in the **backend** folder:
```
OPENAI_API_KEY=your_openai_api_key_here
```

---

## ⚙️ Backend Setup
1. Navigate to backend folder:
   ```bash
   cd backend
   ```
2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask server:
   ```bash
   python app.py
   ```
   Backend will start at `http://localhost:5000`

---

## 💻 Frontend Setup
1. Navigate to project root (where `package.json` is located).
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start development server:
   ```bash
   npm run dev
   ```
   Frontend will run at `http://localhost:5173`

4. Build for production:
   ```bash
   npm run build
   ```

---

## 🛠️ API Endpoint
**POST** `/chat`  
Request:
```json
{
  "session_id": "user123",
  "query": "What is the VC's message?"
}
```
Response:
```json
{
  "answer": "The VC's message is...",
  "sources": ["https://www.iub.edu.pk/vice-chancellor-message", "data.pdf"]
}
```

---



## 📷 Screenshots
<img width="1918" height="871" alt="image" src="https://github.com/user-attachments/assets/f4e7655a-3122-452c-bffe-3e35d2bb20a4" />
