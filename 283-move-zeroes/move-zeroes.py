class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums
        n=len(nums)
        i=0
        j=1
        while(j<n):
            if nums[i]==0 and nums[j]!=0:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                i=i+1
                j=j+1
            elif nums[i]!=0:
                i=i+1
                j=j+1
            else:
                j=j+1
        return nums