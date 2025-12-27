class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=len(nums)
        maxi=nums[0]
        summ=0
        astart=-1
        send=-1

        for i in range(a):
            start=i
            summ=summ+nums[i]
            if(summ>maxi):
                maxi=summ
                start=astart
                send=i

            if(summ<=0):
                summ=0
        return maxi


