class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        a=[]
        for i in range(left,right+1):
            if i <=9:
                a.append(i)
            else:
                temp=str(i)
                if "0" in temp:
                    continue
                else:
                    n=len(temp)
                    j=0
                    while(j<n):
                        if i%int(temp[j])!=0:
                            break
                        j=j+1
                        if(j==n):
                            a.append(i)
        return a
                    