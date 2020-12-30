"""
Knapsack problem 0-1
"""

maxcap = 400
items = [("", 0, 0),             # dummy item
         ("map", 9, 150), 
         ("compass", 13,  35), 
         ("water",  153, 200), 
         ("sandwich", 50, 160), 
         ("glucose", 15,  60), 
         ("tin", 68,  45),  
         ("banana", 27,  60), 
         ("apple", 39,  40), 
         ("cheese", 23,  30), 
         ("beer", 52,  10), 
         ("suntan", 11, 70), 
         ("camera", 32, 30), 
         ("tshirt", 24, 15), 
         ("trousers", 48, 10), 
         ("umbrella", 73, 40), 
         ("waterproof trousers", 42, 70), 
         ("waterproof overclothes", 43, 75), 
         ("notecase", 22, 80), 
         ("sunglasses", 7, 20), 
         ("towel", 18, 12),
         ("socks", 4, 50), 
         ("book", 30, 10)]

# V[(11, 100)] represents optimal value for any selection of first 11 items upto 100 units of weight.
V = {} 
for i in range(0,len(items)):
    for j in range(0,maxcap+1):
        V[(i,j)] = 0

# Generate table of subsolutions
for i in range(1,len(items)):
    for j in range(0,maxcap+1):
        it = items[i]
        if it[1] > j: 
            V[(i,j)] = V[(i-1,j)]
        else:
            V[(i,j)] = max(V[(i-1,j)], it[2] + V[(i-1,j-it[1])])

# Display all items selected tor optimal solution
i = len(items)-1
j = maxcap
print('Items in the knapsack for total value of {}:'.format(V[(len(items)-1,maxcap)]))
while i > 0:
    if V[(i,j)] > V[(i-1,j)]:
        # item selected
        print(items[i][0])
        j = j - items[i][1]
    i = i - 1











