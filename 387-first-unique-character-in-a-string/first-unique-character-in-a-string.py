class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        a={}
        for i in s:
            if i not in a:
                a[i]=1
            else:
                a[i]+=1
        for i in s:
            if a[i]==1:
                return s.index(i)
        return -1
        

