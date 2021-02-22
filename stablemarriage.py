"""
Implementing the stable marriage problem:
"""

class Marriage:
    def __init__(self):
        self.Men          = {} # the man
        self.Women        = {} # the woman
        self.EngagedTo    = {} # dict of who's engaged to whom

        # least preferred to most preferred
        theproblem = """
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

        data = []
        for l in theproblem:
            person, prefs = l.split(': ', 1)
            prefs = list(reversed(prefs.split(', ')))
            data += [(person, prefs)]

        Men   = self.Men
        Women = self.Women

        for name, prefs in data[0:10]:
            Men[name]   = prefs

        for name, prefs in data[10:20]:
            Women[name] = prefs

        EngagedTo = self.EngagedTo

        while len(EngagedTo) < 20:
            for man in self.Men:
                # guy is already engaged
                if man in self.EngagedTo: 
                    continue

                # propose to the woman he most prefers over remaining
                woman = Men[man].pop()

                woman_engagedto = EngagedTo.get(woman, None)

                # neither man or woman are engaged so engage them
                if not woman_engagedto:
                    EngagedTo[woman] = man
                    EngagedTo[man]   = woman

                    print(woman, ' getting engaged to ', man)
                    continue

                wprefs = Women[woman]
                # see which man the woman prefers
                if wprefs.index(man) > wprefs.index(woman_engagedto):
                    print(woman, ' breaking engagement to ', woman_engagedto)
                    print(woman, ' getting engaged to ', man)
                    EngagedTo[woman] = man
                    EngagedTo[man]   = woman
                    del EngagedTo[woman_engagedto]

    def display(self):
        print('all engagements')
        for k, v in self.EngagedTo.items():
                print(k, ' engaged to ', v)

Marriage().display()


