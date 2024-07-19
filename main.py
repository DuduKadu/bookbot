def word_count(f):
    words = f.split()
    print(len(words))

def main():
    file_contents = ''

    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    
    word_count(file_contents)

main() 