class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        true = True
        false = False
        ans=[]
        maximum=max(candies)
        for candy in candies:
            if candy + extraCandies > maximum:
                ans.append(true)
            elif candy + extraCandies == maximum:
                ans.append(true)
            else:
                ans.append(false)
        return ans