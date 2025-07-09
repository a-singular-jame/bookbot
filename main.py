import sys
from stats import num_letters, num_words, filters

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

else:
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")

    num_words(sys.argv[1])

    print("--------- Character Count -------")

    num_letters(sys.argv[1])
    filters()

    print("============= END ===============")