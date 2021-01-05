"""
rot-13 cypher
"""

# returns rot13 encoding of string. only works on actual chars and space
def rot13(inp, amap = {}):
    if not len(amap):
        orda = ord('a')
        ordz = ord('z')
        ordA = ord('A')
        ordZ = ord('Z')
        res = []
        amap = {}
        for m in range(0,26):
            _, r = divmod(m+13,26)
            amap[chr(orda+m)] = chr(orda+r)
            amap[chr(ordA+m)] = chr(ordA+r)
        amap[' '] = ' '
    
    res = []
    for c in inp:
        res.append(amap[c])

    return ''.join(res)

print(rot13("It is the best of times"))


