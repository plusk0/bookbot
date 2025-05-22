from stats import output
import time

def main():
    start = time.time()
    path = "books/frankenstein.txt"
    print(output(path))
    end = time.time()
    print(end - start)
    return 0
main()