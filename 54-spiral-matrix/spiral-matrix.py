class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """  
        a=[]
        n=len(matrix)
        m=len(matrix[0])
        top=0
        left=0
        bottom=n-1
        right=m-1
        while(top<=bottom and left<=right):
            for i in range(left,right+1):
                a.append(matrix[top][i])
            top=top+1
            for i in range(top,bottom+1):
                a.append(matrix[i][right])
            right=right-1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    a.append(matrix[bottom][i])
            bottom=bottom-1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    a.append(matrix[i][left])
            left=left+1
        return a
            
       
                            


                
                

        