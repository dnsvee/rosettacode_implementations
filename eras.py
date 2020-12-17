from math import sqrt
def primefac(upto):
    d = [False] * upto
    p = []

    for f in range(2, upto):
        if not d[f]:
            print(f,end=', ')
            p.append(f)
            for e in range(f+f,upto,f):
                d[e] = True
    return p

pris = primefac(100000)
d = {}
for p in pris:
    d[int(str(p)[::-1])] = True

for k in pris:
    if d.get(k, False):
        print(k)

