import unittest

def wildcard0(s, p, i, j):
    try:
        while p[j] == s[i] or p[j] == '?':
            i += 1
            j += 1
    except:
        return len(p) == j and len(s) == i

    # only here if * 
    return wildcard1(s, p, i, j)

def wildcard1(s, p, i, j):
    while p[j] == '*':
        if wildcard0(s, p, i, j + 1):
            return True
        i += 1
    return False

def wildcard(s, p):
    return wildcard0(s, p, 0, 0)


class TestMe(unittest.TestCase):
    def test_me(self):
        istrue = self.assertTrue
        istrue(wildcard("babab", "bab**"))
        istrue(wildcard("abc", "?b?"))
        istrue(wildcard("aaaabbb", "a***b"))
        istrue(wildcard("acdcb", "a***b"))
        

a = wildcard("acdcb", "acdcb*")
print(a)



#unittest.main()



