"""
Jewels and stones
"""
def howmanyjewels(s, j):
    return len([s0 for s0 in s if s0 in j])

print(howmanyjewels('aAAbbbb', 'aA'))



