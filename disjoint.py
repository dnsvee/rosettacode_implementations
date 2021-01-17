class UnionFind:
    def __init__(self, N):
        self.N = N
        # pair of rank, root
        self.A = [e for e in range(0, self.N)]
        self.S = {e:1 for e in self.A} # size of tree
        pass

    def root(self, a):
        A = self.A
        r = a
        while r != A[r]:
            r = A[r]
            A[r] = A[A[r]]
        return r

    def qunion(self, a, b):
        # union two sets with weigthed tree and path compression
        ra, rb = self.root(a), self.root(b)
        if ra == rb:
            # already rooted
            return

        # check size
        S = self.S
        A = self.A
        if S[ra] >= S[rb]:
            r0, r1 = ra, rb
        else:
            r0, r1 = rb, ra

        A[r1] = r0
        S[r0] += S[r1]
        del S[r1] 

    def qfind(self, a, b):
        ra, rb = self.root(a), self.root(b)
        return ra == rb

    def __repr__(self):
        return ' '.join((str(a) for a in self.A))

uf = UnionFind(6)

uf.qunion(1,2)
uf.qunion(2,3)
print(uf)
print(uf.qfind(1,3))
print(uf.qfind(1,4))
