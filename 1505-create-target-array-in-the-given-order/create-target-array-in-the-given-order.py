class Solution(object):
    def createTargetArray(self, nums, index):
        ans=[]
        for i, j in zip(nums, index):
            ans.insert(j,i)

        return ans
        