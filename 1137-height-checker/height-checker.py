class Solution(object):
    def heightChecker(self, heights):
        expected = list(heights)
        expected.sort()
        count = 0
        for i in range(len(heights)):
            if heights[i]!=expected[i]:
                count+=1

        return count
