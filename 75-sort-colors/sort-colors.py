class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        j=1
        for i in range(len(nums)):
            j=i
            while(j>0 and nums[j-1]>nums[j]):
                temp=nums[j]
                nums[j]=nums[j-1]
                nums[j-1]=temp
                j=j-1
        return nums


        