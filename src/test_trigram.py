# -*- coding: utf-8 -*-

import pytest
from trigrams import(
    create_raw_string,
    format_string_for_list,
    create_trigram_dict
    )

'''
Test file for trigrams assignment
'''

TEXT = '''The young recruit's mistake lay in pretending to know a lot more than
he really did know. He had been put through the unmerciful hazing that
always awaits a very "fresh" rookie, or recruit, but even that had
taught him little. Private Green was always looking for the chance to
prove to his new comrades among the regulars of the Thirty-fourth that
he knew something after all. This afternoon his trouble had taken the
form of trying to find something in a two-days' old newspaper on which
he could discourse for the enlightenment of the other men.
'''

PUNCTUATION = [
    ',',
    '.',
    '?',
    '!',
    '"',
    '-',
    '\n'
]


def test_create_rawstring():
    '''
    Test create_raw_string
    '''
    assert TEXT in create_raw_string('./data/Uncle_Sams.txt')


@pytest.mark.parametrize('punc', PUNCTUATION)
def test_format_string_for_list_punctuation(punc):
    '''
    Test format_string_for_list to ensure all punctuation and newlines are
    removed.
    '''
    assert punc not in format_string_for_list(TEXT)


def test_create_trigram_dict():
    '''
    Tests create_trigram_dict creates a dictionay with the expected shape.
    '''
    word = ['I', 'wish', 'I', 'may', 'I', 'wish', 'I', 'might']
    trigram_dict = {
        ('I', 'wish'): ['I', 'I'],
        ('wish', 'I'): ['may', 'might'],
        ('may', 'I'): ['wish'],
        ('I', 'may'): ['I']
    }
    assert create_trigram_dict(word) == trigram_dict
