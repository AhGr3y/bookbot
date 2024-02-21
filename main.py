def main():
    path_to_book = "books/frankenstein.txt"
    text = get_book_text(path_to_book)
    word_count = get_word_count(text)
    char_dict = get_char_dict(text)
    sorted_list = convert_dict_to_sorted_list(char_dict)

    print(f"--- Begin report of {path_to_book} ---")
    print(f"{word_count} words found in the document")
    print("")
    for dict in sorted_list:
        name = dict["char"]
        num = dict["num"]
        if not name.isalpha():
            continue
        print(f"The '{name}' character was found {num} times")
    print("--- End report ---")

def convert_dict_to_sorted_list(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char": char, "num": dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["num"]

def get_char_dict(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_word_count(text):
    words_from_text = text.split()
    return len(words_from_text)

def get_book_text(path):
    with open(path) as f:
        return f.read()   

main()