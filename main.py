def main():
    book = get_book()
    # print(book)
    word_count, words = get_word_count(book)
    char_count = get_chars(words)
    print(f"{word_count} words found in the book.")
    for char in char_count:
        print(f"The {char} character was found {char_count[char]} times!")


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

main()