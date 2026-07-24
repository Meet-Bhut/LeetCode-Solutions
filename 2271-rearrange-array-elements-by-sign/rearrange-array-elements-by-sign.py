class Solution(object):
    def rearrangeArray(self, nums):
        ans=[]
        pos=[num for num in nums if num>0]
        neg=[num for num in nums if num<0]
        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])

        return ans