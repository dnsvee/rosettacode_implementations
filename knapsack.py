"""
Knapsack problem
"""

class Item:
    def __init__(self, n, w, v):
        self.n = n
        self.v = v
        self.w = w

    def __repr__(self):
        return "{}:{}:{}".format(self.n,self.w,self.v)

class Knapsack:
    def __init__(self):
        self.items = []
        self.best = []
        self.mx = 400
        self.append("map",      9, 150)
        self.append("compass", 13,  35)
        self.append("water",  153, 200, 2)
        self.append("sandwich", 50, 60, 2)
        self.append("glucose", 15,  60, 2)
        self.append("tin", 68,  45, 3)
        self.append("banana", 27,  60, 3)
        self.append("apple", 39,  40, 3)
        self.append("cheese", 23,  30)
        self.append("beer", 52,  10, 3)
        self.append("suntan", 11, 70)
        self.append("camera", 32, 30)
        self.append("tshirt", 24, 15, 2)
        self.append("trousers", 48, 105, 2)
        self.append("umbrella", 73, 40)
        self.append("waterproof trousers", 42, 70)
        self.append("waterproof overclothes", 43, 75)
        self.append("notecase", 22, 80)
        self.append("sunglasses", 7, 20)
        self.append("towel", 18, 12, 2)
        self.append("socks", 4, 50)
        self.append("book", 30, 10, 2)

    def append(self, n, w, v, c = 1):
        for r in range(0,c):
            self.items.append(Item(n, w, v))

    def cand(self, v, c):
        self.best.append((v,c))

    def packsack0(self, cur, value, wght, idx):
        if idx == len(self.items):
            self.cand(value, cur)
            return

        i = self.items[idx]
        if i.w + wght < self.mx:
            c = cur[:]
            c.append(idx)
            self.packsack0(c, value+i.v, wght+i.w, idx+1)
        self.packsack0(cur, value, wght, idx+1)

    def pack(self):
        self.packsack0([], 0, 0, 0)
        self.best = sorted(self.best, key=lambda x : x[0])[0:10]
        for b in self.best:
            print("{} value:".format(b[0]), end="")
            for c in b[1]:
                print(self.items[c].n, end=" ")
            print("\n")


Knapsack().pack()





