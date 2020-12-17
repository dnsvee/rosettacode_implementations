import itertools
perm = itertools.permutations

class Occ:
    def __init__(s, **kw):
        s.nat = kw.get('nat',None)
        s.dri = kw.get('dri',None)
        s.smo = kw.get('som',None)
        s.col = kw.get('col',None)
        s.pet = kw.get('pet',None)

    def __repr__(self):
        return '{} {} {} {} {}'.format(self.nat, self.dri, self.smo, self.col, self.pet)
        pass

H = [Occ(nat='norwegian'), Occ(col='blue'), Occ(dri='milk'), Occ(), Occ()]

def rule2():
    for a in range(2,5):
        H[a].nat, H[a].col = 'english', 'red'
        rule3()
        H[a].nat, H[a].col = None, None

def rule3():
    for b in range(0,5):
        if not H[b].nat:
            H[b].nat, H[b].pet = 'swedish', 'dog'
            rule4()
            H[b].nat, H[b].pet = None, None

def rule4():
    for c in range(0,5):
        if not H[c].nat and not H[c].dri:
            H[c].nat, H[c].dri = 'dane', 'tea'
            rule6()
            H[c].nat, H[c].dri = None, None

def rule6():
        for d in range(0,5):
            if not H[d].dri and not H[d].col:
                H[d].dri, H[d].col = 'coffee', 'green'
                rule7()
                H[d].dri, H[d].col = None, None

def rule7():
        for e in range(0,5):
            if not H[e].pet:
                H[e].pet, H[e].smo = 'birds', 'pallmall'
                rule8()
                H[e].pet, H[e].smo = None, None

def rule8():
        for f in range(0,5):
            if not H[f].col and not H[f].smo:
                H[f].col, H[f].smo = 'yellow', 'dunhill'
                rule13()
                H[f].col, H[f].smo = None, None 

def rule13():
        for f in range(0,5):
            if not H[f].smo and not H[f].dri:
                H[f].smo, H[f].dri = 'bluemaster', 'beer'
                rule14()
                H[f].smo, H[f].dri = None, None 

def rule14():
        for g in range(0,5):
            if not H[g].nat and not H[g].smo:
                H[g].nat, H[g].smo = 'german', 'price'
                rule5()
                H[g].nat, H[g].smo = None, None 


def rule5():
        # white house to right of green
        for h in range(0,4):
            if H[h].col == 'green':
                if not H[h+1].col:
                     H[h+1].col = 'white'
                     rule12()
                     H[h+1].col = None

def rule12():
    for i in range(0,5):
        if H[i].smo == 'dunhill':
            if i > 0 and not H[i-1].pet:
                H[i-1].pet = 'horse'
                rulelast()
                H[i-1].pet = None

            if i < 4 and not H[i+1].pet:
                H[i+1].pet = 'horse'
                rulelast()
                H[i+1].pet = None


def rulelast():
    for i in range(0,5):
        if H[i].smo == None:
            H[i].smo = 'blend'
            break

    for i in range(0,5):
        if H[i].dri:
            H[i].dri = 'water'
            break

    for i in range(0,5):
        if H[i].smo == 'blend':
            if i > 0:
                H[i-1].pet = 'cats'
            if i < 4:
                H[i+1].pet = 'cats'

    for i in range(0,5):
        if H[i].pet == None:
            H[i].pet = 'zebra'

    print(H)


rule2()
