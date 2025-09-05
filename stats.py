def num_of_words(book_content):
    num_words = len(book_content.split())
    return num_words


def num_chars(book_content):
    words_in_book = book_content.split()
    chars_dict = {}

    for word in words_in_book:
        chars_in_word = word.lower()
        for char in chars_in_word:
            if char not in chars_dict:
                chars_dict[char] = 1
            else:
                chars_dict[char] += 1

    return chars_dict


def sort_list(chars_dict):
    list_dict = []
    for char in chars_dict:
        split_dict = {}
        split_dict["char"] = char
        split_dict["num"] = chars_dict[char]
        list_dict.append(split_dict)

    def sort_on(items):
        return items["num"]

    list_dict.sort(reverse=True, key=sort_on)

    return list_dict
