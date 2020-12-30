from math import sqrt
def primefac(upto):
    sieve = [False] * upto
    prs = []

    for f in range(2, upto):
        if not sieve[f]:
            print(f,end=', ')
            prs.append(f)
            for e in range(f+f,upto,f):
                sieve[e] = True
    return prs

pris = primefac(100)
for p in primefac(1):
    print(p)

