class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        k=0
        j=1
        ne=0
        if n==1:
            return 1

        for i in range(n-1):
            ne=k+j
            k=j
            j=ne
        return ne



        