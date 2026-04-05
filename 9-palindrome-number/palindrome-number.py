class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a=str(x)
        b=""
        for i in range(len(a)-1,-1,-1):
            b=b+a[i]
        if a==b:
            return True
        return False
        