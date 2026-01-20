class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        j=1
        a=len(nums)
        while i <a-1:
            j=i+1
            while j<a:
                if nums[i]+nums[j]==target:
                    return list([i,j])
                else:
                    j=j+1
            i=i+1

        