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
