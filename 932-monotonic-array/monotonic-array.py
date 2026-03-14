class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)-1
        if n<1:
            return  True
        flag1=False
        flag2=False
        i=0
        while(i<n):
            if nums[i]<=nums[i+1]:
                i=i+1
                flag1=True
            else:
                flag1=False
                break
        i=0
        while(i<n):
            if nums[i]>=nums[i+1]:
                i=i+1
                flag2=True
            else:
                flag2=False
                break
            
        return flag1 or flag2

        