import math
class Solution(object):
    def co(self,nums,m):
        tot=0
        for i in range(len(nums)):
            tot+=math.ceil(float(nums[i])/m)
        return tot
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        lo=1
        high=max(piles)
        ans=0
        
        while(lo<=high):
            mid=(lo+high)//2
            total_hour=self.co(piles,mid)
            if total_hour<=h:
                high=mid-1
                ans=mid
            else:
                lo=mid+1
        return ans