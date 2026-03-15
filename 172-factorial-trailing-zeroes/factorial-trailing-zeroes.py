class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=str(factorial(n))
        len_a=len(a)
        count=0
        for i in range(len_a-1,-1,-1):
            if a[i]=="0":
                count=count+1
            else:
                break
        return count
    
    def factorial(self,n):
        if n==1:
            return n
        return n*factorial(n-1)
        