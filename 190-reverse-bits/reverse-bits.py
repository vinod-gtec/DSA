class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=bin(n)[2:].zfill(32)
        a=str(s)
        b=a[::-1]
        d=int(b,2)
        return d
        