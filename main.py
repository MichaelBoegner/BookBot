def main():
    book = get_book()
    word_count = get_word_count(book)
    print(f"{word_count} words found in the book.")

def get_book():
    with open("./books/frankenstein.txt") as f:
        return f.read()

def get_word_count(book):
    words = book.split()
    return len(words)
    

main()