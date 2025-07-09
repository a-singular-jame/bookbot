from stats import num_letters, num_words, filters



print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")

num_words("books/frankenstein.txt")

print("--------- Character Count -------")

num_letters("books/frankenstein.txt")
filters()

print("============= END ===============")