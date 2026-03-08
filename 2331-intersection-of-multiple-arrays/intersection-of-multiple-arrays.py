class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        n=len(nums)
        a=[]
        if n==1 or n==0:
            nums[0].sort()
            return nums[0]
        for i in nums[0]:
            for j in range(1,n):
                if i not in nums[j]:
                    break
                elif j==n-1:
                    a.append(i)
                else:
                    continue
        a.sort()
        return a
                
        