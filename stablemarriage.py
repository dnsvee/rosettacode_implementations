"""
First attempt at stable-marriage problem
"""


class Marriage:
    def __init__(self):
        self.Men          = {}
        self.Women        = {}
        self.EngagedTo    = {}
        self.total        = 0

        ex = """
abe: abi, eve, cath, ivy, jan, dee, fay, bea, hope, gay
bob: cath, hope, abi, dee, eve, fay, bea, jan, ivy, gay
col: hope, eve, abi, dee, bea, fay, ivy, gay, cath, jan
dan: ivy, fay, dee, gay, hope, eve, jan, bea, cath, abi
ed: jan, dee, bea, cath, fay, eve, abi, ivy, hope, gay
fred: bea, abi, dee, gay, eve, ivy, cath, jan, hope, fay
gav: gay, eve, ivy, bea, cath, abi, dee, hope, jan, fay
hal: abi, eve, hope, fay, ivy, cath, jan, bea, gay, dee
ian: hope, cath, dee, gay, bea, abi, fay, ivy, jan, eve
jon: abi, fay, jan, gay, eve, bea, dee, cath, ivy, hope
abi: bob, fred, jon, gav, ian, abe, dan, ed, col, hal
bea: bob, abe, col, fred, gav, dan, ian, ed, jon, hal
cath: fred, bob, ed, gav, hal, col, ian, abe, dan, jon
dee: fred, jon, col, abe, ian, hal, gav, dan, bob, ed
eve: jon, hal, fred, dan, abe, gav, col, ed, ian, bob
fay: bob, abe, ed, ian, jon, dan, fred, gav, col, hal
gay: jon, gav, hal, fred, bob, abe, col, ed, dan, ian
hope: gav, jon, bob, abe, ian, dan, hal, ed, col, fred
ivy: ian, col, hal, gav, fred, bob, abe, ed, jon, dan
jan: ed, hal, gav, abe, bob, jon, col, ian, fred, dan
"""[1:-1].split('\n')

        list1 = []
        for l in ex:
            prs, prefs = l.split(': ', 1)
            prefs = list(reversed(prefs.split(', ')))
            list1.append((prs,prefs))

        aman   = self.aman
        awoman = self.awoman

        for i in range(0,10):
            aman(*list1[i])

        for i in range(10,20):
            awoman(*list1[i])

        print(self.Men)

        Men   = self.Men
        Women = self.Women

        while self.total < len(self.Men):
            for m in self.Men:
                if m in self.EngagedTo: 
                    continue
                self.proposed(self.propose(m), m)

    # easy setters
    def aman(self, n, prefs):
        # prefs is list
        self.Men[n]   = [ None, prefs ]

    def awoman(self, n, prefs):
        # prefs is dict
        self.Women[n] = [ None, {k:i for i, k in enumerate(prefs)} ]

    # return woman the man most prefers left over from those he has not proposed to so far
    def propose(self, M):
        return self.Men[M][1].pop()

    # engages men and woman if woman prefers the men over whom she is engaged so she may rethink her engagement
    def proposed(self, W, M):
        woman = self.Women[W]
        man   = self.Men[M]

        EngagedTo = self.EngagedTo
        woman_engagedto = EngagedTo.get(W, None)
        if not woman_engagedto:
            EngagedTo[W] = M
            EngagedTo[M] = W
            self.total += 1
            print('getting engaged: ', M, W)
            return

        p1, p2 = woman[1][M], woman[1][woman_engagedto]
        if p1 > p2:
            print('breaking engagament: ', W, woman_engagedto)
            print('getting engaged: ', M, W)
            EngagedTo[W] = M
            EngagedTo[M] = W
            del EngagedTo[woman_engagedto]

    # uses chainmap for nexttime
    def display(self):
        for k, v in self.EngagedTo.items():
                print(k, ' engaged to ', v)

Mars = Marriage()
Mars.display()


