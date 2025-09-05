def get_text_book(filepath):
    with open(filepath) as f:
        book_content = f.read()

    return book_content


def main():
    print(get_text_book("./books/frankenstein.txt"))


main()
