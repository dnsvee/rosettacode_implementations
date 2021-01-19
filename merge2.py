import random

def merge(a, b):
    i = j = 0
    r = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            r.append(a[i])
            i += 1
        else:
            r.append(b[j])
            j += 1
    if i < len(a):
        r.extend(a[i:])
    if j < len(b):
        r.extend(b[j:])

    return r

def mergesort(l):
    trail = []
    if len(l) < 2:
        return l
    trail.extend([1,1])
    upto = 2
    while True:
        if len(trail)>1:
            b = trail[-1]
            a = trail[-2]
            if a == b:
                x = merge(l[upto-b-a:upto-b], l[upto-b:upto])
                print(trail)
                print(x)
                print()
                l[upto-a-b:upto] = x
                trail[-2] += trail[-1]
                trail.pop()
                continue
        if upto < len(l):
            trail.append(1)
            upto += 1
        if upto == len(l) and len(trail) == 1:
            break
    return l










 



