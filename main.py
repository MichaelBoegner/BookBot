def main():
    book = get_book()
    # print(book)
    word_count, words = get_word_count(book)
    char_count = get_chars(words)
    print(f"{word_count} words found in the book.")
    char_list = get_char_count_to_list(char_count)
    for tuple in char_list: 
        print(f"The character {tuple[0]} occurs {tuple[1]} times.")
        

def get_book():
    with open("./books/frankenstein.txt") as f:
        return f.read()

def get_word_count(book):
    words = book.split()
    return len(words), words
    
def get_chars(words):
    chars = "".join(words).lower()
    char_count = {}
    for char in chars:
        if char in char_count.keys():
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def get_char_count_to_list(char_count):
    char_list = []
    for char in char_count:
        char_list.append((char, char_count[char]))
    return sorted(char_list)

main()