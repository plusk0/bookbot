from stats import output
import sys
import time

def main(path):
    try:
        filepath = path[1]
        start = time.time()
        #path = "books/frankenstein.txt"
        print(output(filepath))
        end = time.time()
        print(end - start)
        return 0
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
    exit(1)
main(sys.argv)