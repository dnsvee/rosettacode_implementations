
def howmanyjewels(s, j):
    cnt = 0
    for s0 in s:
        if s0 in j:
            cnt += 1

    return cnt

print(howmanyjewels('aAAbbbb', 'aA'))



