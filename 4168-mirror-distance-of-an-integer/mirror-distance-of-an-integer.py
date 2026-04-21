class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=str(n)
        b=int(a[::-1])
        value=abs(n-b)
        return value