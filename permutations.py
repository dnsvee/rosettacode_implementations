"""
Generate all permutations of a sequence. Implements the plain changes algorithm.
"""

def permutations(n):
    """
    n is length
    """

    if n < 1: raise ValueError("permutations: n must be > 1")

    # initial seed
    sub = [[1]] 

    # length of next permutation to produce
    n0 = 2

    # built permutations on increasing length until desired length reached
    while n0 <= n:
        res = [] 

        # for each perm. produced so far
        for e, l in enumerate(sub):

            # decide if permutation is at even or odd position according to plain changes algo
            rng = range(n0 - 1, -1, -1) if e % 2 == 0 else range(0, n0)

            # create three new permutations by adding element before, middle, after
            for i in rng:
                res.append([*l[:i], n0, *l[i:]]) 

        n0 += 1

        sub = res

    return sub

import timeit
Tim = timeit.Timer
rep = Tim(stmt='permutations(100)', globals=globals()).timeit(1)
print('Time to make 100 length all permutations is ', rep)
perms = permutations(16)
print(perms, len(perms))


