# implement the lcs (longest common substring) alogrithm

def lcs(s1, s2):
    m = [[0] * (len(s1) + 1) for _ in range(0, (len(s2) + 1))]

    for y in range(0, len(s2)):
        for x in range(0, len(s1)):
            if s1[x] == s2[y]:
                m[y+1][x+1] = m[y][x] + 1
            else:
                m[y+1][x+1] = max(m[y+1][x], m[y][x+1])

    y = len(s2)
    x = len(s1)

    print(m)

    while True:
        if m[y-1][x-1] < m[y][x]:
            print(s1[x])
            y -= 1
            x -= 1
        if m[y][x-1] > m[y-1][x]:
            x -= 1
        else:
            y -= 1


    return m[len(s2)][len(s1)]

r = lcs("strong", "stone")

