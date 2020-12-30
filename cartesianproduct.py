"""
Cartesian product of two or more lists
"""

def cartprod(a,b):
    return [(a0,b0) for a0 in a for b0 in b]

print(cartprod([1,2], [3,4]))
print(cartprod([3,4] ,[1,2]))
print(cartprod([1,2], []))
print(cartprod([], [1,2]))
print(cartprod([], []))

