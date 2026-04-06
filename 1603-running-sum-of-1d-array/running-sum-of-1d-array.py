class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in range(len(nums)):
            summ=0
            for j in range(0,i+1):
                summ=summ+nums[j]
            a.append(summ)
        return a
        