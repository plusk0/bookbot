import time

def get_num_words(contents):

        word_list = contents.split()
        return len(word_list)
    
def get_sorted_list(contents):

    letter_table = {}
    for char in contents:
        if char.isalpha():
            char = char.lower()
            if char in letter_table:
                letter_table[char] += 1
            else:
                letter_table[char] = 1

    sorted_list = []
    for entry in letter_table:
        sorted_list.append({"char": entry, "number":letter_table[entry]})
    sorted_list.sort(reverse=True, key=lambda a: a["number"])
    #print(sorted_list)
    return sorted_list


def format(sorted_list):
    string = ""
    for entry in sorted_list:
        string = string + str(entry["char"]) + ": " + str(entry["number"]) + "\n"
    return string



def output(filepath):
    print(filepath)
    with open(filepath) as f:           # with statement for file opening helps with correctly closing the file -> resource management
         contents = f.read()

    num_words = get_num_words(contents)
    output_list = (format(get_sorted_list(contents)))

    print(f"============ BOOKBOT ============ \n")
    print(f"Analyzing book found at {filepath}...\n")
    print(f"----------- Word Count ---------- \n")
    print(f"Found {num_words} total words \n")
    print(f"--------- Character Count -------\n")                            
    print(f"{output_list}============= END ===============")         # newline before END is part of output_list function
    return
