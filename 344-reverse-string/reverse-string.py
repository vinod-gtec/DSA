class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n=len(s)-1
        i=0
        while(i<=n//2):
            temp=s[i]
            s[i]=s[n-i]
            s[n-i]=temp
            i=i+1

            
        