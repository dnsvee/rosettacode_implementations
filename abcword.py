"""
Show every abc word"
"""

def readdict():
    with open('unixdict.txt', 'r') as f:
        return f.read().split('\n')

for w in readdict():
    try:
        a = w.index('a')
        b = w.index('b')
        c = w.index('c')
        if c > b > a:
            print(w)
    except:
        pass
