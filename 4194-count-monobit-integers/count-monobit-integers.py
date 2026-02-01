class Solution(object):
    def countMonobit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=2
        if n==0:
            return 1
        if n==1:
            return 2
        count=2
        while(2**i)-1<=n:
            count=count+1
            i=i+1
        return count


            
