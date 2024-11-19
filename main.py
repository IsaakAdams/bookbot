def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    num_words = count_words(text)
    # print(f"{num_words} words found in the document")
    chars_dict = get_chars_dict(text)
    # print(chars_dict)

    print_report(book_path, count_words(text), get_chars_dict(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    
    return chars

def print_report(book_path, word_count, char_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    
    for c in char_dict:
        print(f"The '{c}' character was found {char_dict[c]} times")
    
    print("--- End report ---")

main()
