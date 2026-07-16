class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        count = 0
        for num in nums:
            while(num>0):
                d=num%10
                if d == digit:
                    count+=1
                num/=10
        
        return count

        