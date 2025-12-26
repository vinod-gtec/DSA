class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        s=set(nums)
        longest=0
        for num in s:
            if num-1 not in s:
                curr=num
                count=1

                while curr+1 in s:
                    curr=curr+1
                    count=count+1
                longest=max(longest,count)
        return longest
