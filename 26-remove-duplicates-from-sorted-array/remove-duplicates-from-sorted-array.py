class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=len(nums)
        i=0
        j=1
        while(j<a):
            if (nums[j]!=nums[i]):
                i=i+1
                nums[i]=nums[j]
            j=j+1
        return i+1
