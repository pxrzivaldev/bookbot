def get_book_text(path):
    booktext = ""
    with open(path, 'r') as file:
        booktext = file.read()
    return booktext

def main():
    booktext = get_book_text("books/frankenstein.txt")
    print(booktext)
    
if __name__ == "__main__":
    main()
