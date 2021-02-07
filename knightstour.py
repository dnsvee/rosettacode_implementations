"""
Tries solving the knights tour problem
"""

## board is a dict with key y_pos*x+x_pos
board = {}

for y in range(0, 8):
    for x in range(0, 8):
        board[y * 16 + x] = 0

def isposs(y, x):
    # gets all possible knights locations not visited
    r = board.get(y * 16 + x, None)
    return r == 0

def countposs(y, x):
    c = 0
    if isposs(y + 2, x - 1):
        c += 1
    if isposs(y + 2, x + 1):
        c += 1
    if isposs(y + 1, x - 2):
        c += 1
    if isposs(y + 1, x + 2):
        c += 1
    if isposs(y - 2, x - 1):
        c += 1
    if isposs(y - 2, x + 1):
        c += 1
    if isposs(y - 1, x - 2):
        c += 1
    if isposs(y - 1, x + 2):
        c += 1
    return c

def printboard():
    for y in range(0,8):
        for x in range(0,8):
            print('%4s' % str(board[y * 16 + x]), end='')
        print()
    print()

kmoves = [(2, -1), (2, 1), (1, -2), (1, 2), (-2, -1), (-2, 1), (-1, -2) ,(-1, 2)]

def tour(y, x, c):
    print(y, x, c)
    board[y * 16 + x] = c
    if c == 16:
        exit()
        printboard()

    poss = []
    for i, j in kmoves:
        if isposs(y + i, x + j):
            ct = countposs(y + i, x + j)
            poss.append((y + i, x + j, ct))

    poss = sorted(poss, key=lambda x : x[2])
    while len(poss) != 0:
        a = poss.pop()
        print('a=', a)
        tour(a[0], a[1], c + 1)
             
    board[y * 16 + x] = 0

tour(0, 0, 1)


