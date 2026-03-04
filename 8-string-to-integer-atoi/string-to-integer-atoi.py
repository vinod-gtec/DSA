INT_MIN = -2**31
INT_MAX = 2**31 - 1
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag=1
        start=0
        end=len(s)
        while start<end and s[start]==" ":
            start=start+1
        if start<end and (s[start]=="-" or s[start]=="+"):
            if s[start]=="-":
                flag=-1
                start=start+1
            else:
                flag=1
                start=start+1
        return self.helper(start,s,0,flag)
    def helper(self,start,s,num,flag):
        if start>=len(s) or not s[start].isdigit():
            return flag*num
        
        num=num*10 +int(s[start])

        if flag*num<=INT_MIN:
            return INT_MIN
        if flag*num>=INT_MAX:
            return INT_MAX
        
        return self.helper(start+1,s,num,flag)
        
                    



        