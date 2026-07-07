class Solution(object):
    def findDegrees(self, matrix):
        n = len(matrix)
        ans = [0] * n
        for i in range(n):
            ans[i] = sum(matrix[i])
        return ans
        