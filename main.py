import sys

from stats import num_chars, num_of_words, sort_list


def get_text_book(filepath):
    with open(filepath) as f:
        book_content = f.read()

    return book_content


def main():
    file_path = sys.argv[1]

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_content = get_text_book(file_path)
    num_words = num_of_words(book_content)
    num_of_chars = num_chars(book_content)
    sorted_list = sort_list(num_of_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for dicts in sorted_list:
        letter = dicts["char"]
        count = dicts["num"]
        print(f"{letter}: {count}")

    print("============= END ===============")


main()
