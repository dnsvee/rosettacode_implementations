"""
Ackermann function
"""
def ack(m, n):
    if m > 0:
        if n > 0:
            return ack(m-1, ack(m, n-1))
        else:
            return ack(m-1,1)
    else:
        return n+1

for a in [ack(2,9), ack(3,4), ack(3,5), ack(3,6)]:
    print(a)

