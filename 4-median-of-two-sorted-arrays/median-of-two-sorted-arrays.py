class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()
        if (len(nums1)%2==0):
            mid=(len(nums1)//2)
            mid_bef=mid-1
            ans=float(float(nums1[mid]+nums1[mid_bef])/2)
            return ans
        else:
            mid=len(nums1)//2

            return nums1[mid]
