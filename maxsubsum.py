samples = [
            [-2, 1, -3, 4, -1, 2, 1, -5, 4],
            [-1, 5, 6, -2, 12]
          ]

def subsum(a):
    """
    Returns max subsum of string of digits using Kadane's algorithm
    """
    submax   = -1 << 31
    index    = -1
    maxofarr = submax
    span = 0
    for k, v in enumerate(a):
        if v > submax + v:
            submax = v
            index  = k
            span = 1
        else:
            span += 1
            submax += v
        maxofarr = max(submax, maxofarr)

    return maxofarr, index

for a in samples:
    m, i = subsum(a)
    print('subsum of ', a, ' = ', m, i)





