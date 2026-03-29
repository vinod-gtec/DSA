class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=list(s)
        t=list(t)
        i=0
        for j in range(len(t)):
            if i>=len(s):
                break
            if s[i]==t[j]:
                i=i+1
        if len(s)==i:
            return True
        return False


            