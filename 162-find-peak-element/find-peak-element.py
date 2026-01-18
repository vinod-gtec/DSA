class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        if l==1:
            return 0
        for i in range(l):
            left=nums[i-1] if i-1>=0 else float("-inf")
            right=nums[i+1] if i+1<l else float('-inf')

            if nums[i]>left and nums[i]>right:
                return i
            