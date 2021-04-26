def island(grid):
    n = len(grid)
    
    # flatten teh array
    grid = [i for y in grid for i in y]
    
    # no land; change one sea to one land
    if not any(grid): return 1
    
    # all land so result is grid_size ** 2
    if     all(grid): return n * n

    # A is the array used for the union-find algorithm
    # S is the size of elements in the set
    A = []
    S = {} 

    # init each element in it's own set
    for y in range(0, n * n):
        A.append(y)
        S[y] = 1

    # find root of elem a
    def root(a):
        while  A[a] != a:
            a    = A[a]
            A[a] = A[A[a]]
        return a

    # put a&b in the same set
    def union(a, b):
        a = root(a)
        b = root(b)
        if a != b:
            S[a] += S[b] # recalc. size
            A[b]  = a
    
    # combine two cells if they are land (1)
    def comb(a, b):
        if grid[a] == 1 and grid[b] == 1:
            union(a, b)
    
    # combine all cells that are land; take care of edges
    for y in range(0, n):
        for x in range(0, n):
            if x != n - 1:
                comb(y       * n + x, y * n + x + 1)
            if y != n - 1:
                comb((y + 1) * n + x, y * n + x    )


    maxsize = 0

    # iterate over all sea cells and for each cell find all the land masses connected to it
    # and sum size of all islands
    # find the cell that produces the maximum score 
    
    # temp. dict used to store all land masses connected to a single sea cell 
    U = {}
    for y in range(0, n):
        for x in range(0, n):
            U.clear()
            # if cell is sea
            if grid[y * n + x] == 0:
                c = (y - 1) * n + x
                # if north neighbour is land store root of set which it belongs to
                if y > 0 and grid[c] == 1:
                    U[root(c)] = True

                c = (y + 1) * n + x 
                # for the south
                if y < n - 1 and grid[c] == 1:
                    U[root(c)] = True

                c = y * n + x - 1
                # for the west
                if x > 0 and grid[c] == 1:
                    U[root(c)] = True

                c = y * n + x + 1
                # for the east
                if x < n - 1 and grid[c] == 1:
                    U[root(c)] = True

                # combine all connected lands into one land mass and compute the total size
                tot = 0
                for u in U:
                    tot += S[u]
                    
                #  keep track of max. landmass size
                if tot > maxsize:
                    maxsize = tot

    return maxsize + 1 # + 1 is for sea chaged to land
    

class Solution:
    def largestIsland(self, grid):
        return island(grid)

    def test_suite(self):
        def test(k, v): 
            n = island(k)
            if n == v:
                print('success')
            else:
                print('failed; expected %i, got %i' % (v, n))

        test([[1,0],[0,1]], 3) 
        test([[1,1],[1,0]], 4)
        test([[1,1],[1,1]], 4)

Solution().test_suite()
