# -*- encode: utf-8 -*-
# import io

# book = io.open('./data/Uncle_Sams.txt', mode='r', encoding='utf-8')
# book_text = book.read(12950)
# book.close()
# usable_text = book_text[2950:]
usable_text = '"We must break this up," whispered Private Hyman to Noll Terry, Hal Overton\'s soldier chum. "I don\'t want to see him get hurt."'
usable_text.replace(',', '')
print(type(usable_text))
print(usable_text)
