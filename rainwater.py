"""
Solves rainwater trapping problem. 
"""

import collections

class Col:
    l = 0 # max height left
    r = 0 # max height right
    h = 0 # height 

    def __init__(self, h):
        self.h = h

    def __repr__(self):
        return "%d %d %d" % (self.l, self.h, self.r)

# an example. include two stacks of 0 height to the left and right to make computations easier
R = [Col(i) for i in [0, 3, 0, 2, 0, 4, 3, 5, 1, 6, 0]]

# max height to the left
m = 0 # maximum so far
for i in range(1, len(R) - 2):
    R[i].l = m
    # if stack is higher than max then new max is height of stack
    if R[i].h > m:
        m = R[i].h

# max height to the right
i = len(R)-2
m = 0
for i in range(len(R) - 2, 0, -1):
    R[i].r = m
    if R[i].h > m:
        m = R[i].h

# make a nice ASCII graph
for h in range(12, -1, -1):
    for i in range(1, len(R) - 1):
        if R[i].h >= h:
            print('#', end='')
            continue
        mi = min(R[i].l, R[i].r)
        if R[i].h < h <= mi:
            print('~', end='')
            continue
        print(' ', end='')
    print()


