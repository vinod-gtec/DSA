class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        l=len(nums1)
        nums1.sort()
        if(l%2==0):
            a=len(nums1)
            c=(a//2)
            med=float(float(nums1[c]+nums1[c-1])/2)
            return med
        else:
            return nums1[l//2]