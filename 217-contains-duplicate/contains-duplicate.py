class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a=set()
        for i in nums:
            if i in a:
                return True
            else:
                a.add(i)
        return False