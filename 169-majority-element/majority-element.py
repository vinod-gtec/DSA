class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash={}
        res=maj=0
        for i in nums:
            hash[i]=1+hash.get(i,0)
            if hash[i]>maj:
                res=i
                maj=hash[i]
        return res



            