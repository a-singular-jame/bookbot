
def get_book_text(path):
    with open(path) as f:
        return f.read()

def main(i):
    print(get_book_text(i))

def num_words(i):
    text = get_book_text(i)
    no_words = text.split()

    print(len(no_words), "words found in the document")

num_words("books/frankenstein.txt")