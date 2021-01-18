"""
First attempt at stable-marriage problem
"""
class Marriage:
    def __init__(self):
        self.Men          = {}
        self.Women        = {}
        self.total        = 0

        aman   = self.aman
        awoman = self.awoman

        # last is most prefered
        aman('A', ['Z', 'X', 'Y'])
        aman('B', ['X', 'Y', 'Z'])
        aman('C', ['Y', 'Z', 'X'])

        awoman('X', ['C', 'A', 'B'])
        awoman('Y', ['A', 'B', 'C'])
        awoman('Z', ['B', 'C', 'A'])


        Men   = self.Men
        Women = self.Women

        while self.total != len(self.Men):
            for m in self.Men:
                if m[0] == None: 
                    continue
                self.proposed(self.propose(m), m)

    # easy setter
    def aman(self, n, prefs):
        # prefs is list
        self.Men[n]   = [ None, prefs ]

    def awoman(self, n, prefs):
        # prefs is dict
        self.Women[n] = [ None, {k:i for i, k in enumerate(prefs)} ]

    # return to man proposes
    def propose(self, M):
        return self.Men[M][1].pop()

    # engages men to woman if appicable break existing engagement
    def proposed(self, W, M):
        woman = self.Women[W]
        man   = self.Men[M]

        k = woman[0]
        if not k:
            woman[0] = M
            man[0]   = W
            self.total += 1
            return

        p1, p2 = woman[1][M], woman[1][k]
        if p1 > p2:
            woman[0] = M
            man[0] = W
            k[0] = None

    # uses chainmap for nexttime
    def display(self):
        for k, v in self.Men.items():
            if v[0]:
                print(k, ' engaged to', v[0])
            else:
                print(k, ' not engaged')
        for k, v in self.Women.items():
            if v[0]:
                print(k, ' engaged to ', v[0])
            else:
                print(k, ' not engaged')

Mars = Marriage()
Mars.display()


