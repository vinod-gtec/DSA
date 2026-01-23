class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        a=list(s)
        n=len(a)
        value=0
        prev=0
        curr=0
        for i in range(n-1,-1,-1):
            curr=dict[a[i]]

            if curr<prev:
                value=value-curr
            else:
                value=value+curr
            prev=curr
        return value