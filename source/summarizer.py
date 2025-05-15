# source/summarizer.py
from transformers import pipeline

# HuggingFace summarization modeli (masalan, "t5-small" yoki "facebook/bart-large-cnn")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str, max_length: int = 130, min_length: int = 30) -> str:
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]["summary_text"]
