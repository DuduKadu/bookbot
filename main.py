def word_count(f):
    words = f.split()
    return len(words)

def character_count(c):
    text = c.lower()
    characters = {}
    
    for char in text:
        if char in characters and char.isalpha():
            characters[char] += 1
        elif char not in characters and char.isalpha():
            characters[char] = 1
    return characters
 
def get_text(path):
    with open(path) as f:
        return f.read()

def get_dict_list(dict):
    char_list = []

    for key in dict:
        key_dict = {}
        
        key_dict['character'] = key
        key_dict["count"] = dict[key]

        char_list.append(key_dict)
    return char_list

def sort_by(d):
    return d["count"]

def report_log(amount, ls):
    print('--- Begin Report of books/frankenstein ---')
    print(f'{amount} words found in the document')
    print()

    for i in ls:
        character = ''
        count = 0
        for char in i:
            convert = str(i[char])
            if convert.isalpha():
                character = i[char]
            elif convert.isdigit():
                count = i[char]
        print(f'The {character} character was found {count} times')
    
    print('--- End Report ---')


def main():
    file_path = 'books/frankenstein.txt'

    file_contents = get_text(file_path)
    
    total_words = word_count(file_contents)

    char_dict = character_count(file_contents)

    char_ls = get_dict_list(char_dict)

    char_ls.sort(reverse=True, key=sort_by)
    
    report_log(total_words, char_ls)

main() 