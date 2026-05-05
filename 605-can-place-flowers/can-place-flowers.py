class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n==0:
            return True
        if len(flowerbed)==1:
            if flowerbed[0]==0:
                return True
            else:
                return False
        counter=0
        for i in range(len(flowerbed)):
            if i==0:
                if flowerbed[i]==0 and flowerbed[i+1]==0:
                    counter=counter+1
                    flowerbed[i]=1
            elif i==len(flowerbed)-1:
                    if flowerbed[i-1]==0 and flowerbed[i]==0:
                        flowerbed[i]=1
                        counter=counter+1
            else:
                    if flowerbed[i+1]==0 and flowerbed[i-1]==0 and flowerbed[i]==0:
                        flowerbed[i]=1
                        counter=counter+1
        if counter>=n:
            return True
        return False
        