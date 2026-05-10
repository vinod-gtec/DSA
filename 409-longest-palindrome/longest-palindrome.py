class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        set1={}
        for i in s :
            set1[i]=set1.get(i,0)+1

        freq_is=False
        res=0

        for freq in set1.values():
            if (freq%2==0):
                res=freq+res
            else:
                freq_is=True
                res=res+freq-1

        if freq_is:
            return res+1
        return res
        