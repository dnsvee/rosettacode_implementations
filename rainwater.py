"""
Solves rainwater trapping problem:
"""

class St:
    l = 0
    r = 0
    h = 0
    def __init__(self, h):
        self.h = h

    def __repr__(self):
        return "%d %d %d" % (self.l, self.h, self.r)

R = [St(0), St(3), St(0), St(2), St(0), St(4), St(0)]

i = 1
m = 0

def fixit(over, l):
    m = 0
    for o in over:
        l(o, m)

while i < len(R)-2:
    R[i].l = m
    if R[i].h > m:
        m = R[i].h
    i += 1

i = len(R)-2
m = 0
while i > 0:
    R[i].r = m
    if R[i].h > m:
        m = R[i].h
    i -= 1

# make a nice ASCII graph
for h in range(5, -1, -1):
    for i in range(0, len(R)):
        if R[i].h >= h:
            print('#', end='')
            continue
        mi = min(R[i].l, R[i].r)
        if R[i].h < h <= mi:
            print('~', end='')
            continue
        print(' ', end='')
    print()


