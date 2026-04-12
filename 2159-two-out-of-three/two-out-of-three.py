class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in nums1:
            if i in nums2 or i in nums3:
                ans.append(i)
        for j in nums2:
            if j in nums3:
                ans.append(j)
        ans=list(set(ans))
        return ans