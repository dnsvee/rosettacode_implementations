"""
Rosettacode task: Abelian sandpile model

This file creates a .tga image of an Abelian sandpile.
"""
import struct, array
import random

# create a single cell rim around image that will be discarded later
# so the size of image is 128*128
W = 130
H = 130

# this is a dict with a single int as key. value calulated as y<<10|x
I = {}
for h in range(0,H):
    for w in range(0,W):
        I[h<<10|w] = 0

    # place a pile of sand particles on a single location
def pile(x, y, h):
    I[y<<10|x] = h
pile(64,64,16*16*16)


toppled = False
n = s = w = e = 0

# keep updating the model until no longer any stack with count of 4 or more
while not toppled:
    toppled = True
    # only iterates of the range of values of cells that end up in the final image
    for y in range(1,H - 1):
        for x in range(1,W - 1):
            if I[y<<10|x] > 3:
                toppled = False
                I[y<<10|x] -= 4

                I[(y+1)<<10|x] += 1
                I[(y-1)<<10|x] += 1 
                I[y<<10|(x-1)] += 1
                I[y<<10|(x+1)] += 1

# pack data for final write to TGA image
color = {}
color[0] = struct.pack('<BBB', 0,   0, 0)
color[1] = struct.pack('<BBB', 255, 0, 0)
color[2] = struct.pack('<BBB', 0,   0, 255)
color[3] = struct.pack('<BBB', 0, 255, 0)

img = []
for y in range(1,H - 1):
    for x in range(1,W - 1):
        img.append(color[I[y<<10|x]])

with open ('image.tga', 'wb') as f:
    # this is how you create a TGA image
    f.write(struct.pack("<bbbhhbhhhhbb", 0, 0, 2, 0,0,0,  0,0, W-2, H-2, 24, 0))
    f.write(b''.join(img))















