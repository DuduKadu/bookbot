from stats import count_words

def get_book_text(filepath: str):
    with open(filepath) as book:
        text = book.read()

    words_num = count_words(text)
    result = f"{words_num} words found in the document"
    return result

def main():
    print(get_book_text("books/frankenstein.txt"))


if __name__ == "__main__":
    main()
