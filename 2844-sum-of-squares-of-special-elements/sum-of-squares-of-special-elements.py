class Solution(object):
    def sumOfSquares(self, nums):
        squ=0
        n=len(nums)
        for i in range(n):
            if n%(i+1)==0:
                squ+=nums[i]**2
        
        return squ