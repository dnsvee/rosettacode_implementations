"""
anagram rosettacode
"""
from itertools import groupby
words = []
with open('dict.txt') as d:
    words = d.readlines()
words = map    (lambda x: x.strip()              , words)
words = map    (lambda x: ("".join(sorted(x)), x), words)
words = sorted (words,    key=lambda x: x[0])
words = groupby(words,    key=lambda x : x[0])
words = map    (lambda x: (x[0], list(x[1])), words)
words = map    (lambda x: (x[0], list(map(lambda y: y[1], x[1]))), words)
words = sorted (words,    key=lambda x: len(x[1]))
words = list(words)
maxlen= len(words[-1][1])
words = filter(lambda x: len(x[1]) == maxlen, words)
print(list(map(lambda x: x[1], words)))
