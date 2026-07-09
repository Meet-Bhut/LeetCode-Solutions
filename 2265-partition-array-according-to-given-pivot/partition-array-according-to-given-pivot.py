class Solution(object):
    def pivotArray(self, nums, pivot):
        small=[]
        mid=[]
        large=[]
        for i in range(len(nums)):
            if nums[i]>pivot:
                large.append(nums[i])
            elif nums[i]<pivot:
                small.append(nums[i])
            elif nums[i]==pivot:
                mid.append(nums[i])
        
        return small + mid + large