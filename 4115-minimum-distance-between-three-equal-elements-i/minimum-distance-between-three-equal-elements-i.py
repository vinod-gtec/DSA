import math
class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        good_tuple=False
        n=len(nums)
        min_dist=float('inf')
        for i in range(n-2):
            for j in range(i+1,n-1):
                k=j+1
                while(k<n):
                    if nums[i]==nums[j] and nums[j]==nums[k]:
                        good_tuple=True
                        dist=abs(i - j) + abs(j - k) + abs(k - i)
                        min_dist=min(dist,min_dist) 
                    k=k+1

        if good_tuple is not True:
            return -1
        return min_dist

