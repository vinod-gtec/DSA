class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left=0
        right=len(s)-1
        d=list(s)
        a=['a','i','e','o','u','A','I','O','U','E']
        while(left<=right):
            if d[left] not in a:
                left=left+1
            elif d[right] not in a:
                right=right-1
            else:
                temp=d[left]
                d[left]=d[right]
                d[right]=temp
                left=left+1
                right=right-1
        return "".join(d)
