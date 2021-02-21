""" 
Implements  a couple of maze generation algorythms with ascii display
"""

import random
rint = random.randrange

class Maze:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.a = [0] * w * h

    def get(self, y, x):
        if not(0 <= y < self.h) or not(0 <= x < self.w): return -1
        return self.a[y * self.w + x]


    # start (0,0)


    def eller(self, W, H):
        M = [0] * W * H
        S = [i for i in range(0, W * H)]

def printmaze(M, W, H):
    syms = {10: '─', 5 : '│', 0b11 : '└', 6 : '┌', 12 : '┐', 9 : '┘', 7 : '├', 13 : '┤', 11 : '┴', 14 : '┬', 15 : '┼', 1 : '╵', 2 : '╶', 4 : '╷', 8 : '╴' }
    for y in range(0, H):
        for x in range(0, W):
            c = M[y * W + x]
            print(syms.get(c, '?'), end='')

        print()


def recdiv(M, W, H, W0, W1, H0, H1):
    Hx = H1 - H0
    Wx = W1 - W0

    if Hx < 2 or Wx < 2: return

    if Wx >= Hx:
        a = rint(W0 + 1, W1)
        b = rint(H0, H1)

        for y in range(H0, H1):
            if y != b:
                M[y * W + a - 1] &= 0b1101
                M[y * W + a    ] &= 0b0111

        recdiv(M, W, H, W0, a, H0, H1)
        recdiv(M, W, H, a, W1, H0, H1)
    else:
        a = rint(H0 + 1, H1)
        b = rint(W0, W1)

        for x in range(W0, W1):
            if x != b:
                M[(a - 1) * W + x] &= 0b1011
                M[ a      * W + x] &= 0b1110

        recdiv(M, W, H, W0, W1, H0, a)
        recdiv(M, W, H, W0, W1, a, H1)

def divmethod(W, H):
    syms = {10: '─', 5 : '│', 3 : '└', 6 : '┌', 12 : '┐', 9 : '┘', 7 : '├', 13 : '┤', 11 : '┴', 14 : '┬', 15 : '┼', 1 : '╵', 2 : '╶', 4 : '╷', 8 : '╴' }

    M = [0b1111] * W * H

    for y in range(0, H):
        M[y * W]         = 7
        M[y * W + W - 1] = 13

    for x in range(0, W):
        M[0            + x] = 14
        M[(H - 1 ) * W + x] = 11

    M[0]           = 6
    M[W-1]         = 12
    M[(W-1)*W]     = 3
    M[(W-1)*W+W-1] = 9

    recdiv(M, W, H, 0, W, 0, H)

    for y in range(0, H):
        for x in range(0, W):
            print(syms[M[y * W + x]], end='')
        print()

    return M

def kruskal(W, H):
    """
    Uses a randomized version of Kruskal to gen a maze
    """
    M = [0] * W * H
    E = []

    for y in range(0, H):
        for x in range(0, W):
            if y + 1 < H:
                E.append((y * W + x, (y + 1) * W + x, 4, 1))
            if x + 1 < W:
                E.append((y * W + x, y * W + x + 1, 2, 8))
    random.shuffle(E)

    S = [i for i in range(0, W * H)]

    def root(a):
        while S[a] != a:
            S[a] = S[S[a]]
            a = S[a]
        return a

    for e in E:
        a, b, e0, e1 = e
        a0 = root(a)
        b0 = root(b)
        if a0 != b0:
            S[b0] = a0
            M[a] = M[a] | e0
            M[b] = M[b] | e1

    return M

def recback(W, H):
    """
    Uses the recusrive backtracking method. Starts at 0, 0
    """

    M = [0] * W * H

    def get(y, x):
        if not(0 <= y < H) or not(0 <= x < W): return -1
        return M[y * W + x]

    cur = 0 # (0, 0)

    cells = []
    while True:
        y, x = divmod(cur, W)

        l = []

        if get(y + 1, x) == 0: l.append((y + 1, x, 4, 1))
        if get(y - 1, x) == 0: l.append((y - 1, x, 1, 4))
        if get(y, x + 1) == 0: l.append((y, x + 1, 2, 8))
        if get(y, x - 1) == 0: l.append((y, x - 1, 8, 2))

        if len(l) > 0:
            y0, x0, d0, d1 = random.choice(l)
            c = y0 * W + x0
            M[c  ] = M[c]   | d1
            M[cur] = M[cur] | d0
            cells.append(cur)
            cur = c
            continue

        if len(cells) == 0:
            break

        cur = cells.pop()

    return M


print('Recursive backtracking ...')
mz = recback(32, 32)
printmaze(mz, 32, 32)
print()

print('Kruskal ...')
mz = kruskal(32, 32)
printmaze(mz, 32, 32)
print()

divmethod(32,32)

