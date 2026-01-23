class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        lo=min(bloomDay)
        high=max(bloomDay)
        n=len(bloomDay)
        ans=high
        if(len(bloomDay)<m*k):
            return -1
        while(lo<=high):
            mid=(lo+high)//2
            if self.possible(bloomDay,mid,m,k):
                ans=mid
                high=mid-1
            else:
                lo=mid+1
        return ans
            

    def possible(self,bloomDay,day,m,k):
        count=0
        bquets=0
        for i in range(len(bloomDay)):
            if(bloomDay[i]<=day):
                count=count+1
            else:
                bquets+=count//k
                count=0

        bquets+=count//k
        if bquets>=m:
            return True
        return False