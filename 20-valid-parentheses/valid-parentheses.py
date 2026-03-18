class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        len_s=len(s)
        a=[]
        count=0
        if len_s%2!=0:
            return False
        for i in range(len_s):
            if s[i]=="(" or s[i]=="{" or s[i]=="[":
                a.append(s[i])
                count=count+1
            else:
                
                if s[i]==")" and len(a)>0 and a[-1]=="(":
                    a.pop()
                    count=count-1
                elif s[i]=="}" and len(a)>0 and a[-1]=="{":
                    a.pop()
                    count=count-1
                elif s[i]=="]" and len(a)>0 and a[-1]=="[":
                    a.pop()
                    count=count-1
                else:
                    return False
        if count!=0:
            return False
        return True