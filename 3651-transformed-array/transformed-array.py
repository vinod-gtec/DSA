class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        b=len(nums)
        for i in range (b):
            if nums[i]>0:
                j=i
                pos_push=nums[i]
                a.append(nums[(j+pos_push)%b])
            elif nums[i]<0:
                j=i
                pos_push=nums[i]
                a.append(nums[(j+pos_push)%b])
            else:
                a.append(nums[i])
        return a



        