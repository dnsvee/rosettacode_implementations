import unittest

def wildcard0(s, p, i, j):
    try:
        while p[j] == s[i] or p[j] == '?':
            i += 1
            j += 1
    finally:
        if len(p) == j and len(s) == i:
            return True

    # only here if * 
    return wildcard1(s, p, i, j)

def wildcard1(s, p, i, j):
    while p[j:j+1] == '*':
        if wildcard0(s, p, i, j + 1):
            return True
        i += 1
    return False

def wildcard(s, p):
    return wildcard0(s, p, 0, 0)


class TestMe(unittest.TestCase):
    def test_me(self):
        istrue = lambda x, y : self.assertTrue(wildcard(x, y))
        istrue("babab", "bab**")
        istrue("abc", "?b?")
        istrue("aaaabbb", "a***b")
        istrue("acdcb", "a***b")
        

a = wildcard("acdcb", "a*c")
#a = wildcard("acdcb", "a*c?b")
print(a)



#unittest.main()



