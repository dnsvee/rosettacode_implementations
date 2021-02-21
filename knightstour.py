"""
Solves the knights tour problem on a DxD board
"""

## board is a dict with key y_pos*x+x_pos
board = {}
D = 5

for y in range(0, D):
    for x in range(0, D):
        board[y * 16 + x] = 0

def isposs(y, x):
    # gets all possible knights locations not visited
    r = board.get(y * 16 + x, None)
    return r == 0

kmoves = [(2, -1), (2, 1), (1, -2), (1, 2), (-2, -1), (-2, 1), (-1, -2) ,(-1, 2)]

def countposs(y, x):
    c = 0
    for a, b in kmoves:
        if isposs(y + a, x + b): c += 1
    return c

def printboard():
    for y in range(0,D):
        for x in range(0,D):
            print('%4s' % str(board[y * 16 + x]), end='')
        print()
    print()

kmoves = [(2, -1), (2, 1), (1, -2), (1, 2), (-2, -1), (-2, 1), (-1, -2) ,(-1, 2)]

def tour(y, x, c):
    board[y * 16 + x] = c
    if c >= D*D:
        printboard()

    poss = []
    for i, j in kmoves:
        if isposs(y + i, x + j):
            ct = countposs(y + i, x + j)
            if ct > 0:
                poss.append((y + i, x + j, ct))

    poss = sorted(poss, key=lambda x : -x[2])

    while len(poss) > 0:
        y0, x0, ct = poss.pop()
        tour(y0, x0, c + 1)
             
    board[y * 16 + x] = 0

import random
x = random.randrange(0,D)
y = random.randrange(0,D)

tour(y, x, 1)


