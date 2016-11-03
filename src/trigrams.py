# -*- encode: utf-8 -*-

"""
This Trigram module will parse a text file to create trigrams and build a
new text file based on those trigrams.
"""

import io
import sys
import random


def create_raw_string(book, char_to_read=13000, char_offset=2801):
    """
    Get text from book and transform into raw string
    """
    open_file = io.open(book, mode='r', encoding='utf-8')
    raw_string = open_file.read(char_to_read)
    open_file.close()
    return raw_string[char_offset:]


def format_string_for_list(text):
    """
    Remove the punctuation and new lines from the text provided
    """
    punctuation = u',.?!"-'
    replacement_punctuation = u'      '
    new_text = text.translate(
        text.maketrans(punctuation, replacement_punctuation)
        )
    return new_text.replace('\n', ' ').split()


def create_trigram_dict(list_input):
    """
    Creates a trigram dictionary based on a list input
    """
    temp_dict = {}
    temp = list(zip(*[list_input[i:] for i in range(3)]))
    for index_0, index_1, index_2 in temp:
        if temp_dict.get((index_0, index_1)):
            temp_dict[(index_0, index_1)].append(index_2)
        else:
            temp_dict[(index_0, index_1)] = [index_2]
    return temp_dict


def create_text(trigram_dict, words):
    """
    Creates a new text output based on the trigram list input
    """

    keys = list(trigram_dict.keys())
    random_key = random.choice(keys)
    text = ' '.join(random_key)

    while len(text.split()) < words:
        last_1, last_2 = text.split()[-2:]

        if not trigram_dict.get(last_1, last_2):
            last_1, last_2 = random.choice(keys)

        text += ' ' + random.choice(trigram_dict[(last_1, last_2)])
    return text


def main(source_file, word_count):
    raw_string = create_raw_string(source_file)
    parsed_string = format_string_for_list(raw_string)
    trigram_dict = create_trigram_dict(parsed_string)
    text = create_text(trigram_dict, word_count)
    return text

if __name__ == '__main__':
    text = main(sys.argv[1], int(sys.argv[2]))
    print(text)
