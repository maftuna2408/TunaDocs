# source/app.py

import streamlit as st
from parser import extract_text_from_pdf
from summarizer import summarize_text
from visualizer import plot_word_frequency
import tempfile

st.set_page_config(page_title="TunaDocs", layout="wide")

st.title("📚 TunaDocs - Academic PDF Summarizer")

# Fayl yuklash
uploaded_file = st.file_uploader("📤 Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Faylni vaqtincha saqlab olish
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        pdf_path = tmp_file.name

    # 1. PDFdan matn olish
    st.subheader("📄 Extracted Text")
    full_text = extract_text_from_pdf(pdf_path)
    st.text_area("Full text from PDF", full_text, height=250)

    # 2. Qisqacha mazmun
    if st.button("🧠 Summarize"):
        with st.spinner("Summarizing..."):
            summary = summarize_text(full_text)
            st.subheader("✍️ Summary")
            st.write(summary)

    # 3. So‘zlar statistikasi
    if st.button("📊 Show Word Frequency"):
        st.subheader("📈 Most Frequent Words")
        plot_word_frequency(full_text)
