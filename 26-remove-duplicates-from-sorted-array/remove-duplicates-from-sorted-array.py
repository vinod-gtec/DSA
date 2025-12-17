class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b=len(nums)
        i=0
        j=1
        while(j<b):
            if(nums[i]!=nums[j]):
                i=i+1
                nums[i]=nums[j]
            j=j+1
        k=nums[0:i]
        return i+1