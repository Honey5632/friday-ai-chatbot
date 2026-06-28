# 🤖 FRIDAY — AI Operating System

> A fully functional Iron Man inspired AI assistant powered by **Google Gemini**, **Flask** & **Python** with a custom sci-fi interface.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flask-3.x-black?style=for-the-badge&logo=flask&logoColor=white"/>
  <img src="https://img.shields.io/badge/Google_Gemini-API-4285F4?style=for-the-badge&logo=google&logoColor=white"/>
  <img src="https://img.shields.io/badge/HTML%2FCSS%2FJS-Pure-00f0ff?style=for-the-badge"/>
</p>

---

## 📌 Overview

FRIDAY is a locally-hosted AI chatbot with a full sci-fi HUD interface. It's not just a chat window — it supports **multimodal file uploads**, **real-time markdown rendering**, **syntax-highlighted code blocks**, and maintains **full conversation memory** across the session.

Built entirely from scratch — no UI frameworks, no shortcuts.

---

## ✨ Features

| Feature | Description |
|---|---|
| 💬 **AI Chat** | Powered by Google Gemini with full conversation history |
| 📎 **File Upload** | Send PDFs, images, CSVs directly into the AI for analysis |
| 🖼️ **Image Analysis** | Upload any image — FRIDAY analyzes it intelligently |
| 💻 **Code Generation** | Generates syntax-highlighted code with Prism.js |
| 📝 **Markdown Rendering** | Full markdown parsed in real-time via Marked.js |
| 🔒 **Secure Handling** | Uploaded files wiped from local storage immediately after processing |
| 🎨 **Sci-fi UI** | Custom black + cyan HUD design with animated loading states |

---

## 🛠️ Tech Stack

```
Backend    →  Python 3.10 · Flask · Google Gemini API (google-genai)
Frontend   →  Pure HTML · CSS · Vanilla JavaScript
Libraries  →  Marked.js (markdown) · Prism.js (syntax highlighting)
Fonts      →  Orbitron · Share Tech Mono · Inter (Google Fonts)
```

---

## ⚙️ How It Works

```
User types message / uploads file
         │
         ▼
Flask receives POST request (/ask_friday)
         │
         ▼
File saved temporarily to local buffer
         │
         ▼
File uploaded to Gemini Files API (cloud sandbox)
         │
         ▼
Local file wiped immediately 🗑️
         │
         ▼
Gemini processes text + file as multimodal input
         │
         ▼
Response returned → Marked.js parses markdown
         │
         ▼
Prism.js highlights code blocks → rendered in chat
```

---

## 📁 Project Structure

```
friday-ai-chatbot/
│
├── main.py                  # Flask backend — routes, Gemini API, file handling
├── api_file                 # Your Google Gemini API key (NOT pushed to GitHub)
│
├── templates/
│   └── index.html           # Full sci-fi frontend UI
│
├── temp_flask_uploads/      # Temporary file buffer (auto-created, auto-wiped)
│
└── README.md
```

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/Honey5632/friday-ai-chatbot.git
cd friday-ai-chatbot
```

**2. Install dependencies**
```bash
pip install flask google-genai
```

**3. Add your Gemini API key**

Create a file named `api_file` in the project root and paste your API key inside:
```
YOUR_GEMINI_API_KEY_HERE
```
Get your free API key at: [aistudio.google.com](https://aistudio.google.com)

**4. Run the server**
```bash
python main.py
```

**5. Open in browser**
```
http://127.0.0.1:5000
```

---

## 💬 What You Can Ask FRIDAY

```
"Analyze this image"              → Upload any image for detailed analysis
"Create a game in Python"         → Generates full working game code
"Explain this CSV data"           → Upload a CSV for instant analysis
"Review my code"                  → Paste or upload code for feedback
"Write a function that does X"    → Full code with syntax highlighting
```

---

## 🔒 Security Notes

- The `api_file` containing your API key is **never pushed to GitHub**
- Add it to `.gitignore` immediately:
```bash
echo "api_file" >> .gitignore
echo "temp_flask_uploads/" >> .gitignore
```
- Uploaded files are deleted from local storage the moment they are transferred to Gemini's cloud sandbox

---

## 🎨 UI Highlights

- **Font:** Orbitron (HUD headers) + Share Tech Mono (system text)
- **Color:** Absolute black `#000000` + Cyan `#00f0ff`
- **Loading state:** Animated radar spinner + scanning pulse bar
- **Chat layout:** Right-aligned user bubbles · Left-aligned FRIDAY responses
- **Code blocks:** Prism.js Tomorrow Night theme

---

## 🔧 Possible Improvements

- [ ] Deploy to cloud (Render / Railway / Heroku)
- [ ] Add voice input with Web Speech API
- [ ] Stream responses token by token (like ChatGPT)
- [ ] Add conversation export / save history
- [ ] Add multiple personality modes

---

## 🙋 Author

**Honey Rana**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/honey-rana-6748b938a)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Honey5632)

---

## ⚠️ Disclaimer

This project is for educational purposes. FRIDAY is inspired by the Marvel Cinematic Universe — all Iron Man references are purely for creative theming.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
