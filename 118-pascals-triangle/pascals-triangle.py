class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        a=[]
        temp_arr=[]
        for i in range(1,numRows+1):
            for j in range(0,i):
                if j<=0 or j==i-1:
                    temp_arr.append(1)
                else:
                    summ=a[i-2][j-1]+a[i-2][j]
                    temp_arr.append(summ)

            a.append(temp_arr)
            temp_arr=[]
        return a
        