class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d=n
        if n==1:
            return True
        while(d>5):
            s=str(d)
            summ=0
            for i in s:
                summ=summ+(int(i)*int(i))
            if summ==1:
                return True
            d=summ
        return False

