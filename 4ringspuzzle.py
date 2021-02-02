"""
4 Rings puzzle
"""

digs = list(range(3,3+7))

a0 = []
a1 = digs[:]
X = 0

""" 
Solves an equation of the form: 
    """
while len(a1):
    a = a1.pop()
    b0 = []
    b1 = [*a0, *a1]
    while len(b1):
        b = b1.pop()
        X = a + b
        c0 = []
        c1 = [*b0, *b1]
        while len(c1):
            c = c1.pop()
            d = X - c - b
            if (d > 0 and (d in c0 or d in c1)):
                e0 = []
                e1 = [*c0, *c1]
                e1.remove(d)
                while (len(e1)):
                    e = e1.pop()
                    f = X - e - d
                    g = X - f
                    if f != g and f in [*e0,*e1] and g in [*e0, *e1]:
                        print('Sum={} a={} b={} c={} d={} e={} f={} g={}'.format(X, a, b, c, d, e, f, g))

                    e0.append(e)


            c0.append(c)

        b0.append(b)
    a0.append(a)

                

