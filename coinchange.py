"""
Coin changing problem using dynamic programming
"""

def  changecoin(denoms, change):
    row = [0]
    for c in range(1, change + 1):
        M = 2<<16 # minimum coins needed

        d0 = 0 # 
        for d in denoms:
            if c - d < 0: # coin cant be used
                continue

            if row[c - d] < M:
                M = row[c - d] 
                d0 = d

        row.append(row[c-d0] + 1)

    asum = 0
    while change > 0:
        for d in denoms:
            if change - d >= 0:
                if row[change - d] + 1 == row[change]:
                    change -= d
                    asum += d
                    print(d, end=' ')
    print(' = ', asum)

    return M


res = changecoin([1, 2, 5], 11)
print(res)









