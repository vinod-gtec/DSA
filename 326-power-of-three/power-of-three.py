class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        summ=n
        i=0
        if n<1:
            return False
        while(summ%3==0):
            summ=summ//3
        if summ==1:
            return True
        return False
    