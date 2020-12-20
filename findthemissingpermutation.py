import collections

perms = "abcd cabd acdb dacb bcda acbd adcb cdab dabc bcad cadb cdba cbad abdc adbc bdca dcba bacd badc bdac cbda dbca dcab".split(" ")
cols = [[p[i] for p in perms] for i in range(0,4)]

cols = list(map(lambda x: collections.Counter(x), cols))

# should be 6 of the same letter in every column. if only 5 present then it is the missing permutation
sol = ""
for c in cols:
    for k,v in c.items():
        if v == 5:
            sol += str(k)

print(sol)

