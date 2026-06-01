class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        flag=0
        n=len(s)
        i=0
        if len(s)!=len(goal):
            return False
        while(i<n):
            for j in range(n):
                current=s[(i+j)%n]
                if current !=goal[j]:
                    flag=0
                    break
                flag=1
            
            if flag==1:
                return True
            i=i+1
        return False