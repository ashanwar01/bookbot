from stats import num_chars, num_of_words


def get_text_book(filepath):
    with open(filepath) as f:
        book_content = f.read()

    return book_content


def main():
    book_content = get_text_book("./books/frankenstein.txt")
    num_words = num_of_words(book_content)
    num_of_chars = num_chars(book_content)
    print(f"{num_words} words found in the document")
    print(num_of_chars)


main()
