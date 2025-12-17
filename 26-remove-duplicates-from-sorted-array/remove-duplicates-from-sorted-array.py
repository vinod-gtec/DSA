class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b=len(nums)
        i=1
        j=1
        for j in range(1,b):

            if(nums[i-1]==nums[j]):
                pass
            else:
                nums[i]=nums[j]
                i=i+1

        k=len(nums[0:i])
        return k