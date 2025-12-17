class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=[]
        b=len(nums)
        i=0
        j=1
        while(i<b-1):
            if(nums[i]==nums[j]):
                nums.remove(nums[j])
                b=b-1
            else:
                i=i+1
                j=j+1
        k=len(nums)
        return k