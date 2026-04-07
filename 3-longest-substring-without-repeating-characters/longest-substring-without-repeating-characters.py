class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxx=0
        left=0
        right=0
        set1=set()
        for right in range(len(s)):
            while s[right] in set1:
                set1.remove(s[left])
                left=left+1

            set1.add(s[right])
            maxx=max(maxx,right-left+1)
        return maxx
        
        
        