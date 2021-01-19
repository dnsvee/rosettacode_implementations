tosort = [7,6,5,4,3,2,1]

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
        # trouble
        a[i-1], a[j-1] = a[j-1], a[i-1]
        heapify(a, sz, j)

def makeheap(a):
    m = len(a)//2
    for i in range(m, 0, -1):
        heapify(a, len(a), i)

def heapsort(a):
    makeheap(a)
    for i in range(len(a), 0, -1):
        a[i-1], a[0] = a[0], a[i-1]
        heapify(a, i-1, 1)

