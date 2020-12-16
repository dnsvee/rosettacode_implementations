import json
"""
Implementation of abbreviations rosettacode task.
"""

def readwholefile(name):
    with open(name, 'r') as f:
        return f.readlines()


if __name__ == '__main__':
    lines = []
    print(readwholefile('days.txt'))
    with open('days.txt', 'r') as f:
        lines = f.readlines()

    lines = list(map(lambda l: l.split(' '), lines))

    for l in lines:
        m = max(map(lambda x: len(x), l))
        for r in range(1,m):
            s=set(map(lambda x: x[0:r], l))
            if len(s) == 7:
                print(r,s)
                break
