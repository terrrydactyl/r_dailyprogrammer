#!/usr/bin/env python

# [2014-12-1] Challenge #191 [Easy] Word Counting

import string
import sys


from collections import Counter
def strip_beg_end_nonalpha(word):
    while word and (not word[0].isalpha() or not word[-1].isalpha()):
        if not word[0].isalpha():
            word = word[1:]
        elif not word[-1].isalpha():
            word = word[:-1]
    return word
        
def book_word_count(book_url):
    with open(book_url) as f:
        data = f.read()
    punctuation = set(string.punctuation)
    data = data.split()
    words = []
    for word in data:
        if word not in punctuation:
            word = strip_beg_end_nonalpha(word)
            if word:
                words.append(word.lower())
    count = Counter(words)
    return count


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print book_word_count(sys.argv[1])
