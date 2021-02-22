"""
Rosettacode task: Abelian sandpile model

This file creates a .tga image of an Abelian sandpile.
"""
import struct, array
import random

# create a single cell rim around image that will be discarded later
# so the size of image is 129*129
W = 131
H = 131

# this is a dict with a single int as key. value calulated as y<<10|x
A = [0] * W * H

# place a pile of sand particles on a single location
A[66 * W + 66] = 1024 * 4

toppled = False

# keep updating the model until no longer any stack left  with count of 4 or more
while not toppled:
    toppled = True

    # only iterates on the range of values of cells that end up in the final image
    for y in range(1, H - 1):
        for x in range(1, W - 1):
            if A[y * W + x] > 3:
                toppled = False
                A[y * W + x] -= 4

                A[(y+1) * W + x    ] += 1
                A[(y-1) * W + x    ] += 1 
                A[ y    * W + x - 1] += 1
                A[ y    * W + x + 1] += 1

# some colors for the final TGA image    
color = {}
color[0] = struct.pack('<BBB', 0,   0, 0)
color[1] = struct.pack('<BBB', 255, 0, 0)
color[2] = struct.pack('<BBB', 0,   0, 255)
color[3] = struct.pack('<BBB', 0, 255, 0)

img = []
for y in range(1, H - 1):
    for x in range(1, W - 1):
        img.append(color[A[y * W + x]])

with open ('image.tga', 'wb') as f:
    # this is how you create a TGA image
    f.write(struct.pack("<bbbhhbhhhhbb", 0, 0, 2, 0,0,0,  0,0, W-2, H-2, 24, 0))
    f.write(b''.join(img))















