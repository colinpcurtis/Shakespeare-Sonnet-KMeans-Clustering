import pandas as pd
from poetry_analysis import poems
from create_word_dict import remove_punctuation

data = pd.read_csv("word_dictionary.csv", header=None)


def get_word_index(dataframe):  # creates dictionary where value of the word is ranking of how often it occurs
    dictionary = {}
    for n in range(dataframe.shape[0]):
        word = dataframe.iloc[n][0]
        dictionary[word] = n  # save 0, 1, 2 for special values
    return dictionary


_word_index = get_word_index(data)


word_index = {k: (v + 3) for k, v in _word_index.items()}  # creates space for the three special characters in our dict
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2  # unknown
word_index["<UNUSED>"] = 3


def remove_punctuation_for_poems():  # removes any special characters from the poems.  We just want the words
    new_poems = []
    for poem in poems:
        poem = remove_punctuation(poem)
        new_poems.append(poem)
    return new_poems


clean_poems = remove_punctuation_for_poems()


def create_embedding(array, maxlen):  # makes list of length maxlen  + 1, so 121 input neurons for maxlen = 120
    new_array = []
    for lst in array:
        new_lst = [word_index["<START>"]]
        for word in lst:
            if word not in word_index.keys():
                new_lst.append(word_index["<UNK>"])
                if len(new_lst) - 1 == len(lst):
                    # subtract -1 since we have the <start> index.
                    # this "if" statement allows us to make sure that if the last word in the poem is unknown, then
                    # we can still pad to correct length
                    while len(new_lst) <= maxlen:
                        new_lst.append(word_index["<PAD>"])
                    break
            else:
                new_lst.append(word_index[word])
                if len(new_lst) - 1 == maxlen:
                    break
                elif len(new_lst) - 1 == len(lst):
                    # subtract -1 since we have the <start> index
                    while len(new_lst) <= maxlen:
                        new_lst.append(word_index["<PAD>"])
                    break
        new_array.append(new_lst)
    return new_array


list_of_poems = create_embedding(clean_poems, 120)  # embeds each poem as a list of length 120 of integers
