class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=0
        r=len(s)-1
        s=list(s)
        letter="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while(l<r):
            if s[l] in letter and s[r] in letter:
                temp=s[r]
                s[r]=s[l]
                s[l]=temp
                r=r-1
                l=l+1
            elif s[l] not in letter:
                l=l+1
            elif s[r] not in letter:
                r=r-1
            else:
                l=l+1
                r=r-1

        return "".join(s)
            
        