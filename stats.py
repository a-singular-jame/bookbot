
def get_book_text(path):
    with open(path) as f:
        return f.read()

def num_words(i):
    text = get_book_text(i)
    no_words = text.split()
    print(len(no_words), "words found in the document")

def num_letters(n):
    text = get_book_text(n)
    text = text.lower()
    letters_dict = {}
    for letter in text:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1

    for  letter, number in letters_dict.items():
        print(f"'{letter}': {number}")