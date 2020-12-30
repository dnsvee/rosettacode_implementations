"""
ABC Words
"""

def readdict():
    with open('dict.txt', 'r') as f:
        return f.read().split('\n')

i = 1
for w in readdict():
    try:
        a = w.index('a')
        b = w.index('b')
        c = w.index('c')
        if c > b > a:
            print(i, w)
            i += 1
    except:
        pass
