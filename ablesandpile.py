import struct, array
import random

W = 130
H = 130
I = {}
for h in range(0,H):
    for w in range(0,W):
        I[h<<10|w] = 0

I[64<<10|64] = 3*5*7*13*17


toppled = False
n = s = w = e = 0
while not toppled:
    toppled = True
    for y in range(1,H - 1):
        for x in range(1,W - 1):
            if I[y<<10|x] > 3:
                toppled = False
                I[y<<10|x] -= 4

                I[(y+1)<<10|x] += 1
                I[(y-1)<<10|x] += 1 
                I[y<<10|(x-1)] += 1
                I[y<<10|(x+1)] += 1

black = [0,0,0]
red   = [255,0,0]
green = [0,255,0]
blue  = [0,0,255]
img = []
for y in range(1,H - 1):
    for x in range(1,W - 1):
        val = I[y<<10|x]
        if val == 0: img.extend(black)
        if val == 1: img.extend(red)
        if val == 2: img.extend(green)
        if val == 3: img.extend(blue)


with open ('image.tga', 'wb') as f:
    f.write(struct.pack("<bbbhhbhhhhbb", 0, 0, 2, 0,0,0,  0,0, W-2, H-2, 24, 0))
    while len(img):
        app = struct.pack("<BBB", img.pop(), img.pop(), img.pop())
        f.write(app)















