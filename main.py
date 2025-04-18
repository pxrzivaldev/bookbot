from stats import word_count

def main():
    booktext = get_book_text("books/frankenstein.txt")
    num_words = word_count(booktext)
    print(f"{num_words} words found in the document")
    

def get_book_text(path):
    booktext = ""
    with open(path, 'r') as file:
        booktext = file.read()
    return booktext

    
if __name__ == "__main__":
    main()
