class Solution(object):
    def isAcronym(self, words, s):
        ans=""
        for word in words:
            ans+=word[0]

        return (ans==s)
        