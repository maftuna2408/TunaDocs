from parser import extract_text_from_pdf
from summarizer import summarize_text
from visualizer import plot_word_frequency

# Path to your PDF file
pdf_path = "sample.pdf"  # change this to your actual file

# Extract text
full_text = extract_text_from_pdf(pdf_path)

# Summarize
summary = summarize_text(full_text)
print("\n--- Summary ---\n", summary)

# Visualize
plot_word_frequency(full_text)
