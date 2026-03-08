class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        a=len(nums1)
        b=len(nums2)
        i,j=0,0
        res=[]
        while i<a and j<b:
            if nums1[i]>nums2[j]:
                j=j+1
            elif nums1[i]<nums2[j]:
                i=i+1
            else:
                res.append(nums1[i])
                i=i+1
                j=j+1
        return res
        