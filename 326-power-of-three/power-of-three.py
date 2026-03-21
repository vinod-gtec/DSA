class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        summ=3
        i=1
        if n==1:
            return True
        while(summ<=n):
            if 3**i==n:
                return True
            else:
                i=i+1
                summ=3**i
        return False