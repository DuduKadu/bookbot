def count_words(text: str):
    words = text.split()
    alpha = len(words)

    return alpha

def count_letters(text: str):
    lower = text.lower()
    let = {}

    for letter in lower:
        if letter.isalpha() and not letter in let:
            let[letter] = 1
        elif letter in let:
            let[letter] += 1
    return let

    