from fractions import Fraction

def num2(a, b):
    yield a + b
    yield a - b
    yield b - a
    yield a * b
    if b != 0:
        yield a / b
    if a != 0:
        yield b / a


f1 = Fraction(2)
f2 = Fraction(3, 5)

def num4(h, i, j, k):
    for a, b, c, d in [(h,i,j,k), (h,j,i,k), (h,k,i,j)]:
        for n0 in num2(a, b):
            for n1 in num2(c, d):
                for x in num2(n0, n1):
                    if x == 24:
                        return True
    return False

print(num4(1,3,4,6))






