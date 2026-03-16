class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=len(nums)
        b=[0]*(2*a)
        c=len(b)
        for i in range(0,a):
            b[i]=nums[i]
            b[i+a]=nums[i]

        return b


        