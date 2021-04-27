def wagfish(s, p):
    D = {}
    for j in range(0, len(p) + 1): D[(0, j)] = j
    for i in range(0, len(s) + 1): D[(i, 0)] = i
    cost = 0 
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if s[i-1] == p[j-1]:
                cost = 0
            else:
                cost = 1
            D[(i,j)] = min(D[(i-1,j)]+1, D[(i,j-1)]+1, D[(i-1,j-1)] + cost)
    return D[(len(s), len(p))]


edit = wagfish("saturday", "sunday")
edit = wagfish("sitting", "kittten")
print('edit = ', edit)


