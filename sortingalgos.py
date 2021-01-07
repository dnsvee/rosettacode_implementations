import random, time
""" 
Implements some popular sorting algorithms
"""

bunch = [random.randrange(0,1<<20) for i in range(0,1<<20)]

# chcks if array is sorted min > max
def checkit(b):
    for i in range(0,len(b)-1):
        if b[i] > b[i+1]:
            return False
    return  True

# clocks a sorting function
# ex. clockit(sortfun, tosort)
def clockit(l, desc, *args):
    s = time.time()
    r = l(*args)
    e = time.time()
    print("sorted {} with {} in {}s".format(len(r), desc, e-s), end='')
    checkit(r)
    if not r:
        print(': failed', end='')
    print('\n')
    return r

def swapsort(b):
    # keep swapping consecutive items if not sorted
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

# insertion sort 
def selsort(b):
    i = 1
    while i < len(b):
        j = i
        while j >= 0 and b[j-1] > b[j]:
                b[j], b[j-1] = b[j-1], b[j]
                j -= 1
        i += 1
    return b

# quicksort: not in-place
def qsort(l):
    rec = qsort
    if len(l) < 2:
        return l

    b, m, a = [], [], []
    p = l[random.randint(0,len(l)-1)]
    while len(l):
        i = l.pop()
        if i < p: b.append(i)
        if i > p: a.append(i)
        if i == p: m.append(i)
    return qsort(b) + m + qsort(a)


# merges two sorted arrays into one sorted array
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

# merge sort: not in-place
def mergesort(tosort):
    if len(tosort) == 2:
        return merge(tosort[:1], tosort[-1:])
    if len(tosort) == 1:
        return tosort
    m = len(tosort) // 2
    tosort, tosort2 = tosort[:m], tosort[-m:]
    return merge(mergesort(tosort), mergesort(tosort2))

# the builtin sort
def builtinsort(tosort):
    tosort = sorted(tosort)
    return tosort

# well-known heapify
def heapify(a, sz, i):
    j = i
    l = a[i-1]
    if (  i*2) <= sz and a[(i*2)-1] > l:
        j = i * 2
        l = a[j-1]
    if (1+i*2) <= sz and a[(i*2)  ] > l:
        j = i * 2 + 1
        l = a[j-1]
    if i != j:
        # heap out of order
        a[i-1], a[j-1] = a[j-1], a[i-1]
        heapify(a, sz, j)

# turn array into heap
def makeheap(a):
    m = len(a)//2 # last parent node
    for i in range(m, 0, -1):
        heapify(a, len(a), i)

# famous heapsort: in-place, still slow
def heapsort(a):
    makeheap(a)
    for i in range(len(a), 0, -1):
        a[i-1], a[0] = a[0], a[i-1]
        heapify(a, i-1, 1)
    return a

def testthese(*totest):
    counts = []
    payload = [random.randrange(0,1<<16) for i in range(0,1<<16)]
    for n, f in totest:
        counts.append(clockit(f, n, payload[:]))
    if not all(map(lambda x : len(x) == len(counts[0]), counts)):
        print("inconsistent results")

testthese(("quicksort", qsort), ("heapsort", heapsort), ("mergesort", mergesort), ("builtinsort", builtinsort))







