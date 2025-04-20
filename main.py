from stats import *

def main():
    bookpath = "books/frankenstein.txt"
    booktext = get_book_text(bookpath)
    num_words = word_count(booktext)
    charcount = characters_count(booktext)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for chardic in sort(charcount):
        for d in chardic:
            print(f"{d}: {chardic[d]}")
    print("============= END ===============")

def get_book_text(path):
    booktext = ""
    with open(path, 'r') as file:
        booktext = file.read()
    return booktext

    
if __name__ == "__main__":
    main()
