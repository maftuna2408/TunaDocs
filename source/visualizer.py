# source/visualizer.py
import matplotlib.pyplot as plt
from collections import Counter
import re

def plot_word_frequency(text: str, top_n: int = 10):
    # Faqat so‘zlarni ajratib olish (punctuation’lardan tozalash)
    words = re.findall(r'\b\w+\b', text.lower())
    
    # So‘zlar sonini sanash
    word_counts = Counter(words).most_common(top_n)
    
    # So‘z va ularning chastotasi
    labels, values = zip(*word_counts)

    # Grafik chizish
    plt.figure(figsize=(10, 5))
    plt.bar(labels, values, color='skyblue')
    plt.title(f"Top {top_n} most frequent words")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
