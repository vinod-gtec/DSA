class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in nums:
            temp=str(i)
            n=len(temp)
            if n>1:
                for j in temp:
                    a.append(int(j))
            else:
                a.append(int(i))
        return a