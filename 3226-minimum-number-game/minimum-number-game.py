class Solution(object):
    def numberGame(self, nums):
        nums.sort()
        for i in range(1,len(nums),2):
            nums[i-1],nums[i]= nums[i],nums[i-1]

        return nums

        