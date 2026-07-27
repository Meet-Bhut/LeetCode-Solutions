class Solution(object):
    def checkGoodInteger(self, n):
        dsum=0
        ssum=0
        while (n>0):
            digit=n%10
            dsum+=digit
            ssum+=digit*digit
            n/=10

        return ssum-dsum>=50

        