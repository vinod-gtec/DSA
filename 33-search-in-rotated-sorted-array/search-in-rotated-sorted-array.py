class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nlen=len(nums)
        lo=0
        high=len(nums)-1
        while(lo<=high):
            mid=(lo+high)//2
            if(nums[mid]==target):
                return mid
            if(nums[lo]<=nums[mid]):
                if(nums[lo]<=target and target<=nums[mid]):
                    high=mid-1
                else:
                    lo=mid+1
            else:
                if(nums[mid]<=target and target<=nums[high]):
                    lo=mid+1
                else:
                    high=mid-1
        return -1
            
