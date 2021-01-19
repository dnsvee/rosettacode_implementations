
def pack(y, x):
    return y<<10|x

def unpack(c):
    return c>>10, c-((c>>10)<<10)
    return y, x

textualmap = """
....#....
##..#....
....#....
.#####.#.
.......#.
.......#.
"""[1:-1].split('\n')

He = len(textualmap)
Wi = len(textualmap[0])

# calculated distances
Di = {}
Ve = {}
for h in range(0,He):
    for w in range(0,Wi):
        li = textualmap[h]
        c  = pack(h, w)
        if li[w]   == ".":
            Ve[c] = [False, 1, None]
            Di[c] = 1<<32      # Distance from src
        elif li[w] == "#":
            Ve[c] = [True, 0, None]

src = [0,0]
dst = [3,3]

ps = pack(*src)
Di[ps] = 0
Ve[ps] = [False, 1, None] # visited

# set of verts to consider
Co = set()
Co.add(ps)

while len(Co):
    # find neighbour with lowest distance
    d0 = 1<<32
    cur = 0
    for k in Co:
        if Di[k] < d0:
            d0 = Di[k]
            cur = k
                
    Ve[cur][0] = True
    Co.remove(cur)

    # c is current
    h, w = unpack(cur)

    for y, x in [ [h-1, w], [h+1, w], [h, w-1], [h, w+1] ]:
        c = pack(y, x)
        if (0 <= y < He) and (0 <= x < Wi) and (Ve[c][1] > 0):
            if (Di[cur] + 1) < Di[c]:
                Di[c] = Di[cur] + 1
                Ve[c][2] = cur

                if not Ve[c][0]:
                    Co.add(c)



f = pack(He-1,Wi-1)
while True:
    Ve[f][1] = 2
    f = Ve[f][2]
    if f == None:
        break;

Ls = []
for y in range(0,He):
    Ll = []
    Ls.append(Ll)
    for x in range(0,Wi):
        c = pack(y,x)
        v = Ve[c][1]
        if v == 0:
            Ll.append('#')
        elif v == 1:
            Ll.append('.')
        elif v == 2:
            Ll.append('+')


Ls = map(lambda x: ''.join(x), Ls)

print('\n'.join(Ls))


