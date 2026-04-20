class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        lis=[]
        for i in range(len(colors)-1):
            for j in range(i+1,len(colors)):
                if colors[i]!=colors[j]:
                    count=j-i
            lis.append(count)
        maxi=max(lis)
        return maxi

        