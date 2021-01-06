import random, time

bunch = [random.randrange(0,1<<14) for i in range(0,1<<14)]

def checkit(b):
    for i in range(0,len(b)-1):
        if b[i] > b[i+1]:
            return False
    return  True

def clockit(l, desc, *args):
    s = time.time()
    r = l(*args)
    e = time.time()
    print("{} in {:.2}s".format(desc, e-s), end='')
    checkit(r)
    if not r:
        print(': failed', end='')
    print('\n')
    return r


# assumes len(b) > 1
def swapsort(b):
    done = False
    while not done:
        done = True
        for i in range(0,len(b)-1):
            if b[i+1] < b[i]:
                done = False
                b[i], b[i+1] = b[i+1], b[i]
        if done:
            break
    return b

def selsort(b):
    i = 1
    while i < len(b):
        j = i
        while j >= 0 and b[j-1] > b[j]:
                b[j], b[j-1] = b[j-1], b[j]
                j -= 1
        i += 1
    return b

def qsort(l):
    rec = qsort
    if len(l) < 2:
        return l

    b, m, a = [], [], []
    p = l[len(l) // 2]
    while len(l):
        i = l.pop()
        if i < p: b.append(i)
        if i > p: a.append(i)
        if i == p: m.append(i)
    return b + m + a

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

b = clockit(swapsort, "swapsort", bunch[:])
b = clockit(swapsort, "swapsort sorted", b)
b = clockit(selsort, "selection sort", bunch[:])
b = clockit(qsort, "quicksort", bunch[:])
b = clockit(mergesort, "mergesort", bunch[:])




