class Solution(object):
    def maxProfit(self, prices):
        mi=prices[0]
        profit=0

        for i in range(1,len(prices)):
            if prices[i]<mi:
                mi=prices[i]
            elif prices[i]-mi>profit:
                profit=prices[i]-mi
        return profit

            

