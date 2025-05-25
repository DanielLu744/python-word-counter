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

# 🔽 This test code runs only when you execute utils.py directly
if __name__ == "__main__":
    print("🔧 Running test for utils.py...")

    test_text = "Python is easy. Python is powerful, and easy to learn."
    cleaned = clean_text(test_text)
    print("Cleaned text:", cleaned)

    word_count = count_words(cleaned)
    print("Word count:", word_count)

    print("Displaying bar chart...")
    plot_word_freq(word_count)