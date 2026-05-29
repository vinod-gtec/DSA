class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        temp=len(nums)
        for i in range(0,len(nums)):
            if nums[i]==target:
                curr=abs(i-start)
                if curr<temp:
                    temp=curr
        return temp
        