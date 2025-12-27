class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        mi=prices[0]
        j=1
        for i in range(1,len(prices)):
            if prices[i]<mi:
                mi=prices[i]
                j=j+1
            else:
                summ=prices[i]-mi
                profit=profit+summ
                mi=prices[j]
                j=j+1
        return profit