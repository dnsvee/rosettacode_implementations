import random
import struct

def put(c):
    print(c, end='')

class Map:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.a = [0 for h0 in range(0,h) for w0 in range(0,w)]
        self.a[256*512+256] = 1

    def populate(self, am):
        pot = [-self.w, +self.w, -1, +1]
        sz = 0
        while sz < 256:
            if sz == 256: break
            a, b = random.randrange(0,self.w), random.randrange(0, self.h)
            if (128 < a < 512-128) or (128 < b < 512-128):
                continue
            c = a * self.w + b
            if self.a[c]:
                continue
            am =- 1

            d = 0
            while True:
                i = random.randrange(0,4)
                c0 = c + pot[i]
                if 0 <= c0 < self.w*self.h:
                    d += 1
                    c = c0
                    for p in pot:
                        c0 = c + p
                        if 0 <= c0 < self.w*self.h:
                            if self.a[c0] != 0:
                                self.a[c] = d
                                sz += 1
                                break
                    continue
                break

    def display(self):
        with open('brown.tga', 'wb') as f:
            s = struct.pack("<bbbhhbhhhhbb", 0, 0, 2, 0,0,0, 0, 0, 512, 512, 24, 0)
            f.write(s)
            
            black = struct.pack("<BBB", 0, 0, 0)
            white = struct.pack("<BBB", 255, 255, 255)
            red   = struct.pack("<BBB", 0, 0, 255)
            green = struct.pack("<BBB", 0, 255, 0)
            blue  = struct.pack("<BBB", 255, 0, 0)
            for i in range(0,self.h*self.w):
                y, x = divmod(i, self.w)

                if self.a[i] == 0:
                    f.write(black)
                elif self.a[i] < 10:
                    f.write(white)
                elif self.a[i] < 20:
                    f.write(red)
                elif self.a[i] < 30:
                    f.write(green)
                elif self.a[i] < 50:
                    f.write(blue)


bmap = Map(512,512)
bmap.populate(1<<10)
bmap.display()



