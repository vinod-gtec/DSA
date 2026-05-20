class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n=len(A)
        i=0
        j=0
        a=[]
        for i in range(0,n):
            count=0
            for j in range(0,i+1):
                temp=B[0:i+1]
                if A[j] in temp:
                    count=count+1
            a.append(count)
        return a

            