from stats import *

import sys

def get_book_text(filepath: str):
    with open(filepath) as book:
        text = book.read()

    words_num = count_words(text)
    char_count = count_letters(text)
    return words_num, char_count

def reporting(argument: str):
    words, chars = get_book_text(argument)

    order_chars = sorting(chars)
    order_chars.sort(reverse=True, key=sort_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {argument}")
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
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    reporting(sys.argv[1])


if __name__ == "__main__":
    main()
