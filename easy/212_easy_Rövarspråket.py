# coding=utf-8
import sys
import string


vowels = 'aeiouyåäöAEIOUYÅÄÖ'.decode('utf-8')
while True:
    word = raw_input("Please type in a word: ")
    if word == '--quit':
        sys.exit()
    word = word.decode('utf-8')
    modified_word = []
    for c in word:
        if c not in vowels and c not in string.punctuation and c != ' ':
            modified_word.append(c + 'o' + c.lower())
        else:
            modified_word.append(c)
    modified_word = ''.join(modified_word)
    print modified_word
