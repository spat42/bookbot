from audioop import reverse


def word_count(book):
    all_words = book.split()
    return len(all_words)


def character_count(book):
    book = book.lower()
    all_chars = {}
    for char in book:
        if char in all_chars:
            all_chars[char] += 1
        else:
            all_chars[char] = 1

    return all_chars


def sort_on(items):
    return items["num"]


def sorted_list(char_dict):
    char_list = []
    for char in char_dict:
        new_dict = {}
        new_dict["char"] = char
        new_dict["num"] = char_dict[char]
        char_list.append(new_dict)

    char_list.sort(reverse=True, key=sort_on)
    return char_list
