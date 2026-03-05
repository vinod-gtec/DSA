class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        m=len(s)
        n=len(g)
        l=0
        r=0
        while(l<m and r<n):
            if(g[r]<=s[l]):
                r=r+1
            l=l+1
        return r
