class Solution:
    def jump(self, nums: List[int]) -> int:     
        # from the current point to the max. point you can reach find the point
        # in the range that allows the algorithm to jump furthest.
        # repeat until the end is reached

        i     = 0
        jumps = 1
        
        if len(nums) == 1: return 0            
        
        maxsofar = nums[0]
        while maxsofar < len(nums) - 1:            
            jumps += 1           
            
            m0 = maxsofar
            i0 = 0
            
            # find the point in the range of allowed indices you can reach and
            # jump to this point
            while i < maxsofar:                
                i += 1
                if m0  < nums[i] + i:
                    m0 = nums[i] + i
                    i0 = i
            
            maxsofar = m0 
            i        = i0    
            
        return jumps
        
