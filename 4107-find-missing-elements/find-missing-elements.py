class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()
        ans=[]
        a=max(nums)
        b=min(nums)
        for i in range(1, len(nums)):
            for j in range(nums[i - 1] + 1,nums[i]):
                ans.append(j)

        return ans
        