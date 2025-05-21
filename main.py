from stats import get_num_words
from stats import get_num_char

def main():
    path = "books/frankenstein.txt"
    num_words = get_num_words(path)
    print(f"{num_words} words found in the document")
    get_num_char(path)
main()