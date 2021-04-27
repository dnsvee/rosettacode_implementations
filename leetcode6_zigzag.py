# solution to leetcode #6 zigzag conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        
        # take the initial string and write it down into the required zigzag
        #  pattern & use a dict for the result
        # key of dict is (y, x) tuple with y the line and x the column of 
        # the appropriate character of string s in the right spot
        # value of key is the right char of string s
        
        D    = {}
        y, x = 0, 0 # initial position of the zigzag pattern in the dict D
        i    = 0    # position of char of string s being handled
        try:
            while True:
                D[(y, x)] = s[i]
                
                if (i // (numRows-1)) % 2 == 0:
                    # zigzag down
                    y += 1
                else:
                    # zigzag along the diagonal upwards
                    y -= 1
                    x += 1
                    
                i += 1
        except:
            # sorts the dict into a list with the key coordinate tuple as sorting 
            # key so the result is [(0,0), (0,1), (0,2) ... ] 
            # then extract the letter and join into result string
            
            return ''.join(map(lambda x : x[1], sorted([*D.items()], key=lambda x: x[0])))
           
            
