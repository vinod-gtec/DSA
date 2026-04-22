class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash1={}
        for i in range(len(nums)):
            if nums[i] in hash1:
                if abs(hash1[nums[i]]-i)<=k:
                    return True
            hash1[nums[i]]=i
        return False