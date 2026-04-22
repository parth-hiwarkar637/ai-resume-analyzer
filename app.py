import streamlit as st 
import ollama
import PyPDF2


MODEL = "llama3"



def read_pdf(upload_file):
    text = ""
    reader = PyPDF2.PdfReader(upload_file)
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content
    return text



def chat_bot(resume_text):
    system_prompt = f"""
You are a professional resume reviewer.

Analyze the resume and provide:
- Score out of 10
- Strengths
- Weaknesses
- Improvements

Be specific, avoid generic advice, and focus on job readiness.

Resume:
{resume_text}

Format:

Score: <number>/10

Strengths:
- ...

Weaknesses:
- ...

Improvements:
- ...
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "user", "content": system_prompt}
        ]
    )

    return response['message']['content']



upload_file = st.file_uploader("Upload your PDF", type=["pdf"])

if upload_file is not None:
    if st.button("Analyze"):
        with st.spinner("Analyzing..."):
            resume_text = read_pdf(upload_file)
            response = chat_bot(resume_text)

        st.write(response)