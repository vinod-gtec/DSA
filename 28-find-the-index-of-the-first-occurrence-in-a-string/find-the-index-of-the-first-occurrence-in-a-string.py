class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n=len(needle)-1
        i=0
        j=0
        while(i<=len(haystack)-len(needle)):
            j=i+n
            if haystack[i:j+1]==needle[:]:
                return i
            else:
                i=i+1
        return -1
        