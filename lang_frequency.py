import argparse

def load_data(filepath):
    our_text = open(filepath,encoding='cp1251')
    return our_text

words = {} #Dictionary for the word count {'word':number}

def get_most_frequent_words(text):
    """
    Split each line into words, modify and
    add to dictionary as a key and count of reps as a value.
    """
    for line in text.readlines():
        #remove 'bad' chars in each line
        for char in ['*','-','–','"']:
            line = line.replace(char,'')

        #add word to dictionary
        for word in line.strip().lower().split():
            words[word] = words.get(word,0) + 1
    text.close()

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='''Show frequent words.''')
    parser.add_argument('text_file', type=str, help='filepath')

    user_input = parser.parse_args()
    get_most_frequent_words(load_data(user_input.text_file))
    print(sorted(words.items(), key=lambda a : a[1],reverse=True)[:10])

