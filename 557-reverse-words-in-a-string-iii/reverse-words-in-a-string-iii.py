class Solution(object):
    def reverseWords(self, s):
        ans=[]
        s=s.split(" ")
        for i in s:
            ans.append(i[::-1])
        
        return " ".join(ans)