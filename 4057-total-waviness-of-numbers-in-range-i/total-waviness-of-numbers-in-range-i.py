class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        count=0
        if num2<100:
            return count
        for i in range(num1,num2+1): 
            if i<=100:
                continue
            else:
                temp=str(i)
                n=len(temp)
                for i in range(1,n-1):
                    if int(temp[i-1])<int(temp[i]) and int(temp[i])>int(temp[i+1]):
                        count=count+1
                    elif int(temp[i-1])>int(temp[i]) and int(temp[i])<int(temp[i+1]):
                        count=count+1
                    else:
                        pass
        return count      

        