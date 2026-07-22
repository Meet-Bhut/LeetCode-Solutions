class Solution(object):
    def minimumAverage(self, nums):
        ans=[]
        for i in range(len(nums)//2):
            a=max(nums)
            b=min(nums)
            avg=(a+b)/2.0
            ans.append(avg)
            nums.remove(a)
            nums.remove(b)

        ans.sort()
        return ans[0]
        