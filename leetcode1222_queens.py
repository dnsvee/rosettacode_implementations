# solution to problem 1224 from leetcode

class Solution:
    def queensAttacktheKing(self, queens, king):
        Q    = {(x,y) for x, y in queens}
        x, y = king
        res  = []
        
        # start at the kings position and move along each of the 8 directions horizontal, vertical and diagonal where a 
        # queen can attack and add the coordinates of said queen when found 
        for x0, y0 in  [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]:
            x1 = x0 + x
            y1 = y0 + y
            while 0 <= x1 <= 7 and 0 <= y1 <= 7:
                if (x1, y1) in Q:
                    res.append([x1, y1])
                    break
                    
                x1 += x0
                y1 += y0
            
        return res
        
    def test_suite(self):
        def shouldbe(q, k, r):
            if not (set(tuple(i) for i in self.queensAttacktheKing(q, k)) == set(tuple(i) for i in r)):
                raise ValueError('test failed')

        shouldbe([[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], [0,0], [[0, 1], [1,0], [3,3]])
        shouldbe([[0,0],[1,1],[2,2],[3,4],[3,5],[4,4]], [4,5], [[4, 4], [3, 4], [3, 5]])
    
Solution().test_suite()
