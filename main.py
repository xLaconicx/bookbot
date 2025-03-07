import sys

from stats import number_of_words, character_count

def get_book_text(path_to_file):
    with open(path_to_file, 'r') as file:
        book_text = file.read()
        return book_text
    
def main():

    #Step 1: Check to see if sys.arv has two arguments
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)

    # Step 2: Get the text of the book
    book_text = get_book_text(sys.argv[1])
    
    # Step 2: Calculate the total word count and display it
    num = number_of_words(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    
    # Step 3: Calculate character counts and filter alphabetic characters
    char_counts = character_count(book_text)
    characters_list = [
        {"char": char, "num": count} for char, count in char_counts.items() if char.isalpha()
    ]
    
    # Step 4: Sort characters by frequency (descending order)
    characters_list.sort(key=lambda char_info: char_info["num"], reverse=True)
    
    # Step 5: Display sorted character counts
    print("--------- Character Count -------")
    for char_info in characters_list:
        print(f"{char_info['char']}: {char_info['num']}")
    
    # Final decorative line, as requested by assignment
    print("============= END ===============")

# Call the main function to execute the script
main()
