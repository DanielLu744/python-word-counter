def count_words(text):
    word_count = {}
    words = text.lower().split()

    for word in words:
        word = word.strip(".,!?;:'\"()[]{}")  # 去除标点
        if word:
            word_count[word] = word_count.get(word, 0) + 1

    return word_count

def main():
    text = input("Please enter some text:\n")
    result = count_words(text)

    print("\n--- Word Frequencies ---")
    for word, count in sorted(result.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()