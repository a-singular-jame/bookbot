letters_dict = {}
sorted_totals = []

def get_book_text(path):
    with open(path) as f:
        return f.read()

def num_words(i):
    text = get_book_text(i)
    no_words = text.split()
    print(f"Found {len(no_words)} total words")

def num_letters(n):
    text = get_book_text(n)
    text = text.lower()

    for letter in text:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1

def filters():
    for  letter, number in letters_dict.items():
        sorted_totals.append ({"char" : letter, "num" : number})
        sorted_totals.sort(reverse = True, key = sort_on)
    
    for i in range(len(sorted_totals)):
        temp = sorted_totals[i]["char"]
        if temp.isalpha() == True:
            print(f"{sorted_totals[i]["char"]}: {sorted_totals[i]["num"]}")

def sort_on(items):
    return items["num"]


