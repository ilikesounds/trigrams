# -*- coding: utf-8 -*-

from trigrams import create_raw_string

'''
Test file for trigrams assignment
'''

TEXT = """The young recruit's mistake lay in pretending to know a lot more than
he really did know. He had been put through the unmerciful hazing that
always awaits a very "fresh" rookie, or recruit, but even that had
taught him little. Private Green was always looking for the chance to
prove to his new comrades among the regulars of the Thirty-fourth that
he knew something after all. This afternoon his trouble had taken the
form of trying to find something in a two-days' old newspaper on which
he could discourse for the enlightenment of the other men.
"""


def test_create_rawstring():
    '''
    Test create_raw_string
    '''
    assert TEXT in create_raw_string('./data/Uncle_Sams.txt')
