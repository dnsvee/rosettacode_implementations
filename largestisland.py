"""
Can you flip a single 0 to 1 to make a larger island?
"""
def largeIsland(grid):
    n = len(grid)
    
    grid = [i for y in grid for i in y]

    if not any(grid):   return 1
    if all(grid):       return n * n

    A = []
    S = {} 

    # initialize for union-find algo
    for y in range(0, n * n):
        A.append(y)
        S[y] = 1

    def root(a):
        # path crunching
        while  A[a] != a:
            a = A[a]
            A[a] = A[A[a]]
        return a

    # a, b are roots
    def union(a, b):
        if S[a] > S[b]:
            A[b] = a
            S[a] += S[b]
            del S[b]
        else:
            A[a] = b
            S[b] += S[a]
            del S[a]        

    # combine islands if connected
    def comb(a, b):
        if grid[a] == 1 and grid[b] == 1:
            a = root(a)
            b = root(b)
            if a != b:
                union(a, b)
    
    for y in range(0, n):
        for x in range(0, n):
            if x != n - 1:
                comb(y       * n + x, y * n + x + 1)
            if y != n - 1:
                comb((y + 1) * n + x, y * n + x    )

    W = T = 0

    # iterate over 0 elements and see if flipping them matters
    for y in range(0, n):
        for x in range(0, n):
            U = {}
            if grid[y * n + x] == 0:
                c = (y - 1) * n + x
                if y > 0 and grid[c] == 1:
                    U[root(c)] = True

                c = (y + 1) * n + x 
                if y < n - 1 and grid[c] == 1:
                    U[root(c)] = True

                c = y * n + x - 1
                if x > 0 and grid[c] == 1:
                    U[root(c)] = True

                c = y * n + x + 1
                if x < n - 1 and grid[c] == 1:
                    U[root(c)] = True

                tot = 0
                for u in U:
                    tot += S[u]
                if tot > T:
                    T = tot
                    w = y * n + x

    # return largest island you can make with flipping one zero to one
    return T + 1

r = largeIsland([[1, 1, 0], [1, 0, 1], [0, 1, 1]])
print(r)



