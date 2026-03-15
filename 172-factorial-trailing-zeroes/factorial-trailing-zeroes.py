class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        div=5
        while(n>=div):
            count=count + n//div
            div=div*5
        return count
        