from stats import count_words, count_letters

def get_book_text(filepath: str):
    with open(filepath) as book:
        text = book.read()

    words_num = count_words(text)
    char_count = count_letters(text)
    result = f"{words_num} words found in the document\n"
    return result, char_count

def main():
    print(get_book_text("books/frankenstein.txt"))


if __name__ == "__main__":
    main()
