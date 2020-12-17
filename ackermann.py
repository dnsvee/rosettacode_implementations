def ack(m, n):
    if m > 0:
        if n > 0:
            return ack(m-1, ack(m, n-1))
        else:
            return ack(m-1,1)
    else:
        return n+1


print(ack(3,4))
print(ack(3,5))
print(ack(3,6))
