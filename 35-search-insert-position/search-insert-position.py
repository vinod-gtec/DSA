class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo=0
        high=len(nums)-1
        ans=high+1
        while lo<=high:
            mid=(lo+high)/2
            if nums[mid]>=target:
                ans=mid
                high=mid-1
            else:
                lo=mid+1
        return ans
        