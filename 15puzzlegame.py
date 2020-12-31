"""
15 Puzzle Game

"""
import sys, random
exit = sys.exit
randrange = random.randrange

B = {}
cnt = 1
for y in range(1,5):
    for x in range(1,5):
        B[(y,x)] = cnt
        cnt += 1
B[(4,4)] = 0

x0 = 4
y0 = 4

def printboard(B):
    for y in range(1,5):
        for x in range(1,5):
            print('{:4}'.format(B[(y,x)]), end='')
        print('\n')

# checks if board in solved state; returns bool
def issolved(B):
    for y in range(0,15):
        y0, x0 = divmod(y, 4)
        if B[(y0+1,x0+1)] != y+1:
            return False
    return True

# shuffle board in steps unique steps
def shuffle(B, steps, x0, y0):
    range14 = range(1,5)
    fun = lambda : randrange(-1,2)
    while steps > 0:
        y1, x1 = y0+fun(), x0+fun()
        if not x1 in range14: continue
        if not y1 in range14: continue
        if (y1!=y0) and (x1!=x0): continue # only move horiz. or vert.

        B[(y1,x1)], B[(y0,x0)] = B[(y0,x0)], B[(y1,x1)]

        steps = steps - 1

        x0, y0 = x1, y1

    return x0, y0

print("move the zero by passing 'w' 'e' 's' or 'n' or a combination of them as movement commands eg. wesn")
x0, y0 = shuffle(B, 4, x0, y0)
while True:
    printboard(B)
    if issolved(B): 
        print('solved')
        sys.exit(0)

    i = input("> ")

    if len(i) == 0:
        print('bye')
        exit(0)

    x1 = 0
    y1 = 0
    for c in i:
        x1 = x0
        y1 = y0
        if c == 'w' and x0 > 1: x1 = x0 - 1
        if c == 'e' and x0 < 4: x1 = x0 + 1
        if c == 'n' and y0 > 1: y1 = y0 - 1
        if c == 's' and y0 < 4: y1 = y0 + 1

        B[(y1,x1)], B[(y0,x0)] = B[(y0,x0)], B[(y1,x1)]

        x0, y0 = x1, y1

    print(B)


