# solution to leetcode problem #665

class Solution:
    def checkPossibility(self, nums):
        # scan from the left and the right and find pairs of elements in decreasing order
        # if scanning from each side 2 pairs are found that are in the wrong order
        # then the sequence is not non-decreasing
        if len(nums) <= 2:
            return True
        
        i = 0        
        x = nums[0]
        y = nums[len(nums)-1]
        left, right = 0, 0
        while i < len(nums):
            if nums[i] < x:
                left += 1
            else: #if nums[i] > x:
                x = nums[i] 
                
            if nums[-i - 1] > y:
                right += 1
            else:# nums[k] < y:
                y = nums[-i - 1]
                
            if left >= 2 and right >= 2:
                return False
            
            i += 1
            
        return True

tst  = [[4, 2, 3], [4, 2, 1]]
exp = [True,      False]

res = []
for e in tst:
    res += [Solution().checkPossibility(e)]

if exp != res:
    raise ValueError()


