def number_of_words(book_text):
    return len(book_text.split())

def character_count(book_text):
    char_counts = {}
    for char in book_text:
        lowercase_char = char.lower()

        if lowercase_char in char_counts:
            char_counts[lowercase_char] += 1
        else:
            char_counts[lowercase_char] = 1
    return char_counts
