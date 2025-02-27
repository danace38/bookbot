from stats import get_num_words, count_char, sort_count
import sys

#This function will open the file and read it as string
def get_book_text(filepath):

    with open(filepath) as file:
        file_contents = file.read()
    
    return file_contents


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    char_count_result = count_char(book_text)
    sorted_chars = sort_count(char_count_result)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {book_path} total words")
    print("--------- Character Count -------")

    
    # Print each character and count from the sorted list
    for char_dict in sorted_chars:
        #Get the character (the only key in the dictionary)
        char = list(char_dict.keys())[0]
        # Only print if it's an alphabetical character
        if char.isalpha():
             print(f"{char}: {char_dict[char]}")

    print("============= END ===============")    


main()