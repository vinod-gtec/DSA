class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=len(nums)
        summ=0
        maxx=nums[0]
        astart=-1
        aend=-1

        for i in range(a):
            start=i
            summ=summ+nums[i]
            if (summ>maxx):
                maxx=summ
                start=astart
                aend=i
            if summ<=0:
                summ=0
        return maxx
        
            