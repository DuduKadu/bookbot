from stats import *

def get_book_text(filepath: str):
    with open(filepath) as book:
        text = book.read()

    words_num = count_words(text)
    char_count = count_letters(text)
    return words_num, char_count

def reporting():
    words, chars = get_book_text("books/frankenstein.txt")

    order_chars = sorting(chars)
    order_chars.sort(reverse=True, key=sort_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    for letter in order_chars:
        char = letter["char"]
        num = letter["num"]

        print(f"{char}: {num}")
    print("============= END ===============")
    return words, chars
                



    


def main():
    reporting()


if __name__ == "__main__":
    main()
