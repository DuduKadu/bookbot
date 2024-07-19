def word_count(f):
    words = f.split()
    return len(words)

def character_count(c):
    text = c.lower()
    characters = {}
    
    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters
 
def get_text(path):
    with open(path) as f:
        return f.read()
        


def main():
    file_path = 'books/frankenstein.txt'

    file_contents = get_text(file_path)
    
    amount = word_count(file_contents)

    char_amout = character_count(file_contents)

main() 