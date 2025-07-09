letters_dict = {}
sorted_totals = []

# opens and returns whole text file
# for other functions to use
def get_book_text(path):
    with open(path) as f:
        return f.read()

# finds and prints the number of words in given file
def num_words(i):
    text = get_book_text(i)
    no_words = text.split()
    print(f"Found {len(no_words)} total words")

# calculates and prints total of each 
# character in given file
def num_letters(n):
    text = get_book_text(n)
    text = text.lower()

    for letter in text:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1

# sorts and filters characters in 
# correct order and only alphabetical
def filters():
    for  letter, number in letters_dict.items():
        sorted_totals.append ({"char" : letter, "num" : number})
        sorted_totals.sort(reverse = True, key = sort_on)
    
    for i in range(len(sorted_totals)):
        temp = sorted_totals[i]["char"]
        if temp.isalpha() == True:
            print(f"{sorted_totals[i]["char"]}: {sorted_totals[i]["num"]}")

# apparently this is needed to sort properly
def sort_on(items):
    return items["num"]


