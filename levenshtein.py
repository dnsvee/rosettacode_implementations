"""
Rosettacode task: Levensthein distance
"""

def levdist(a,b):
    me = levdist
    if not len(a) and not len(b):
        return 0

    if len(a) and not len(b):
        return len(a)

    if not len(a) and len(b):
        return len(b)

    if a[0] == b[0]:
        return me(a[1:], b[1:])


    return 1 + min(me(a[1:], b[1:]), me(a, b[1:]), me(a[1:], b))


print("Levensthein distance between 'rosettacode' and 'raisethysword' is {}".format(levdist("rosettacode", "raisethysword")))
print("Levensthein distance between 'sitting' and 'kitten' is {}".format(levdist("sitting", "kitten")))
