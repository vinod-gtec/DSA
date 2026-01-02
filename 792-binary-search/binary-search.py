class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        i=0
        j=n-1
        while(i<=j):
            if nums[i]== target:
                return i
            elif nums[j]==target:
                return j
            else:
                i=i+1
                j=j-1
        return -1
    
        