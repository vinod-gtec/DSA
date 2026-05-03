class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d=n
        if n==1:
            return True
        seen=set()
        while(d!=1):
            s=str(d)
            summ=0
            for i in s:
                summ=summ+(int(i)*int(i))
            if summ==1:
                return True
            d=summ
            if d in seen:
                break
            else:
                seen.add(summ)
        return False

