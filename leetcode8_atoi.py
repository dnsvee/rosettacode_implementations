# solution to leetcode problem 8

class Solution:
    def myAtoi(self, s: str) -> int:
        val  = 0
        sign = 1
        try:
            i = 0
            
            # skip whitespace
            while s[i] == ' ':
                i   += 1
                
            # check sign
            if   s[i] == '-': 
                sign = -1
                i   +=  1
            elif s[i] == '+': 
                sign =  1
                i   += 1
                
            # convert string to number
            ord0 = ord('0')
            while '0' <= s[i] <= '9':
                val  = val * 10 + ord(s[i]) - ord0
                i   += 1
            
        finally:
            # do the overflow fix
            return min(max(val * sign, -2147483648), 2147483647)
