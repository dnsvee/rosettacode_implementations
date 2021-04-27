# solution for leetcode problem 32: Longest Valid Parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        if len(s) < 2: return 0        
        S = []
                
        # push every char on top of a stack
        # if top two items are matching pair then replace with number 2 (length of matching pair)
        # if top of stack is a matching pair with a number in between than replace pair with number 2 (length of matching pair)
        # while top two items are numbers (lengths) add them together into a single length
        # max length of valid parens is maximum number in the stack
        
        for p in s:
            if p == '(':
                S.append(-1)  
                
            if p == ')':
                if len(S) == 0:
                    continue
                    
                if S[-1] == -1:
                    S[-1] = 2
                    
                elif len(S) >= 2 and S[-1] > 0 and S[-2] == -1:
                    S[-2] = 2
                
                else:
                    S.append(-2)
                    continue
                    
                while len(S) >= 2 and S[-1] > 0 and S[-2] > 0:
                    S[-2] += S[-1]
                    S.pop()                                          
        
        S.append(0)
        
        return max(S)

    def test_suite(self):
        def test(s,n):
            ret = 'passed' if self.longestValidParentheses(s) == n else 'failed'
            print(ret)

        for s in [["(()", 2], [")()())", 4], ["", 0]]:
            test(*s)

Solution().test_suite()

            
