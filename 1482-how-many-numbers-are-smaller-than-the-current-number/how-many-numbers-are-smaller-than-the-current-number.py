class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        for j in nums:
            count=0
            for i in range(len(nums)):
                if nums[i]<j:
                    count=count+1
            a.append(count)
        return a
        