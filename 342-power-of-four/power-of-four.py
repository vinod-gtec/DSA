class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d=n
        i=n
        if i==1:
            return True
        while(i>=4 and i%4==0):
            if(i==4):
                return True
            i=i//4
        return False
        