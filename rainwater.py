"""
Solves rainwater trapping problem.
"""
import collections

class St:
    l = 0 # min height left
    r = 0 # min height right
    h = 0 # height of loc.
    def __init__(self, h):
        self.h = h

    def __repr__(self):
        return "%d %d %d" % (self.l, self.h, self.r)

# example
R = [St(0), St(3), St(0), St(2), St(0), St(4), St(0)]

# max height to the left
i = 1
m = 0
while i < len(R)-2:
    R[i].l = m
    if R[i].h > m:
        m = R[i].h
    i += 1


# max height to the right
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


