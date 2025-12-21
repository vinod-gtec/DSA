class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        siz=len(nums)
        v=[-1]*(siz+1)
        for num  in nums:
            v[num]=num
        for i in range(len(v)):
            if v[i]==-1:
                return i
        return 0
            