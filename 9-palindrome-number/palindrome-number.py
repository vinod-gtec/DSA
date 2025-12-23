class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev=0
        num=x
        if x<0:
            return False
         
        while(num!=0):
            rev=rev*10+num%10
            num=num//10
        return rev==x
        