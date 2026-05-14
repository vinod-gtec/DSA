class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        max_val=max(nums)
        if n!=max_val+1:
            return False
        a=nums
        for i in range(1,n):
            if i in a:
                a.remove(i)
            else:
                return False
            
        if n-1 in a:
            return True
        return False