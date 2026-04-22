# ai-resume-analyzer

# 📄 AI Resume Analyzer (Offline)

A simple and efficient AI-powered Resume Analyzer built using Python, Streamlit, and Ollama.

This tool allows users to upload their resume (PDF) and receive structured feedback including a score, strengths, weaknesses, and improvement suggestions — all running locally without any external API.

---

## 🚀 Features

* 📂 Upload PDF Resume
* 🤖 AI-based analysis using Ollama (Local LLM)
* 📊 Resume scoring (out of 10)
* ✅ Strengths identification
* ⚠️ Weakness detection
* 🚀 Actionable improvement suggestions
* 🔒 Fully offline (no API cost)

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Ollama (LLaMA / Phi models)
* PyPDF2

---

## ⚙️ How It Works

1. User uploads a resume (PDF)
2. Text is extracted from the file
3. Resume is sent to a local LLM via Ollama
4. AI analyzes and returns structured feedback
5. Results are displayed in a clean UI

---

## 📦 Installation

```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Make sure Ollama is running:

```bash
ollama serve
```

---

## 📌 Future Improvements

* Job-role based analysis
* Resume rewriting feature
* ATS keyword scoring system
* Export report as PDF

---

## 💡 Inspiration

Built to explore local AI applications and create a practical tool for students and job seekers.

---

## 👨‍💻 Author

Parth Hiwarkar
