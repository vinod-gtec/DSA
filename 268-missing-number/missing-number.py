class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        siz=len(nums)
        i=0
        while(i<siz):
            if i not in nums:
                a=i
                return a
            i=i+1
        return len(nums)
        