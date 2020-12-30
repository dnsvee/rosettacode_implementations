"""
Rosettacode task Anagrams
"""
from itertools import groupby
words = []
with open('dict.txt') as d:
    words = d.readlines()

# strip blanks
words = map(lambda x: x.strip(), words)

# ex. anagram -> aaagnmr
def sortletters(w):
    return "".join(sorted(w))

# groups words in a set where the key is the word sorted by it's letters that's common to each word
grouped = {}
for w in words:
    c = sortletters(w)
    s = grouped.get(c, set())
    s.add(w)
    grouped[c] = s

# find size of largest set
m = 0
for k,v in grouped.items():
    m = m if len(v) < m else len(v)

# list all sets with size equal to largest value
for k,v in grouped.items():
    if len(v) == m:
        print(v)
