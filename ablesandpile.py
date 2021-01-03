import struct, array
import random

W = 130
H = 130
I = {}
for h in range(0,H):
    for w in range(0,W):
        I[(h,w)] = 0

I[(64,64)] = 256

toppled = False
while not toppled:
    toppled = True
    for y in range(1,H - 1):
        for x in range(1,W - 1):
            if I[(y,x)] > 4:
                toppled = False
                I[(y,x)] -= 4

                n = y + 1
                s = y - 1
                w = x - 1
                e = x + 1
                I[(n,x)] += 1
                I[(s,x)] += 1 
                I[(y,w)] += 1
                I[(y,e)] += 1

black = (255<<24)|(255<<16)|(255<8)|255
red   = 255<<16
green = 255<<8
blue  = 255
img = []
for y in range(1,H - 1):
    for x in range(1,W - 1):
        val = I[(y,x)]
        if val == 0: img.append(black)
        if val == 1: img.append(red)
        if val == 2: img.append(green)
        if val == 3: img.append(blue)


with open ('image.tga', 'wb') as f:
    f.write(struct.pack("<bbbhhbhhhhbb", 0, 0, 2, 0,0,0,  0,0, W-2, H-2, 32, 0))
    a = array.array("I")
    a.extend(img)
    f.write(bytes(a))















