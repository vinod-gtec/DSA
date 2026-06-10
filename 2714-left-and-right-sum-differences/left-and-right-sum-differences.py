class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = sum(nums)
        left = 0
        ans = []

        for num in nums:
            total -= num      # right sum
            ans.append(abs(left - total))
            left += num       # update left sum

        return ans

        