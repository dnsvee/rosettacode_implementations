arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
arr = [-1, 5, 6, -2, 12]

def subsum(a):
    """
    Returns max subsum of string of digits using Kadane's algorithm
    """
    submax  = maxest = -9999
    index   = -1
    for k, v in enumerate(a):
        m = max(a[k], submax + a[k])
        if m > submax + v:
            submax = v
            index  = k
        else:
            submax += a[k]
        if submax > maxest:
            maxest = submax


    return maxest

m = subsum(arr)
print(m)





