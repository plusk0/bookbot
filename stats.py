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
            if char in seen_list:

                for tuple in letter_list:

                    for value in tuple:
                        if value == char:
                            print(tuple)
                            tuple = 1 # change old tuple to new tuple (tuple with ex. e : 1 -> e : 2)


            else:
                letter_list.append({char.lower(), 1})
                seen_list.append(char)
                print(letter_list)
                time.sleep(0.2)



    sorted_list = []
    sorted_list = letter_list
    sorted_list.sort(reversed=True)
    print(letter_list)
    print(sorted_list)



def output(filepath):
    num_words = get_num_words(filepath)
    char_count = get_num_char(filepath)
    print(f"\
    ============ BOOKBOT ============" \
    "Analyzing book found at {filepath}..." \
    "----------- Word Count ----------" \
    "Found {num_words} total words" \
    "--------- Character Count -------" \
    "{char_count}" \
    "============= END ==============="
)