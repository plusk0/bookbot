import time


def sort_on(dict):
    return dict[1]

def get_num_words(filepath):

    with open(filepath) as f:
        contents = f.read()
        word_list = contents.split()
        return len(word_list)
    
def get_num_char(filepath):
    letter_list = []
    seen_list = []
    with open(filepath) as f:
        word_list = f.read()
    for char in word_list:
        if char.isalpha():
            char = char.lower()
            if char in seen_list:

                for letter in letter_list:
                    if letter[0]== char:
                        index = letter_list.index(letter)
                        letter_list[index] = tuple(list((letter[0],letter[1]+1)))
            else:
                letter_list.append((char, 1))
                seen_list.append(char)

    sorted_list = sorted(letter_list, reverse= True, key=lambda func : func[1])
    return sorted_list


def format(sorted_list):
    string = ""
    for entry in sorted_list:
        
        string = str(string + str(entry[0])+ ": " + str(entry[1]) + "\n")
    return string



def output(filepath):
    num_words = get_num_words(filepath)
    output_list = (format(get_num_char(filepath)))

    print(f"============ BOOKBOT ============ \n")
    print(f"Analyzing book found at {filepath}...\n")
    print(f"----------- Word Count ---------- \n")
    print(f"Found {num_words} total words \n")
    print(f"--------- Character Count -------\n")                            
    print(f"{output_list}============= END ===============") # newline before END is part of output_list function
    return
