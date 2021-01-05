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
    p = l[random.randrange(0, len(l))]
    while len(l):
        i = l.pop()
        if i < p: b.append(i)
        if i > p: a.append(i)
        if i == p: m.append(i)
    return b + m + a

b = clockit(swapsort, "swapsort", bunch[:])
b = clockit(swapsort, "swapsort sorted", b)
b = clockit(selsort, "selection sort", bunch[:])
b = clockit(qsort, "quicksort", bunch[:])




