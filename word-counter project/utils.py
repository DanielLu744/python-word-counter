import string
from collections import Counter
import matplotlib.pyplot as plt

def clean_text(text):
    text = text.lower()
    for char in string.punctuation:
        text = text.replace(char, "")
    return text

def count_words(text):
    words = text.split()
    return dict(Counter(words).most_common())

def plot_word_freq(word_count, top_n=10):
    top_items = list(word_count.items())[:top_n]
    words = [item[0] for item in top_items]
    freqs = [item[1] for item in top_items]

    plt.figure(figsize=(10, 5))
    plt.bar(words, freqs)
    plt.title(f"Top {top_n} Words by Frequency")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
