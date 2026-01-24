class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summ=0
        a=len(nums)
        astart=-1
        aend=-1
        maxx=nums[0]
        
        for i in range(a):
            start=i
            summ=summ+nums[i]
            if summ>maxx:
                maxx=summ
                start=astart
                aend=i
            if(summ<0):
                summ=0
        return maxx 

            


        
            