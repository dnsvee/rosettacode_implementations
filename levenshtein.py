"""
Rosettacode task: Levensthein distance
"""

def levdist(a, ai, b, bi):
    me = levdist
    if ai == len(a):
        return len(b) - bi

    if bi == len(b):
        return len(a) - ai

    if a[ai] == b[bi]:
        return me(a, ai + 1, b, bi + 1)


    return 1 + min( me(a, ai + 1, b, bi + 1), me(a, ai, b, bi + 1), me(a, ai + 1, b, bi))

def levenstein(a, b):
    return levdist(a, 0, b, 0)


print("Levensthein distance between 'rosettacode' and 'raisethysword' is {}".format(levenstein("rosettacode", "raisethysword")))
print("Levensthein distance between 'sitting' and 'kitten' is {}".format(levenstein("sitting", "kitten")))
