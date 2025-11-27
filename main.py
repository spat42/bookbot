import sys

from stats import character_count, sorted_list, word_count


def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()

    return book_text


def main():
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book = get_book_text(filepath)
    num_words = word_count(book)
    num_characters = character_count(book)
    sorted_characters = sorted_list(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for chararacter in sorted_characters:
        if chararacter["char"].isalpha():
            print(f"{chararacter['char']}: {chararacter['num']}")
    print("============= END ===============")


main()
