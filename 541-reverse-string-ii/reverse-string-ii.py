class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s=list(s)
        a=""
        for i in range(0,len(s),2*k):
            temp=s[i:k+i]
            val=temp[::-1]
            s[i:k+i]=val

        a=""
        for i in s:
            a=a+i 
        return a

        