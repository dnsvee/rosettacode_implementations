# working solution for Valid Number #65 problem on Leetcode

class Solution:
    def isNumber(self, s: str) -> bool:                 
      c = False
      try:
        i = 0
        if s[0] == '-' or s[0] == '+':
            c = False
            i = 1   
        d = False
        if s[i] == '.':
            d = True
            c = False
            # must follow a digit
            i += 1        
            
        while s[i].isdigit():
            c = True
            i += 1
            
        if s[i] == '.':
            if d: return False
            i += 1
            while s[i].isdigit():
                i += 1        
          
        if not c: return False
        if s[i] == 'e' or s[i] == 'E':           
            c = False
            i += 1
            
            if s[i] == '-' or s[i] == '+':
                i += 1            
            
            while s[i].isdigit():
                c = True
                i += 1
                
            return False
      except:
        return c

    def testsuite(self):
        def test(s, exp):
            if self.isNumber(s) != exp: raise ValueError('test failed for %s' % s)

        istrue  = lambda s : test(s, True)
        isfalse = lambda s : test(s, False)

        istrue('123')
        istrue('1.4')
        isfalse('abc')


            
Solution().testsuite()
