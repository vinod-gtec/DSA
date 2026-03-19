class Solution(object):
    def maxProfit(self, prices):
        minn=prices[0]
        profit=0
        for i  in range(1,len(prices)):
            if prices[i]<minn:
                minn=prices[i]
            elif prices[i]-minn>profit:
                profit=prices[i]-minn
        return profit

            

