import argparse

def load_data(filepath):
    our_text = open(filepath)
    return our_text

words = {} #Dictionary for the word count {'word':number}

def get_most_frequent_words(text):
    """
    Split each line into words, modify and
    add to dictionary as a key and count of reps as a value.
    """
    for i in text.readlines():
        i = i.strip().lower()

        for char in ['*','-','–','"']:
            i = i.replace(char,'')

        for a in i.split():
            words[a] = words.get(a,0) + 1
    text.close()


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='''Show frequent words.''')
    parser.add_argument('text_file', type=str, help='filepath')

    user_input = parser.parse_args()
    get_most_frequent_words(load_data(user_input.text_file))
    print(sorted(words.items(), key=lambda a : a[1],reverse=True)[:10])

