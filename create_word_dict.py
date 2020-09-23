import string
import operator
import csv
from reading_poem_txt_files import poems


def flatten(array):
    return [item for sublist in array for item in sublist]


words = flatten(poems)


def remove_punctuation(array):
    word_lst = []
    punct = set(string.punctuation)
    for word in array:
        word = word.lower()  # make lowercase
        word_lst.append(''.join(x for x in word if x not in punct))  # removes special punctuation characters
    return word_lst


words = remove_punctuation(words)


def create_dict(array):  # associates to each word the number of times it's used throughout the poems
    dictionary = {}
    for word in set(array):
        dictionary[word] = array.count(word)
    return dictionary


word_count = create_dict(words)
sorted_dict = dict(sorted(word_count.items(), key=operator.itemgetter(1), reverse=True))
# we want low numbers in our dictionary to be words that are used often, and high numbers to be rarely used words

w = csv.writer(open("word_dictionary.csv", "w"))
for key, value in sorted_dict.items():
    w.writerow([key, value])
