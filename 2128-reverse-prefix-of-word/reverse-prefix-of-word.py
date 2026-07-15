class Solution(object):
    def reversePrefix(self, word, ch):
        ind=word.find(ch)
        if ind== -1:
            return word

        word1=word[:ind+1]
        word2=word[ind+1:]
        word3=word1[::-1]
        return word3+word2

        

        
        
        