import unittest

class TestMe(unittest.TestCase):
    def test_me(self):
        istrue = lambda x, y : self.assertTrue(domatch(x, y))
        isfalse = lambda x, y : self.assertFalse(domatch(x, y))
        istrue ("babab", "bab**")
        istrue ("aaaabbb", "a***b")
        istrue ("acdcb", "a***b")
        istrue ("ac", "a*c")
        istrue ("ac", "**a**c**")
        istrue ('abc', "a?c")
        istrue ('abc', "a*c")
        istrue ('abc', "a*?c")
        istrue ('abc', "???")
        istrue ('abc', "?*?")
        istrue ('abc', '*a*c')
        isfalse("abc", "a*d")
        isfalse("abc", "b")
        

def mletter(s, p, i, j):
    return p[j] == s[i] or p[j] == '?'

def match(s, p, i, j):
    while True:
        if p[j] == '*':
            if j + 1 == len(p): return True # found

            if p[j + 1] == '*':
                j += 1
                continue

            j += 1
            while i < len(s):
                if mletter(s, p, i, j) and match(s, p, i, j): return True
                i += 1
            return False

        else: # letter
            while i < len(s) and j < len(p) and mletter(s, p, i, j):
                i += 1
                j += 1

            if j == len(p): return i == len(s)

            if p[j] == '*': return match(s, p, i, j)
                
            return False

def domatch(s, p):
    if s == p:     return True
    if not len(p): return False
    return match(s, p, 0, 0)


unittest.main()



