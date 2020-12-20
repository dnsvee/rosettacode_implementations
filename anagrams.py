"""
Rosettacode task Anagrams
"""
from itertools import groupby
words = []
with open('unixdict.txt') as d:
    words = d.readlines()

# strip blanks
words = map    (lambda x: x.strip()              , words)

def sortletters(w):
    return "".join(sorted(w))

grouped = {}
for w in words:
    c = sortletters(w)
    s = grouped.get(c, set())
    s.add(w)
    grouped[c] = s

m = 0
for k,v in grouped.items():
    m = m if len(v) < m else len(v)

for k,v in grouped.items():
    if len(v) == m:
        print(v)
