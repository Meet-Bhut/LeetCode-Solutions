class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        ans=[]
        
        for num in nums:
            count=0
            for i in range(len(nums)):
                if num>nums[i]:
                    count+=1

            ans.append(count)
        
        return ans

        