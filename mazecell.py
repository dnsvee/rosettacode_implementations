import struct, random

W = 256
H = 256

randint = random.randint

class Maze:
    def __init__(self, b, d):
        self.a  = [0] * W * H
        self.a0 = [0] * W * H
        self.b = b
        self.d = d

        for y in range(0, H):
            for x in range(0, W):
                self.a[y * W + x] = 0
                if y >= H//2 -  8 and y < H//2 +  8 and x >= W//2 -  8 and x < W//2 +  8:
                    self.a[y * W + x] = 0 if randint(0,4) == 0 else 1

    def clear(self):
        return
        for y in range(0, H):
            for x in range(0, W):
                self.a0[y * W + x] = 0

    def swap(self):
        self.a, self.a0 = self.a0, self.a

    def get(self, y, x):
        return self.a[y * W + x]

    def neighbs(self, y, x):
        c = self.get
        return c(y-1, x-1) + c(y-1, x) + c(y-1, x+1) + c(y, x-1) + c(y, x+1) + c(y+1, x-1) + c(y+1, x) + c(y+1, x+1) 

    def gen(self):
        self.clear()
        for y in range(1, H-1):
            for x in range(1, W-1):
                c = self.neighbs(y, x)
                if self.b[c] == '1':
                    self.a0[y * W + x] = 1
                elif self.d[c] == '1':
                    self.a0[y * W + x] = self.a[y * W + x]
                else:
                    self.a0[y * W + x] = 0
        self.swap()

pack = struct.pack

red  = pack('<BBB', 0, 0, 255)
black= pack('<BBB', 0, 0, 0)
with open('maze.tga', 'wb') as f:
    M = Maze("000111010", "000000111")
    for n in range(0,256):
        print(n)
        M.gen()

    f.write(pack('<BBBHHBHHHHBB', 0, 0, 2, 0,0,0, 0,0, W,H, 24, 0))
    for i in range(0, H):
        for j in range(0, W):
            if M.a[i * W + j] == 1:
                f.write(red)
            else:
                f.write(black)





