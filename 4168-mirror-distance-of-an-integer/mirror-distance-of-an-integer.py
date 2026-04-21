class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=str(n)
        b=a[::-1]
        c=int(b)
        value=abs(n-c)
        return value