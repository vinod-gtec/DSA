class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        high=len(nums)-1
        lo=0
        if l==1:
            return 0
        while(lo<=high):
            mid=(lo+high)//2
            if mid-1<0:
                left=float("-inf")
            else:
                left=nums[mid-1]
            if mid+1>=l:
                right=float("-inf")
            else:
                right=nums[mid+1]
            if nums[mid]>left and nums[mid]>right:
                return mid

            elif nums[mid]<left:
                high=mid-1
            else:
                lo=mid+1

        