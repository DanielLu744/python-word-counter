from utils import clean_text, count_words, plot_word_freq

def main():
    choice = input("Enter 1 to read from a file, or 2 to input text manually: ")

    if choice == "1":
        filename = input("Enter the filename (e.g., sample_text.txt): ")
        try:
            with open(filename, "r", encoding="utf-8") as file:
                text = file.read()
        except FileNotFoundError:
            print("File not found. Please check the path.")
            return
    else:
        text = input("Please enter your text: ")

    cleaned = clean_text(text)
    word_count = count_words(cleaned)

    print("\n--- Top 10 Word Frequencies ---")
    for word, freq in list(word_count.items())[:10]:
        print(f"{word}: {freq}")

    save = input("\nWould you like to save the results to a file? (y/n): ")
    if save.lower() == 'y':
        with open("word_count_result.txt", "w", encoding="utf-8") as f:
            for word, freq in word_count.items():
                f.write(f"{word}: {freq}\n")
        print("Results saved to word_count_result.txt")

    plot = input("Would you like to generate a bar chart? (y/n): ")
    if plot.lower() == 'y':
        plot_word_freq(word_count)

if __name__ == "__main__":
    main()