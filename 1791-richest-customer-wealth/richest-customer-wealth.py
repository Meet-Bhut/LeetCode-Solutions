class Solution(object):
    def maximumWealth(self, accounts):
        sum1=0
        for i in range(len(accounts)):
            sum2=0
            for j in range(len(accounts[i])):
                sum2+=accounts[i][j]

            if sum1<sum2:
                sum1=sum2

        return sum1





        