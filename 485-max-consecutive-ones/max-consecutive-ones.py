class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b=len(nums)
        count=0
        max1=0
        j=0
        if len(nums)==0:
            return 0
        while(j<len(nums)):
            if(nums[j]==1):
                j=j+1
                count=count+1
                if(count>max1):
                    max1=count
            else:
                j=j+1
                count=0
        return max1
        
            
