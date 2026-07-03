class Solution(object):
    def reversePrefix(self, s, k):
        part1=s[:k]
        part2=s[k:]
        part3=part1[::-1]
        return part3+part2


