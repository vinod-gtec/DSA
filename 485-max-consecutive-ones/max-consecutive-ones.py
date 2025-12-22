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
        for num in nums:
            if num:
                count=count+1
                if(count>max1):
                    max1=count
            else:
                count=0
        return max1
        
            
