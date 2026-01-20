class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        a=len(nums)
        count=0
        for i in nums:
            if i<k:
                count=count+1
            else:
                pass
        return count
        