class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo=0
        high=len(nums)-1
        ans=10*100
        while(lo<=high):
            mid=(lo+high)//2
            if(nums[lo]<=nums[mid]):
                ans=min(ans,nums[lo])
                lo=mid+1
            else:
                ans=min(ans,nums[mid])
                high=mid-1
        return ans
