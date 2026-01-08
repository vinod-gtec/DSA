class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        b=[[1]]
        temp=[]
        for i in range(1,rowIndex+1):
            temp=[]
            for j in range(0,i+1):
                if j==0 or j==i:
                    temp.append(1)
                else:
                    temp.append(b[i-1][j-1]+b[i-1][j])
            b.append(temp)
        return b[rowIndex]


                



            
        