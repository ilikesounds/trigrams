# -*- encode: utf-8 -*-
import io


def create_raw_string(book):
    """
    Get text from book and transform into raw string
    """
    open_file = io.open(book, mode='r', encoding='utf-8')
    raw_string = open_file.read(13000)
    open_file.close()
    return raw_string[2727:]


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


def create_trigram_list(list_input, n):
    """
    Creates a trigram tuple list based on a list input
    """
    return list(zip(*[list_input[i:] for i in range(n)]))
