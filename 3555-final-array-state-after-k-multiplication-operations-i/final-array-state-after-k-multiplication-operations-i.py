class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for i in range(k):
           nums[nums.index(min(nums))]=min(nums)*multiplier;    
        
        return nums