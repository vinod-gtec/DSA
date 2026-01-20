class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = len(nums)
        p={}
        for i in nums:
            if i not in p:
                p[i]=1
            else:
                p[i]+=1
        return max(p,key=p.get)
            




            