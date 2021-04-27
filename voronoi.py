import struct
import array

W = 512
H = 512

G = [0] * W * H

def gt(y, x):
    return G[y * W + x]

def cg(y, x, v):
    G[y * W + x] = v

import random

def randi(upto):
    return random.randrange(0, upto)

pts = {}
def acolor(r, g, b):
    return struct.pack('<BBB', r, g, b)

clr = []
for i in range(0, 12):
    clr.append(acolor(randi(255), randi(255),  randi(255)))
while len(clr):
    y, x = randi(H), randi(W)
    if pts.get((y, x)) is None:
        pts[(y, x)] = clr.pop()

print(pts)

with open('voronoi.tga', 'wb+') as v:
    v.write(struct.pack('<BBBHHBHHHHBB', 0, 0, 2,  0, 0, 0,  0, 0, W, H, 24, 0))
    for y in range(0, H):
        for x in range(0, W):
            p0 = None
            di = None
            for p in pts.keys():
                y0, x0 = p
                s0 = pow(x - x0, 2) + pow(y - y0, 2)
                s0 = abs(x - x0) + abs(y - y0)
                if di is None or s0 < di:
                    di = s0
                    p0 = p
            v.write(pts[p0])

            






