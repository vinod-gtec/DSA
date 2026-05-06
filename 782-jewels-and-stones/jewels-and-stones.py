class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        counter=0
        set1=set(jewels)
        for i in stones:
            if i in set1:
                counter=counter+1
        return counter
        