Edges = {}
E = Edges
# edges
E['a'] = { 'b' : 1, 'c' : 2 }
E['b'] = { 'd' : 5 }
E['c'] = { 'd' : 1 }
E['d'] = { }
B = {}

# verts
Verts = {'a', 'b', 'c', 'd'}
V = Verts

# calculated distances
Distances = {x : 1<<32 for x in V}
D = Distances

D['a'] = 0

# visited
Vx = set()

while len(V) > 0:
    d0 = 1<<32
    for k,v in D.items():
        if k in V: # unvisited
            if v < d0: 
                d0 = v
                W = k
    V.remove(W)

    for s0 in E[W].items():
        k, v = s0
        if k in V:
            if D[k] > D[W] + v:
                D[k] = D[W] + v
                B[k] = W

print('Distance to D = {}'.format(D['d']))

def print_path(W):
    W = 'd'
    print(W)
    while True:
        try:
            v = B[W]
        except KeyError:
            break
        print(v)
        W = v

print_path('d')


