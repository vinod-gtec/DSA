class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in range(len(nums)):
            summ=0
            summ=sum(nums[0:i+1])
            a.append(summ)
        return a
        