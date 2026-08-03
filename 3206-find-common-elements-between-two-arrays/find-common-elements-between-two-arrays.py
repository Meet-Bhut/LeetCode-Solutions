class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        count1 = 0
        count2 = 0
        s1=set(nums1)
        s2=set(nums2)
        for i in nums1:
            if i in s2:
                count1+=1

        for j in nums2:
            if j in s1:
                count2+=1
        
        return [count1,count2]