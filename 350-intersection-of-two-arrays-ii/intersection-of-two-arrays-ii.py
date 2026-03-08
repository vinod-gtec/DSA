class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a=[]
        if len(nums1)<len(nums2):
            for i in nums1:
                if i in nums2:
                    a.append(i)
                    nums2.remove(i)
        else:
            for i in nums2:
                if i in nums1:
                    a.append(i)
                    nums1.remove(i)
        return a            
        