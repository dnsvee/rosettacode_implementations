import collections

perms = "abcd cabd acdb dacb bcda acbd adcb cdab dabc bcad cadb cdba cbad abdc adbc bdca dcba bacd badc bdac cbda dbca dcab".split(" ")
print(perms)
cols = []
for c in range(0,4):
    row = []
    for p in perms:
        row.append(p[c])
    cols.append(row)

cols = list(map(lambda x: collections.Counter(x), cols))
sol = ""
for c in cols:
    for k,v in c.items():
        if v == 5:
            sol += str(k)

print(sol)

