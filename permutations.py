"""
Generate all permutations of a sequence. Implements the plain changes algorithm.
"""

def permutations(n):
    """
    n is length of every permutation
    """

    if n < 1: raise ValueError("permutations: n must be > 1")

    sub = [[1]] # all permuattions of list length 1

    n0 = 2 # next permutation to produce

    # loop until all perms. produced
    while n0 <= n:
        res = [] 

        # for each perm. produced so far
        for e, l in enumerate(sub):

        # decide if permutation is at even or odd position
            for i in range(n0 - 1, -1, -1) if e % 2 == 0 else range(0, n0 - 1 + 1):
                res.append( [*l[:i], n0, *l[i:]] ) # create new perm. by embedding 'n' at every possible position in ascending or descending order

        n0 += 1

        l = res # list just made becomes new input

    return l

import timeit
Tim = timeit.Timer
Tim(stmt='permutations(100)', globals=globals()).timeit(1)


