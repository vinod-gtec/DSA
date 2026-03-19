class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        n=len(nums)
        while(j<n):
            if nums[j]!=0:
                temp=nums[j]
                nums[j]=nums[i]
                nums[i]=temp
                i=i+1
            j=j+1
        return nums